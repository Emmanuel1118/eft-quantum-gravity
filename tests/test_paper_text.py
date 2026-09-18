import importlib.util
import contextlib
import hashlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("paper_text", Path(__file__).resolve().parents[1] / "scripts/paper_text.py")
paper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(paper)


class PaperTextTests(unittest.TestCase):
    def test_page_selection(self):
        self.assertEqual(paper.selected_pages("3,1-2,2", 3), [1, 2, 3])
        for value in ("0", "4", "3-2", "1-2-3"):
            with self.assertRaises(ValueError):
                paper.selected_pages(value, 3)

    def test_search_handles_pdf_line_breaks(self):
        self.assertIn(paper.normalized("nonanalytic momentum"), paper.normalized("Nonana-\nlytic   momentum"))

    def test_output_cannot_replace_source(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "source.pdf"
            path.write_bytes(b"unchanged")
            with self.assertRaises(ValueError):
                paper.write_new(path, "bad", path, force=True)
            self.assertEqual(path.read_bytes(), b"unchanged")

    def test_existing_output_preserved(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "text.txt"
            path.write_text("original")
            with self.assertRaises(FileExistsError):
                paper.write_new(path, "bad", Path(directory) / "source.pdf")
            self.assertEqual(path.read_text(), "original")

    def test_blank_pdf_not_reported_as_success(self):
        from pypdf import PdfWriter
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "blank.pdf"
            writer = PdfWriter()
            writer.add_blank_page(width=100, height=100)
            writer.write(path)
            self.assertEqual(paper.extract(path)["textless_pages"], [1])
            self.assertEqual(paper.main([str(path)]), 1)

    def test_malformed_pdf_has_controlled_failure(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "invalid.pdf"
            path.write_bytes(b"not a PDF")
            self.assertEqual(paper.main([str(path)]), 2)

    def cache(self, directory):
        source = Path(directory) / "source.pdf"
        source.write_bytes(b"source bytes")
        path = Path(directory) / "extraction.json"
        data = {"source_file": str(source), "source_url": "https://example.org/paper",
                "sha256": hashlib.sha256(source.read_bytes()).hexdigest(), "page_count": 10,
                "pages": [{"page": 2, "text": "A " + "prefix " * 100 + "Nonana-\nlytic momentum" + " suffix" * 100},
                          {"page": 7, "text": "Another nonanalytic result", "matches": False}]}
        path.write_text(json.dumps(data), encoding="utf-8")
        return path, source

    def test_cached_search_without_pdf_recomputes_matches_and_bounds_output(self):
        with tempfile.TemporaryDirectory() as directory:
            path, source = self.cache(directory)
            source.unlink()
            stdout, stderr = io.StringIO(), io.StringIO()
            with patch.object(paper, "extract", side_effect=AssertionError("PDF reopened")), contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                code = paper.main([str(path), "--from-json", "--find", "nonanalytic", "--max-matches", "1", "--context-chars", "20"])
            self.assertEqual(code, 0)
            self.assertIn("Showing 1 of 2", stdout.getvalue())
            self.assertLess(len(stdout.getvalue()), 250)
            self.assertIn("covered PDF pages 2,7", stderr.getvalue())

    def test_cache_missing_pages_and_changed_pdf_fail(self):
        with tempfile.TemporaryDirectory() as directory:
            path, source = self.cache(directory)
            self.assertEqual(paper.read_cache(path, verify_pdf=source)["page_count"], 10)
            with self.assertRaisesRegex(ValueError, "not cached"):
                paper.read_cache(path, pages="2-3")
            source.write_bytes(b"changed")
            with self.assertRaisesRegex(ValueError, "hash"):
                paper.read_cache(path, verify_pdf=source)

    def test_cache_rejects_duplicate_pages_and_malformed_schema(self):
        with tempfile.TemporaryDirectory() as directory:
            path, _ = self.cache(directory)
            data = json.loads(path.read_text())
            data["pages"].append(data["pages"][0])
            path.write_text(json.dumps(data))
            with self.assertRaisesRegex(ValueError, "duplicate page"):
                paper.read_cache(path)
            path.write_text("[]")
            self.assertEqual(paper.main([str(path), "--from-json"]), 2)

    def test_cached_output_cannot_overwrite_pdf_or_cache(self):
        with tempfile.TemporaryDirectory() as directory:
            path, source = self.cache(directory)
            original = path.read_bytes()
            for target in (path, source):
                self.assertEqual(paper.main([str(path), "--from-json", "--output", str(target), "--force"]), 2)
            self.assertEqual(path.read_bytes(), original)
            self.assertEqual(source.read_bytes(), b"source bytes")

    def test_full_json_keeps_undisplayed_pages_and_text(self):
        with tempfile.TemporaryDirectory() as directory:
            path, _ = self.cache(directory)
            dest = Path(directory) / "selected.json"
            with contextlib.redirect_stdout(io.StringIO()):
                code = paper.main([str(path), "--from-json", "--find", "nonanalytic", "--max-matches", "1", "--json-output", str(dest)])
            self.assertEqual(code, 0)
            saved = json.loads(dest.read_text())
            self.assertEqual(len(saved["pages"]), 2)
            self.assertGreater(len(saved["pages"][0]["text"]), 1000)
            self.assertEqual(paper.format_matches(saved["pages"], "nonanalytic", mode="pages"), "Matching PDF pages: 2, 7")
            self.assertIn("Nonana-\nlytic", paper.format_matches(saved["pages"], "nonanalytic", mode="full"))


if __name__ == "__main__":
    unittest.main()
