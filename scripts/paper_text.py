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


def read_cache(path, pages=None, query=None, verify_pdf=None):
    """Search a page-aware extraction without opening or requiring its PDF."""
    result = json.loads(Path(path).read_text(encoding="utf-8-sig"))
    if (not isinstance(result, dict) or
            not isinstance(result.get("page_count"), int) or result["page_count"] < 1 or
            not re.fullmatch(r"[0-9a-fA-F]{64}", str(result.get("sha256", ""))) or
            not isinstance(result.get("source_file"), str) or not result["source_file"] or
            not isinstance(result.get("pages"), list)):
        raise ValueError("Invalid extraction cache: missing page/provenance data")
    available = {}
    for record in result["pages"]:
        if (not isinstance(record, dict) or not isinstance(record.get("page"), int) or
                not 1 <= record["page"] <= result["page_count"] or
                record["page"] in available or not isinstance(record.get("text"), str)):
            raise ValueError("Invalid extraction cache: malformed or duplicate page")
        available[record["page"]] = record["text"]
    if verify_pdf and hashlib.sha256(Path(verify_pdf).read_bytes()).hexdigest() != result["sha256"].lower():
        raise ValueError("Cached extraction does not match the supplied PDF hash")
    requested = selected_pages(pages, result["page_count"]) if pages else sorted(available)
    missing = sorted(set(requested) - available.keys())
    if missing:
        raise ValueError("Pages {} are not cached; extract them from the source PDF".format(missing))
    result["pages"] = [{"page": n, "text": available[n], "has_text": bool(available[n].strip()),
                        "matches": query is None or normalized(query) in normalized(available[n])}
                       for n in requested]
    result["query"] = query
    result["textless_pages"] = [p["page"] for p in result["pages"] if not p["has_text"]]
    return result


def format_matches(matched, query=None, mode="snippets", context_chars=160, limit=5):
    """Bound displayed search results; saved JSON still holds every selected page."""
    shown = matched[:limit] if query else matched
    if mode == "pages":
        output = "Matching PDF pages: " + ", ".join(str(p["page"]) for p in shown)
    else:
        blocks = []
        for page in shown:
            text = page["text"]
            if query and mode == "snippets":
                # Normalized excerpts are search aids, not verbatim quotations.
                text = normalized(text)
                start = text.index(normalized(query))
                left = max(0, start - context_chars)
                right = min(len(text), start + len(normalized(query)) + context_chars)
                text = ("..." if left else "") + text[left:right] + ("..." if right < len(text) else "")
            blocks.append("=== PDF page {} ===\n{}".format(page["page"], text))
        output = "\n\n".join(blocks)
    if len(shown) < len(matched):
        output += "\nShowing {} of {} matching pages; narrow --pages or increase --max-matches.".format(len(shown), len(matched))
    return output


def write_new(path, content, source, force=False):
    path = Path(path)
    if path.resolve() == Path(source).resolve():
        raise ValueError("Output must not overwrite the source PDF")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w" if force else "x", encoding="utf-8", newline="\n") as stream:
        stream.write(content)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path, help="Selected PDF, or extraction JSON with --from-json")
    parser.add_argument("--from-json", action="store_true", help="Reuse cached extraction; do not open the PDF")
    parser.add_argument("--verify-pdf", type=Path, help="With --from-json, check the cache against this PDF's SHA-256")
    parser.add_argument("--pages", help="1-based PDF page numbers, e.g. 9-11,15")
    parser.add_argument("--find", help="Case-insensitive phrase search with whitespace normalization")
    parser.add_argument("--format", choices=("snippets", "pages", "full"), default="snippets",
                        help="Search display (default: normalized snippet from first match on each page)")
    parser.add_argument("--max-matches", type=int, default=5, help="Maximum matching pages displayed (default: 5)")
    parser.add_argument("--context-chars", type=int, default=160, help="Snippet characters on each side of the match")
    parser.add_argument("--source-url", help="Canonical source URL, never a temporary download URL")
    parser.add_argument("--output", type=Path, help="Write UTF-8 extracted text instead of stdout")
    parser.add_argument("--json-output", type=Path, help="Write metadata and page-aware extraction JSON")
    parser.add_argument("--render-dir", type=Path, help="Render selected pages to PNG with pypdfium2")
    parser.add_argument("--force", action="store_true", help="Replace existing generated output only")
    args = parser.parse_args(argv)
    try:
        if args.find is not None and not args.find.strip():
            raise ValueError("Search phrase cannot be blank")
        if args.max_matches < 1 or args.context_chars < 0:
            raise ValueError("--max-matches must be positive; --context-chars must be nonnegative")
        if args.verify_pdf and not args.from_json:
            raise ValueError("--verify-pdf requires --from-json")
        if args.from_json and (args.render_dir or args.source_url):
            raise ValueError("Use the original PDF for rendering; cached provenance cannot be overridden")
        result = (read_cache(args.pdf, args.pages, args.find, args.verify_pdf) if args.from_json
                  else extract(args.pdf, args.pages, args.find, args.source_url))
        protected = {args.pdf.resolve(), Path(result["source_file"]).resolve()}
        if args.verify_pdf:
            protected.add(args.verify_pdf.resolve())
        # Validate all output destinations before creating any output.
        outputs = [p for p in (args.output, args.json_output) if p]
        if len({p.resolve() for p in outputs}) != len(outputs):
            raise ValueError("Text and JSON outputs must be different files")
        for dest in outputs:
            if dest.resolve() in protected:
                raise ValueError("Output must not overwrite the source PDF or extraction cache")
            if dest.exists() and not args.force:
                raise FileExistsError("Output exists: {} (use --force for generated output)".format(dest))
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
        output = format_matches(matched, args.find, args.format, args.context_chars, args.max_matches)
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
        if args.from_json:
            print("Cache-only search: covered PDF pages {}. Missing pages were not searched."
                  .format(",".join(str(p["page"]) for p in result["pages"])), file=sys.stderr)
            print("Source: {}; SHA-256: {}".format(result.get("source_url") or result["source_file"], result["sha256"]), file=sys.stderr)
        return 0 if matched and any(p["has_text"] for p in matched) else 1
    except (OSError, ValueError, ImportError) as error:
        print("ERROR: {}".format(error), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
