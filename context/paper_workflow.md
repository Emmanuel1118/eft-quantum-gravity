# Paper reading and research index

Implemented 2026-09-16. Stage 5/5B operational checks and the final independent
conversation check passed, the latter on 2026-09-18. Evidence and the repeatable
acceptance prompt are in `context/stage5_acceptance.md`.

## Sources of truth

- Google Drive: source PDFs and the native Research Paper Index spreadsheet.
- Obsidian: conceptual notes, paper summaries, and their coverage.
- This repository: utilities, procedures, tests, and setup evidence.
- Ignored `output/`: disposable selected-PDF caches, extracted text, images,
  spreadsheet build files, and verification snapshots. Never edit a local
  snapshot as though it were the live catalog.

Canonical URLs and the vault location are in `local_environment.md`.
The two-root workspace and URL-based Drive route remain in use.

## Find and read a paper

1. Read the index metadata, then bounded ranges in the observed `Papers` tab.
   Locate by Paper ID, DOI, arXiv ID, title, or topic. Metadata contains the
   current sheet/table IDs; never assume row numbers persist after sorting.
2. For Drive inventory, list documents and folders within the known Papers
   folder using paginated `google_drive_search`. Recurse into every returned
   subfolder and follow all `next_page_token` values unchanged. A folder's
   first 100 children or an interrupted traversal is not a complete inventory.
   Inspect shortcuts or other source-file types if encountered.
3. For filename search, use a Drive query such as `name contains 'Donoghue 2023'`
   together with the observed parent ID and `trashed = false`. General text
   search can match citations inside other PDFs; it is not a filename filter.
4. Read source metadata to confirm its ID, MIME type, filename, and parent.
   Use connector `fetch` for readable text. For exact mathematics, retrieve the
   selected original PDF with `download_raw_file=true, include_base64=false`.
5. Materialize the returned authenticated `file_uri` into
   `output/paper_cache/<stable-id>-<version>.pdf`. If only its temporary download
   URL is exposed, download that exact URL; never substitute a guessed public
   Drive download endpoint. Do not persist the temporary URL. On this machine
   sandbox network restrictions required approved `Invoke-WebRequest` downloads;
   local extraction and rendering then ran without escalation. No Drive mount
   or local library mirror is required.
6. Extract/search locally and render the relevant original pages. Cite the
   canonical Drive URL/file ID, actual version, physical PDF page, and section
   or equation. Page numbers below are 1-based PDF indices, which can differ
   from printed page labels. Text extraction does not establish mathematical
   typography or OCR correctness.

From the repository root:

```powershell
powershell.exe -NoProfile -ExecutionPolicy RemoteSigned -File scripts/paper_text.ps1 output/paper_cache/donoghue-2211.09902v2.pdf --pages 9-11 --find 'non-analytic'
```

To save page-aware text, provenance, and rendered originals:

```powershell
powershell.exe -NoProfile -ExecutionPolicy RemoteSigned -File scripts/paper_text.ps1 output/paper_cache/donoghue-2211.09902v2.pdf --pages 10 --source-url 'https://drive.google.com/file/d/1kFK0ZZh3Y8tlOfahuLvFHfIhlc6ZdG96/view' --output output/paper_cache/donoghue-page10.txt --json-output output/paper_cache/donoghue-page10.json --render-dir output/paper_cache/donoghue-page10
```

Existing outputs are preserved by default. Use `--force` only for intentionally
replacing generated output; the source PDF cannot be an output path. Omit
`--pages` to extract all pages. `--find` normalizes case, whitespace, and ordinary
line-break hyphenation. It prints full matching pages, not a mathematical parse.
JSON records include the source SHA-256, page count, metadata, and per-page text.
Exit 0 means text was found; exit 1 means no match/extractable text; exit 2 means
invalid inputs or an operational error. Scans with no text need visual inspection
or a separately selected OCR workflow; OCR is not silently performed.

The PowerShell wrapper selects the installed Codex Python runtime, falling back
to `python` if unavailable. This avoids this machine's older Python 3.7 default.
Verified dependencies are pinned in `scripts/requirements-papers.txt`:
Python 3.12, pypdf 6.10.0, and pypdfium2 5.13.0. No packages were installed.
On another machine use a modern Python environment and these requirements.

