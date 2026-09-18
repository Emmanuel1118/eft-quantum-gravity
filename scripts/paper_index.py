"""Validate a disposable catalog snapshot or look up records before connector edits.

Input JSON: {"headers": [...], "rows": [[...], ...]} using live displayed values.
This utility is read-only. The Google Sheet remains authoritative.
"""
import argparse
import json
import re
from pathlib import Path


def normalize_doi(value):
    value = str(value or "").strip().casefold()
    return re.sub(r"^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)", "", value)


def normalize_arxiv(value):
    value = str(value or "").strip().casefold()
    value = re.sub(r"^(?:https?://arxiv\.org/(?:abs|pdf)/|arxiv:\s*)", "", value)
    value = re.sub(r"\.pdf$", "", value)
    return re.sub(r"v\d+$", "", value)


def records(snapshot, identity_only=False):
    headers = snapshot["headers"]
    required = {"Paper ID", "Title", "DOI", "arXiv ID"}
    if not identity_only:
        required |= {"Drive status", "Drive file ID", "Your familiarity"}
    if len(set(headers)) != len(headers) or not required <= set(headers):
        raise ValueError("Missing or duplicate catalog headers")
    for row in snapshot["rows"]:
        if len(row) > len(headers):
            raise ValueError("Row extends beyond catalog headers")
        if any(str(v or "").strip() for v in row):
            yield dict(zip(headers, list(row) + [""] * (len(headers) - len(row))))


def validate(snapshot):
    issues = []
    seen = {key: {} for key in ("Paper ID", "DOI", "arXiv ID", "Drive file ID")}
    for row in records(snapshot):
        paper_id = row["Paper ID"]
        if not paper_id or not row["Title"]:
            issues.append("Every populated record needs a Paper ID and Title")
        if row["Drive status"] == "Present" and not row["Drive file ID"]:
            issues.append("{}: Present requires a verified Drive file ID".format(paper_id))
        for key in seen:
            value = normalize_doi(row[key]) if key == "DOI" else normalize_arxiv(row[key]) if key == "arXiv ID" else row[key]
            if value:
                if value in seen[key]:
                    issues.append("Duplicate {}: {} and {}".format(key, seen[key][value], paper_id))
                seen[key][value] = paper_id
    return issues


def lookup(snapshot, doi=None, arxiv=None):
    matches = []
    for row in records(snapshot, identity_only=True):
        if ((doi and normalize_doi(row["DOI"]) == normalize_doi(doi)) or
                (arxiv and normalize_arxiv(row["arXiv ID"]) == normalize_arxiv(arxiv))):
            matches.append(row)
    if len(matches) > 1:
        raise ValueError("Ambiguous identifiers: review matching records before any write")
    if matches:
        row = matches[0]
        for key, candidate, normalize in (("DOI", doi, normalize_doi), ("arXiv ID", arxiv, normalize_arxiv)):
            if candidate and row[key] and normalize(candidate) != normalize(row[key]):
                raise ValueError("Conflicting {} on matched record: review before any write".format(key))
    return matches


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot", type=Path)
    parser.add_argument("--doi")
    parser.add_argument("--arxiv")
    parser.add_argument("--lookup-only", action="store_true",
                        help="Match a compact live projection: Paper ID, Title, DOI, arXiv ID; skip full audit")
    args = parser.parse_args()
    try:
        snapshot = json.loads(args.snapshot.read_text(encoding="utf-8-sig"))
        if args.lookup_only and not (args.doi or args.arxiv):
            raise ValueError("--lookup-only requires --doi or --arxiv")
        issues = [] if args.lookup_only else validate(snapshot)
        result = {"records": len(list(records(snapshot, identity_only=args.lookup_only))),
                  "full_validation": not args.lookup_only, "issues": issues}
        if args.doi or args.arxiv:
            result["matches"] = [{"Paper ID": r["Paper ID"], "Title": r["Title"]} for r in lookup(snapshot, args.doi, args.arxiv)]
        print(json.dumps(result, ensure_ascii=True, indent=2))
        return 1 if issues else 0
    except (OSError, ValueError, KeyError) as error:
        print(json.dumps({"error": str(error)}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
