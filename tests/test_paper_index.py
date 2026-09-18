import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location("paper_index", Path(__file__).resolve().parents[1] / "scripts/paper_index.py")
index = importlib.util.module_from_spec(spec)
spec.loader.exec_module(index)


class IndexTests(unittest.TestCase):
    def sample(self):
        return {"headers": ["Paper ID", "Title", "DOI", "arXiv ID", "Drive status", "Drive file ID", "Your familiarity"],
                "rows": [["P1", "First", "10.1234/abc", "0802.0716", "Present", "file1", "Read substantially"],
                         ["P2", "Second", "", "hep-th/0405239", "Absent", "", "Not assessed"]]}

    def test_identifier_variants(self):
        self.assertEqual(index.lookup(self.sample(), doi="https://doi.org/10.1234/ABC")[0]["Paper ID"], "P1")
        self.assertEqual(index.lookup(self.sample(), arxiv="https://arxiv.org/pdf/0802.0716v1.pdf")[0]["Paper ID"], "P1")

    def test_sort_keeps_identity_and_human_input(self):
        snapshot = self.sample()
        snapshot["rows"].reverse()
        match = index.lookup(snapshot, arxiv="arXiv:0802.0716v2")[0]
        self.assertEqual(match["Paper ID"], "P1")
        self.assertEqual(match["Your familiarity"], "Read substantially")

    def test_conflicting_identifiers_require_review(self):
        with self.assertRaises(ValueError):
            index.lookup(self.sample(), doi="10.1234/abc", arxiv="hep-th/0405239")

    def test_duplicate_work_is_flagged(self):
        snapshot = self.sample()
        snapshot["rows"][1][3] = "0802.0716v3"
        self.assertTrue(any("Duplicate arXiv" in issue for issue in index.validate(snapshot)))

    def test_invalid_presence_is_flagged(self):
        snapshot = self.sample()
        snapshot["rows"][0][5] = ""
        self.assertTrue(index.validate(snapshot))


if __name__ == "__main__":
    unittest.main()