## Catalog schema and meaning

The native spreadsheet has `Papers` and `Guide & Lists` tabs. The main table has
32 columns, with identity and working statuses first and detailed provenance
to the right. Its guide defines the fields and dropdown choices.

- Internal Paper IDs are persistent identifiers, not row numbers. Never reuse
  an ID after retiring a record. Prefer DOI, then base arXiv ID for matching;
  use title/authors/year as review evidence if neither identifier exists.
- Preprint and published versions normally share a record. Record the stored
  PDF version and relevant errata explicitly. Do not silently replace the
  cited version (e.g. the 2014 Blanchet review has later retitled revisions).
- Publication year is blank when not established from checked sources;
  preprint year remains separate. Publication metadata does not rename PDFs.
- `Drive status` refers to Papers and descendants. `Absent` is supported by a
  complete successful library inventory; it does not mean absent everywhere
  in the Google account. `Unchecked` and `Inaccessible` preserve uncertainty.
- `Summary status` distinguishes mention-only references, stubs, partial or
  substantial summaries, and unchecked records. Record actual coverage and
  vault-relative paths. Do not count a concept note as a whole-paper summary.
- The Obsidian URI is a local-app convenience; the relative path remains the
  fallback. Browser launch of that URI has not been tested in this session.
- `Your familiarity`, its reported date, and `Personal comment` are human-owned.
  Only explicit user reports change familiarity. Initial Donoghue assessment:
  `Read substantially`, supplied 2026-09-16. Other records: `Not assessed`.
- Initial priorities and relevance descriptions are agent judgments grounded
  in current research context; the human may revise them.
- Dates are numeric spreadsheet dates. The native DATE column currently uses
  its locale's M/d/yyyy display; do not confuse formatting with stored values.

## Maintain it during research

At discovery, inspect the live headers and identifier columns first. Deduplicate
before inserting. If an identifier resolves to multiple records, or DOI and
arXiv point to different records, pause the merge and flag the conflict. Never
overwrite a personal assessment while refreshing metadata.

For updates, re-read the target row and table constraints, map intended fields
to current columns, and write only those fields. Re-resolve the row after any
sort. Concurrent edits between read and write are still possible: keep edit
batches short, re-read just before writing, and verify afterward. This is not
a transactional background synchronization service.

For new rows, inspect the last complete row and the empty destination. Copy
formatting/validation only, write the complete new record, extend the native
table's range to cover it, and preserve its column types/options. Do not copy
another paper's links, comments, or familiarity. Check typed dates, table
coverage, dropdowns, and exact identifiers after readback.

After an authorized PDF addition or a note update, refresh the relevant
availability or coverage fields and verification date. Periodically repeat
the full Papers inventory and vault reference search. Never delete records
merely because a file disappeared or a link failed.

The read-only `scripts/paper_index.py` can validate a disposable live snapshot
and resolve normalized DOI/arXiv identifiers. Supply JSON with `headers` and
`rows` taken from the live sheet, not a stale build file. It flags duplicate
identifiers and impossible Present-without-file-ID records; it does not verify
the actual existence of remote files or decide whether two similar titles match.
It does not write to Drive. The connector performs authorized writes.

## Recovery and checks

Use Google Sheets version history for routine recovery. Before substantial
restructuring, export a dated XLSX snapshot to an agreed backup location.
Exports remain snapshots; the original spreadsheet ID stays authoritative.
Restore only after inspecting the relevant version and intended affected data.
No automatic export schedule or extra Drive backup folder was created.

Google Sheets-specific table display may change on XLSX export or local import.
In this runtime, the exported preview showed blue table banding and numeric-looking
arXiv IDs; the native API confirmed white body rows and exact text IDs, including
the leading zero in `0802.0716`. Use native values and table metadata to verify
data, and a browser when available to verify exact native appearance.

Run tests with the modern Python interpreter documented in `local_environment.md`:

```powershell
$paperPython = Join-Path $env:USERPROFILE '.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe'
& $paperPython -m unittest discover -s tests -p 'test_paper*.py' -v
```

See `stage5_acceptance.md` for evidence and the completed independent check.
