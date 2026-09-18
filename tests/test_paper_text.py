import importlib.util
from pathlib import Path
import tempfile
import unittest

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


if __name__ == "__main__":
    unittest.main()
