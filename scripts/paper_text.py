"""Extract/search a selected PDF with stable physical-page references.

Requires pypdf. Optional page rendering requires pypdfium2.
PDFs and derived output are disposable; this utility never modifies the source.
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path


def selected_pages(spec, count):
    if not spec:
        return list(range(1, count + 1))
    result = set()
    for part in spec.split(","):
        bounds = part.strip().split("-")
        if len(bounds) > 2:
            raise ValueError("Pages must look like 1,3-5")
        start = int(bounds[0])
        end = int(bounds[-1])
        if not 1 <= start <= end <= count:
            raise ValueError("Page range must be within 1..{}".format(count))
        result.update(range(start, end + 1))
    return sorted(result)


def normalized(text):
    text = re.sub(r"[\u00ad\u0002]", "", text)
    text = re.sub(r"(?<=\w)-\s*\n\s*(?=\w)", "", text)
    return " ".join(text.split()).casefold()


def extract(path, pages=None, query=None, source_url=None):
    from pypdf import PdfReader
    from pypdf.errors import PyPdfError
    try:
        reader = PdfReader(path)
    except PyPdfError as error:
        raise ValueError("Cannot read PDF: {}".format(error)) from error
    if reader.is_encrypted and not reader.decrypt(""):
        raise ValueError("Password-protected PDF: provide an accessible source")
    records = []
    for number in selected_pages(pages, len(reader.pages)):
        text = reader.pages[number - 1].extract_text() or ""
        records.append({"page": number, "text": text,
                        "has_text": bool(text.strip()),
                        "matches": query is None or normalized(query) in normalized(text)})
    return {"source_file": str(Path(path).resolve()), "source_url": source_url,
            "sha256": hashlib.sha256(Path(path).read_bytes()).hexdigest(),
            "page_count": len(reader.pages), "page_numbering": "1-based PDF page index",
            "metadata": {str(k): str(v) for k, v in (reader.metadata or {}).items()},
            "query": query, "pages": records,
            "textless_pages": [r["page"] for r in records if not r["has_text"]]}


def write_new(path, content, source, force=False):
    path = Path(path)
    if path.resolve() == Path(source).resolve():
        raise ValueError("Output must not overwrite the source PDF")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w" if force else "x", encoding="utf-8", newline="\n") as stream:
        stream.write(content)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--pages", help="1-based PDF page numbers, e.g. 9-11,15")
    parser.add_argument("--find", help="Case-insensitive phrase search with whitespace normalization")
    parser.add_argument("--source-url", help="Canonical source URL, never a temporary download URL")
    parser.add_argument("--output", type=Path, help="Write UTF-8 extracted text instead of stdout")
    parser.add_argument("--json-output", type=Path, help="Write metadata and page-aware extraction JSON")
    parser.add_argument("--render-dir", type=Path, help="Render selected pages to PNG with pypdfium2")
    parser.add_argument("--force", action="store_true", help="Replace existing generated output only")
    args = parser.parse_args(argv)
    try:
        if args.find is not None and not args.find.strip():
            raise ValueError("Search phrase cannot be blank")
        # Validate all output destinations before creating any output.
        outputs = [p for p in (args.output, args.json_output) if p]
        if len({p.resolve() for p in outputs}) != len(outputs):
            raise ValueError("Text and JSON outputs must be different files")
        for dest in outputs:
            if dest.resolve() == args.pdf.resolve():
                raise ValueError("Output must not overwrite the source PDF")
            if dest.exists() and not args.force:
                raise FileExistsError("Output exists: {} (use --force for generated output)".format(dest))
        result = extract(args.pdf, args.pages, args.find, args.source_url)
        matched = [p for p in result["pages"] if p["matches"]]
        rendered_paths = []
        if args.render_dir:
            import pypdfium2 as pdfium
            for p in result["pages"]:
                dest = args.render_dir / "page-{:04d}.png".format(p["page"])
                if dest.exists() and not args.force:
                    raise FileExistsError("Rendered page exists: {}".format(dest))
                rendered_paths.append((p["page"], dest))
            args.render_dir.mkdir(parents=True, exist_ok=True)
            with pdfium.PdfDocument(str(args.pdf)) as document:
                for number, dest in rendered_paths:
                    page = document[number - 1]
                    bitmap = page.render(scale=1.5)
                    bitmap.to_pil().save(dest)
                    bitmap.close()
                    page.close()
        output = "\n\n".join("=== PDF page {} ===\n{}".format(p["page"], p["text"]) for p in matched)
        if args.output:
            write_new(args.output, output + "\n", args.pdf, args.force)
        else:
            if hasattr(sys.stdout, "reconfigure"):
                sys.stdout.reconfigure(encoding="utf-8")
            print(output)
        if args.json_output:
            write_new(args.json_output, json.dumps(result, ensure_ascii=False, indent=2) + "\n", args.pdf, args.force)
        if result["textless_pages"]:
            print("WARNING: No extractable text on pages {}; inspect rendered pages or use OCR.".format(result["textless_pages"]), file=sys.stderr)
        print("PDF pages: {}; selected: {}; matching: {}".format(result["page_count"], len(result["pages"]), len(matched)), file=sys.stderr)
        return 0 if matched and any(p["has_text"] for p in matched) else 1
    except (OSError, ValueError, ImportError) as error:
        print("ERROR: {}".format(error), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
