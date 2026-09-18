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

## Decide how much to read

Start with the question, not a fixed retrieval checklist. Search vault filenames
and headings with `rg`, then read the relevant sections. Follow useful links
selectively; a wikilink or bibliography entry does not establish summary coverage.

| Need | Minimum useful evidence | Escalate when |
| --- | --- | --- |
| Explain a covered concept or recall a documented result | Relevant concept/paper note | Coverage, assumptions, or provenance are inadequate |
| Locate literature or check catalog status | Relevant live index fields | Identity or location is uncertain |
| Register a new paper | Bibliographic identity and discovery source | Identifiers conflict or identity is ambiguous |
| Resolve a missing claim or derivation step | Located source passage and surrounding context | Dependencies require additional sections |
| Use an exact equation in a new calculation, quote, or resolve a discrepancy | Original page for the chosen version, preferably cached | Other pages or versions are needed |
| Comprehensive review or derivation | Task-appropriate broader reading | Continue until requested coverage is met |

Stop once evidence supports the requested answer. A partial summary can fully
answer a narrow question. A substantial summary is not proof of every claim.
For ordinary reminders, reuse previously source-verified results with their
provenance; do not claim a fresh source check. Separate source claims, advisor
roadmaps, our calculations, and unresolved questions.

## Find and read a selected paper

1. Skip the index when a known note already supplies sufficient evidence. When
   locating literature, read/reuse this task's live index metadata and headers,
   then search by Paper ID, DOI, arXiv ID, title, or topic. Retrieve only identity,
   source links, note paths, and coverage needed for the question. Use observed
   tab names and bounded ranges; never assume row numbers survive sorting.
2. Follow the recorded note path and check its actual relevant coverage. If
   source reading is needed, state the missing evidence briefly. Check existing
   selected-PDF caches, extraction JSON, and rendered pages before remote fetch.
   Reuse the recorded version; use source hashes to associate extraction with
   local PDFs. A local hash does not establish remote freshness. Check remote
   metadata/version when an updated source is requested, suspected, or material
   to the result; refresh only affected artifacts. Never silently change versions.
3. Use the recorded Drive file ID directly. Search filenames only for unresolved
   sources, using e.g. `name contains 'Donoghue 2023'`, an observed parent ID,
   and `trashed = false`. General text search may match citations in other PDFs.
   A search confined to one parent does not cover its descendants.
4. If no adequate cache exists, read/reuse source metadata to confirm ID, MIME
   type, filename, parent, and available version information. Choose readable
   connector text OR the original PDF according to the need; do not fetch both
   automatically. For mathematics/local extraction, retrieve the selected PDF
   with `download_raw_file=true, include_base64=false`.
5. Materialize the returned authenticated `file_uri` into
   `output/paper_cache/<stable-id>-<version>.pdf`. If only its temporary download
   URL is exposed, download that exact URL; never substitute a guessed public
   Drive download endpoint. Do not persist the temporary URL. On this machine
   sandbox network restrictions required approved `Invoke-WebRequest` downloads;
   local extraction and rendering then ran without escalation. No Drive mount
   or local library mirror is required.
6. Search cached extraction first; extract missing pages and render only relevant
   originals as needed. Reuse existing images of the same source. Cite the
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
line-break hyphenation. By default it displays a normalized snippet around the
first match on each of up to five matching pages, not a mathematical parse or
verbatim quotation. `--format pages` returns page numbers; `--format full`
returns full matching pages. `--max-matches N` bounds displayed matching pages
and `--context-chars N` controls snippet context. Without `--find`, selected
text is returned in full. JSON always preserves all selected page texts,
independently of display limits; avoid loading the whole JSON into conversation.
JSON records include the source SHA-256, page count, metadata, and per-page text.
Exit 0 means text was found; exit 1 means no match/extractable text; exit 2 means
invalid inputs or an operational error. Scans with no text need visual inspection
or a separately selected OCR workflow; OCR is not silently performed.

Search an existing extraction without reopening/downloading the PDF:

```powershell
powershell.exe -NoProfile -ExecutionPolicy RemoteSigned -File scripts/paper_text.ps1 output/stage5/donoghue-extraction.json --from-json --find 'nonanalytic' --max-matches 3
```

Cache search reports covered physical pages; a miss applies only to that
coverage and that search phrase. Explicitly requested uncached pages are an
error, not a negative result. `--verify-pdf <path>` additionally compares the
cached SHA-256 against local PDF bytes without extracting again. Cache search
retains source provenance and cannot render pages or override the source URL.
Use the PDF route to render or extend coverage. Cache loss is recoverable through
selected-file retrieval; no full-library mirror or background sync is needed.

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

### Read and update economically

Read metadata once per read-only task and reuse it until structure changes or
a range fails. Request only needed columns and matching records. Do not load the
whole table, Guide & Lists tab, or source PDFs for routine lookups. An in-session
projection is disposable; re-read affected live data before edits. No second
maintained local catalog is introduced.

For updates, re-read the target row and table constraints, map intended fields
to current columns, and write only those fields. Re-resolve the row after any
sort. Concurrent edits between read and write are still possible: keep edit
batches short, re-read just before writing, and verify afterward. This is not
a transactional background synchronization service.

Group related edits into a short coherent batch, then read back changed cells,
Paper IDs, and any relevant preserved fields. Do not reread the entire catalog
for a one-row update. Do not write unchanged values or update `Last verified`
merely because a record was consulted. When updating verification dates, state
the scope in the relevant coverage/provenance field: it does not imply that every
field or the entire paper was verified. Familiarity remains human-owned.

### New paper registration

Use the metadata-first, deduplicate-before-enrichment procedure in
[paper registration](paper_registration.md) only when adding/discovering papers.
It covers compact identity reads, batch deduplication, unknown-field defaults,
native table insertion, targeted verification, and safe retries.

### Reusable Obsidian coverage

Add/update a compact block in paper notes as useful research warrants:

- Identity: Paper ID, DOI/arXiv ID, exact source version and canonical link.
- Covered: claims/topics actually summarized, with section/page/equation locators.
- Referenced only: pointers without an explanation or transcription.
- Verified: exact material checked, source version, method and date/evidence.
- Assumptions/conventions: those established from the source; mark unknowns.
- Gaps: unresolved questions and sections not yet covered.

Keep substantive explanations in notes and short coverage descriptions in the
index. Distinguish quotations/transcriptions, source summaries, our inference,
advisor guidance, and independent calculation checks. Reuse shared concept notes
through links rather than repeating them in every summary. After authorized
reading, save useful supported results incrementally and update only affected
index coverage. Do not pre-read the library or rewrite groups of existing notes.

### Audits are separate from ordinary research

Run full inventory/whole-index validation for an explicit audit, a structural
change, a completeness-sensitive question, or evidence of catalog inconsistency.
Run infrastructure acceptance checks after relevant changes or suspected failures,
not at every conversation start. Full inventory uses paginated Drive searches
within Papers, recurses every returned subfolder, follows all next-page tokens,
and examines shortcuts/source-file types as needed. An interrupted traversal is
incomplete. An older absence is a dated observation; inaccessible is not absent.
Never delete records merely because a file disappears or a link fails.

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
