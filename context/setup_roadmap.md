# VS Code research setup roadmap

_Documented: 2026-09-16_

Adapted from the user-supplied
`VSCode_Only_Research_Setup_Stage4_and_Beyond.md`. This records the plan;
it does not authorize or report execution of its stages. Current completion
evidence lives in [current_state.md](current_state.md).

## Completed foundation: Stages 1–4

Project context, the separate Obsidian Git backup, Codex IDE setup, and local
Mathematica integration are complete. Stage 4 includes fresh-kernel FeynCalc
and FeynGrav loading, shared textual setup, portable VS Code tasks, and the
fresh-conversation acceptance test.

Two assumptions in the supplied plan have been superseded by recorded decisions:

- The workspace has two roots: the research repository and Obsidian vault.
  Access the paper library through authenticated Google Drive URLs
  in `local_environment.md`; do not restore the streamed Drive workspace root
  or depend on local `G:` access.
- This machine uses the verified direct local Wolfram kernel through
  `scripts/run_wolfram.ps1`. Do not restart Stage 4 or replace that working
  route with the plan's original WolframScript-only approach. No cloud fallback.

See [decisions.md](decisions.md) for the rationale.

## Stage 5 — Paper reading and search from VS Code

Status: implemented on 2026-09-16; current-conversation checks passed.
Final fresh-conversation check pending. See [acceptance record](stage5_acceptance.md)
and [paper workflow](paper_workflow.md) for evidence and commands.

- In a fresh session, verify library listing, PDF filename search, and basic
  metadata access through the authenticated Drive connection.
- Find likely sources, extract/search text from a selected PDF, and identify
  the exact PDF used by filename and Drive URL/file ID, with page or section
  when feasible.
- The supplied plan requires a local PDF extraction utility under `scripts/`,
  accepting a PDF path and printing text or writing to `output/paper_cache/`.
  Prefer a maintained Python PDF library or an installed extractor. When
  implementing this step, reconcile selected-file retrieval through the Drive
  connection with local extraction; the inaccessible streamed mount is not a
  prerequisite. Connector text retrieval alone does not establish completion
  of this local-extraction requirement.
- Keep generated text/cache disposable and ignored. Do not commit full paper
  text, write generated files beside Drive sources, or mirror the library.
- Keep extraction provenance in ignored per-source JSON. Stage 5B owns the
  authoritative catalog; do not maintain a second local bibliography.
- Verify exact mathematics against original PDF pages: text extraction can
  mishandle equations, columns, figures, and scans.

Acceptance: find one existing relevant PDF, identify a chosen section, search
for a specific concept, and report the exact source and page/section where
feasible, without modifying source PDFs. A paper must be meaningfully inspectable
without leaving VS Code, including the planned local extraction capability.

## Stage 5B — Research Paper Index

Status: implemented on 2026-09-16; current-conversation checks passed.
Final fresh-conversation reopen-and-update check pending.

- Maintain the native Research Paper Index in Papers through the existing
  authenticated Drive connection. This is an authorized writable artifact.
- Index stored PDFs and known relevant external works with stable IDs, title,
  authors, DOI/arXiv, separate publication/preprint years, versions and sources.
- Record Drive location, Obsidian summary status and coverage, priorities,
  next actions and explicitly reported human familiarity.
- Deduplicate by identifiers, distinguish missing from unchecked, preserve
  human edits, and re-resolve rows by ID after sorting. Extend the native table
  and preserve types/dropdowns when adding records.
- Use session-driven maintenance and version-history recovery. No background
  synchronization or duplicate local catalog is required.

Evidence: 18 records (8 stored, 10 external); source/note links; user-supplied
familiarity; live row addition; sorted ID-based update preserving another field;
duplicate checks; native metadata/value verification and exported visual review.
Exact native chip visuals await a browser-equipped session. Run the prompt in
[stage5_acceptance.md](stage5_acceptance.md) before marking Stage 5/5B fully complete.

## Stage 6 — Obsidian editing and backup from VS Code

Status: pending; the vault already exists as a separate Git repository.

- Verify note search, linked Markdown reading, and explicitly requested note
  edits/creation while preserving Obsidian links and Markdown conventions.
- After the controlled edit, update the index record's summary coverage and
  verification date while preserving human familiarity.
- Retain the existing restrictions on deletion, moving, renaming, and mass
  reorganization.
- Verify that VS Code Source Control shows the research and vault repositories
  separately and supports reviewing, committing, and pushing each.
- Establish reviewed session backups: calculations, scripts, tests, and context
  in the research repository; new and changed notes in the vault repository.
  Keep their histories separate. Automatic backup can be considered later.

Acceptance: an authorized, controlled note edit can be reviewed, committed,
and pushed without leaving VS Code.

## Stage 7 — Standard research workflow

Status: pending.

At session start, read `AGENTS.md`, `context/current_state.md`, and
`context/local_environment.md`; consult the overview and decisions when relevant.
Inspect relevant calculations, notes, and papers before substantial work.

Keep reproducible calculations in `calculations/`, utilities in `scripts/`,
tests in `tests/`, conceptual understanding in Obsidian, active status in
`context/current_state.md`, durable decisions in `context/decisions.md`, and
source literature in Drive. Avoid duplicate summaries.

Consult and maintain the Research Paper Index using `paper_workflow.md` after
new literature discoveries, authorized source/note changes and human reports.

At session close, distinguish established results from open questions, update
the appropriate notes and state when needed, record only durable decisions,
run relevant checks, show diffs, and suggest commit boundaries/messages.
Report scientific conclusions, unresolved questions, and changes in each repo.

Outcome: a documented, repeatable session-start and session-end workflow used
for the Stage 8 acceptance task.

## Stage 8 — End-to-end VS Code acceptance test

Status: pending.

Choose a narrow continuation of the existing one-loop/Newtonian-potential work,
not a major new calculation. Complete the following within VS Code:

1. Read current project state and consult an Obsidian note.
2. Find a relevant Drive paper and extract/search its PDF text.
   Locate it through the index and verify source/note references.
3. Inspect or modify a small `.wl` calculation.
4. Run local Mathematica and inspect the result.
5. Update the appropriate note and project state when needed.
   Refresh the corresponding paper-index fields when applicable.
6. Review the changes in VS Code Source Control for the Git review/commit loop.

Acceptance: demonstrate the complete question → context → notes and papers →
calculation → local Mathematica → result → note/state update → Git review/commit
workflow without manual transfer between a separate chat and the environment.

## Completion and optional tooling

Complete Stages 5–8 in order. After an implemented stage, update current state
with evidence and record any durable decisions. The source plan calls for
committing relevant stage changes; this documentation update does not execute
that workflow.

Required for migration completion: the completed local Wolfram/package/tasks
setup, PDF read/search and local extraction, controlled note editing, management
of both Git repositories in VS Code, the standard session workflow, and the
end-to-end acceptance test.

Optional; add only for a concrete need: Zotero, additional MCP servers,
automatic Obsidian commits, a Wolfram editor extension, LaTeX tooling,
GitHub Actions, WSL, containers, cloud compute, and whole-library vector/RAG
ingestion. These should not delay migration completion.
