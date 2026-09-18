# Register new papers efficiently

Read this procedure only when adding/discovering papers. The canonical index
remains the live Google Sheet; see [paper workflow](paper_workflow.md) for
sources of truth and reading decisions.

1. **Collect identity from evidence already at hand.** Use title, authors,
   DOI/base arXiv ID, canonical external URL, and discovery/metadata source from
   the research task. If needed, obtain bibliographic metadata from an
   authoritative landing page. Do not download/read the paper, generate a
   summary, or chase optional metadata solely to create a row. Keep unverified
   years, venue, DOI, or version blank; distinguish preprint and publication year.
2. **Deduplicate before enrichment.** Read live headers and a bounded projection
   of Paper ID, Title, DOI, and arXiv ID once for the discovery batch. Normalize
   identifiers with `scripts/paper_index.py --lookup-only`; check all candidates
   against existing rows AND each other. Search known Drive IDs when applicable.
   A text row-search result alone may miss identifier spelling/URL variants.
   For larger tables, chunk the identity columns, not all 32 columns. Establish
   complete identity coverage before declaring no match. Without reliable IDs,
   compare title/authors/year among plausible matches; uncertain matches require
   review. If identifiers conflict, including a different nonempty identifier
   on the matched row, flag the conflict and do not merge or insert a duplicate.
3. **Reuse matches.** Resolve existing Paper IDs and update only newly supported
   fields if needed. No-op rediscovery needs no write. Preprint/publication
   versions normally share a record; preserve the cited/stored version.
4. **Prepare minimal new records.** Include unique Paper ID, title, available
   identity/source data, brief research relevance, discovery source, and Added
   date. Use current allowed status values: `Unchecked` for unexamined Drive or
   summary availability; `Not assessed` for familiarity unless the user gave an
   explicit assessment. Set `Present` only with verified file/location evidence;
   set `Absent` only with a complete successful inventory and its date. A quick
   unsuccessful search is insufficient. Search relevant vault titles/identifiers
   once for the batch if coverage is useful; record actual coverage/paths or
   leave it unchecked. Do not create empty summary notes for registration.
5. **Commit a short live batch.** Re-read current table bounds, column types,
   validations, live identity data, last complete row, and destination cells
   immediately before writing. Allocate unused IDs above the highest retained
   ID (never reuse retired IDs; retain their records). If structure/identities
   changed, reconcile first. Copy formatting/validation only; write new records
   with unknown fields blank, and extend the native table once for the batch.
   Preserve table options, exact text identifiers/leading zeros, typed dates,
   existing formulas and human fields. Do not sort as part of routine insertion.
6. **Verify and stop.** Read back new rows and table coverage/types/options;
   confirm IDs/identifiers and destination boundaries, not every existing cell.
   If a write times out or its outcome is uncertain, resolve candidate IDs and
   identifiers live before retrying so retries do not duplicate records.
   Enrich later when research supplies new evidence. Do not invent a test paper
   to exercise the live catalog.

The compact lookup input is JSON with `headers` and `rows` for just the four
identity columns, assembled from current connector reads under ignored `output/`:

```powershell
$paperPython = Join-Path $env:USERPROFILE '.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe'
& $paperPython scripts/paper_index.py output/live-identities.json --lookup-only --arxiv '2211.09902v2'
```

This mode reports matches/conflicts but does not perform a full catalog audit or
prove that the supplied projection covers all live records. Read completeness
and native writes remain the connector workflow's responsibility.
