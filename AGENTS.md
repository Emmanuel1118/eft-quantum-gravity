# AI Agent Instructions

## Project

This repository contains computational and reproducible work for an M.Sc.
research project on effective-field-theory approaches to quantum gravity.

The VS Code workspace contains this repository and an Obsidian vault containing
conceptual research notes. Research papers and reference material remain in
Google Drive, accessed through folder/file URLs using the authenticated Google
Drive connection. The streamed Drive folder is not a VS Code workspace root.

These are separate sources of truth and should not be duplicated into this repository.

## Before substantial work

1. Read `context/current_state.md`.
2. Read `context/research_overview.md` when broader scientific context is needed.
3. Inspect relevant existing calculations before creating new ones.
4. Consult relevant notes in the Obsidian vault.
5. Use relevant source-grounded notes first. Open papers only for missing,
   uncertain, conflicting, or calculation-critical evidence; see the reading
   decision rules in `context/paper_workflow.md`.

Do not assume that chat history is authoritative if it conflicts with project files.

## Repository responsibilities

Use this repository for:

- reproducible calculations;
- Mathematica / Wolfram Language source;
- Python calculations and utilities;
- tests;
- scripts;
- research-state tracking;
- methodological decisions.

Do not copy the research-paper library or entire Obsidian vault into this repository.

## Mathematica

Prefer textual `.wl` source files for reproducible calculations.

Interactive `.nb` notebooks may be used when appropriate for exploration or
visualization, but important reusable calculations should eventually have a
textual source representation.

Place Wolfram Language calculations under:

`calculations/mathematica/`

Do not overwrite a working calculation merely to reorganize it.

## Python

Place scientific Python calculations under:

`calculations/python/`

Supporting utilities belong under:

`scripts/`

Tests belong under:

`tests/`

## Obsidian vault

The Obsidian vault contains conceptual scientific knowledge and research notes.

Agents may read relevant notes freely.

Agents may edit or create notes when explicitly required by the task.

Do not:

- delete notes;
- rename notes;
- move notes;
- reorganize folders;
- rewrite large groups of notes;

unless explicitly instructed.

Preserve Obsidian links and existing Markdown conventions.

## Research paper library

Treat the Google Drive research-paper directory as READ-ONLY by default.

Confine all project Drive interaction to `M.Sc. Research` and its descendants
(folder ID `1hinWMyTV1ld3FKfvzUeRijC_JUOBp7XU`). Do not read, search, list, edit,
or otherwise interact with other Drive folders or their contents. Scope searches
to known research-folder parents; do not run account-wide discovery. Follow
shortcuts only when their targets are established to be within this boundary.

Do not add/create, upload, copy, trash, or permanently delete Drive files or
folders unless the user specifically asks for that operation. Registering a
paper means adding a row to the existing index, not uploading a PDF or creating
a new spreadsheet. Routine index work must not create backup/copy files on Drive.

The existing Research Paper Index is an authorized writable exception. The user
approved ongoing maintenance on 2026-09-16. The temporary Google Drive app
Allow all actions setting was reverted to Use my default on 2026-09-19 at the
user's request. Respect enforced tool approvals. Standing index authorization
is not permission to operate outside the research folder or to create/delete
files. These project boundaries are behavioral instructions,
not technical restrictions on the connected account. Other source-file changes
still require explicit instructions.

**Do not ask for permission or confirmation for routine Research Paper Index
work.** The user reaffirmed standing authorization on 2026-09-19. During research,
proceed with index reads/searches, new-paper registration, supported record and
coverage updates, required native-table extension, and readback verification
through the authenticated connection. This authorization persists across
conversations; the user need not explicitly request each index update. Perform
the required live-data checks and then write, without an approval checkpoint
merely because the index is on Drive or the operation changes a spreadsheet.
Preserve human-owned fields and follow the catalog procedures below. Ask about
unresolved factual ambiguity only when needed, not to renew this authorization.
If an enforced tool/platform approval blocks an operation, identify that actual
block separately; do not present it as missing project authorization or bypass it.

Use the library URL in `context/local_environment.md` through the Google Drive
connection for discovery and reading. Do not depend on sandbox access to the
local `G:` mount. Including that mount as a workspace root caused Windows
sandbox initialization to fail; URL access has been verified separately.

Agents may:

- search it;
- read papers;
- identify relevant literature;
- cite papers in notes and research output.

Do not rename, move, delete, or reorganize papers unless explicitly instructed.

## Paper reading and catalog maintenance

Read relevant sections of `context/paper_workflow.md` for reading decisions,
selected-PDF retrieval, local extraction, and catalog updates. Load
`context/paper_registration.md` only when adding/discovering papers.
The canonical spreadsheet URL is in
`context/local_environment.md`. Use it rather than a locally maintained catalog.

- Consult the index when locating literature; register newly relevant papers
  during authorized research work, even if their PDF is not in Papers.
- For questions already supported by a known vault note, skip index and PDF
  reads. Read only relevant note sections; stop when the evidence is sufficient.
- Register new papers from available bibliographic metadata first. Deduplicate
  using a compact live identity projection, including candidates in the same
  batch. Do not read/download PDFs, summarize papers, inventory the library,
  or verify every optional field merely to add a record. Record unknowns.
- Reuse metadata within a task for read-only lookups. Use bounded reads and
  narrow write/readback batches; refresh live structure and affected cells
  before writes. Do not rerun acceptance checks or full audits routinely.
- Match DOI and base arXiv IDs before adding a row. Resolve the current row by
  stable Paper ID after any sorting, and flag conflicting matches.
- Read current cells and native table constraints before writing. Preserve
  human edits, extend the native table when adding rows, and verify readback.
- Change human familiarity only from the user's explicit assessment. Never
  infer familiarity from note existence, paper access, or an AI explanation.
- Keep summary coverage in the index and substantive summaries in Obsidian.
  A mention or citation is distinct from a paper summary.
- Distinguish referenced, summarized, and source-verified material. Keep source
  version, page/equation locators, assumptions, and unresolved gaps in notes.
  Update these incrementally during authorized research, not by pre-reading
  the library. Do not update verification dates merely for consulting a row.
- A failed or incomplete scan means unchecked/inaccessible, not absent.
  Availability currently refers to Papers and its descendants.
- Store selected PDF caches, extraction JSON/text, and temporary catalog
  snapshots under ignored `output/`. Do not store temporary download URLs or
  credentials in durable files. No background synchronization is configured.
- Reuse cached extraction and rendered pages for the recorded source version.
  Prefer compact search snippets; a partial-cache miss is not paper-wide absence.

## Research state

After substantial research work, update:

`context/current_state.md`

when the active understanding, open questions, or next step has changed.

Record durable methodological or organizational choices in:

`context/decisions.md`

Do not fill these files with session transcripts. Keep them concise and useful
to a future researcher or AI agent.

## Outputs

Generated temporary output belongs under:

`output/`

Do not treat generated output as authoritative when the calculation that
produced it is available.

## General working principle

Chats are for discussion.

Files are the durable source of truth.

If `context/local_environment.md` exists, read it to determine the
machine-specific locations of external research resources.
