# Research Decisions

This file records durable methodological, computational, and organizational
decisions whose rationale may otherwise be forgotten.

Do not record routine actions or temporary experiments.

---

## 2026-09-13 — Use a VS Code-centered research environment

### Decision

Use VS Code as the main operational research workspace.

Maintain separate sources of truth for:

- reproducible work in Git;
- conceptual notes in Obsidian;
- literature in Google Drive.

### Reason

The research workflow should not depend on the state or memory of a particular
AI chat application.

AI agents should be able to reconstruct the current project state from files.

---

## 2026-09-13 — Prefer textual Wolfram Language source for durable calculations

### Decision

Prefer `.wl` files for important reproducible Mathematica calculations while
retaining `.nb` notebooks where interactive exploration or visualization is
useful.

### Reason

Textual source files are easier to:

- version control;
- diff;
- edit with AI tools;
- execute automatically;
- review for reproducibility.

---

## 2026-09-13 — Access literature through Google Drive URLs

### Decision

Keep only the research repository and Obsidian vault in the VS Code workspace.
Access the separate literature library through folder/file URLs using the
authenticated Google Drive connection. Treat the library as read-only by
project policy. Store its access URLs in `context/local_environment.md`.

### Reason

With the streamed Drive folder in the workspace, the IDE passed it as a writable
sandbox root. Applying permissions failed with `SetNamedSecurityInfoW` error 87
and prevented ordinary commands from starting. Selecting the `research` profile
alone did not resolve that behavior. Removing the folder restored ordinary
sandbox execution and local repository/Obsidian reads.

The dedicated sandbox account still cannot read the streamed G: mount. URL-based
access through the authenticated connection successfully listed the library and
read text from a research PDF on 2026-09-13. This provides a working literature
route without Drive ACL changes, reduced sandbox isolation, or a duplicate paper
library. It depends on the authenticated connection and does not establish local
filesystem access. Sandbox write-boundary verification is a separate check;
the ordinary-tool completion results are recorded in `context/current_state.md`.

---

## 2026-09-14 - Use a shared local Wolfram setup and explicit smoke-test evidence

Use `wolframscript -local -file` through portable Windows VS Code tasks.
Load FeynCalc and FeynGrav in `calculations/mathematica/setup.wl`; keep
calculation-specific assumptions and gauge choices in individual sources.
Optional machine-specific package paths belong in ignored `local_config.wl`.

Require both exit code zero and the explicit final PASS marker for the smoke
task. The installed launcher can return zero without executing source in the
Windows sandbox. A successful run under the licensed user account does not
establish sandbox acceptance. Resolve that distinction without cloud fallback
or relaxing the sandbox. Tasks use process-scoped PowerShell `RemoteSigned`
to run local scripts without changing persistent execution policy.

### Follow-up: use the direct local kernel on this Windows machine

Select the documented `wolfram.exe -noicon -noprompt -script` interface through
ignored `context/wolfram.local.json`. This supersedes the earlier WolframScript-only
choice here: direct execution passes in the existing sandbox with the same
machine-wide license, while WolframScript still fails after configuration
redirection. Its exact internal failure cause was not established.

Keep kernel user files under `output/` and reference existing packages from
ignored `local_config.wl`. No license changes or broader sandbox access are
needed. Retain the portable WolframScript default when local JSON is absent.
Require completion evidence for all runs and propagate native nonzero exits;
the bootstrap reserves `$Epilog` for completion detection. Regression checks
exercise fresh-kernel evaluation and failure handling.

---

## 2026-09-16 - Use a native Drive spreadsheet as the literature catalog

Maintain Research Paper Index in the existing Papers folder through the
authenticated Google Drive connection. Include known relevant external papers
as well as stored PDFs. The Sheet is authoritative; extraction/build snapshots
under `output/` are disposable. Obsidian remains authoritative for summaries.

Use stable Paper IDs, normalized DOI/arXiv matching, source/version provenance,
and distinct availability/summary/familiarity fields. Update human familiarity
only from explicit reports. Preserve manual edits with narrow read-before-write
updates and ID resolution after sorting. Extend native table metadata on inserts.

Index maintenance has standing user authorization. No connector scope narrowing
is required, and existing write access worked. The user prefers broader future
paper-library access; this setup does not request reorganization of source files.
Maintenance is session-driven; background sync and scheduled backups are optional.

Use pypdf for selected-PDF extraction and pypdfium2 for page rendering through
`scripts/paper_text.ps1`, which chooses the existing modern Python runtime.
Record physical page numbers, source hash and canonical URL; check mathematics
against rendered originals. Preserve the two-root workspace and authenticated
URL-based retrieval. Selected downloads may need sandbox network approval.

Keep the fresh-conversation acceptance gate explicit. Current-session tool
readbacks and new Python processes do not establish an independent conversation.

---

## 2026-09-18 - Read notes first and register papers from metadata

Use the minimum evidence needed for each question: relevant Obsidian sections,
targeted index fields, cached extraction, then selected original pages when
coverage is missing, uncertain, conflicting, or calculation-critical. Track
referenced, summarized, and source-verified material separately with version,
locators, assumptions and gaps. Reuse existing verification honestly; do not
describe note consultation as fresh source verification.

Register newly relevant papers from available metadata without mandatory PDF
reading, summary creation, optional-field enrichment, or full inventory. Use
compact live identity projections, normalized DOI/base arXiv matching, and
within-batch deduplication. Preserve unknowns, human-owned fields, native table
constraints, and stable IDs. Refresh live prerequisites immediately before
short writes and verify affected rows; reconcile uncertain writes before retry.

Keep the live Sheet authoritative, Obsidian substantive, and caches disposable.
Default text searches to bounded snippets; cached searches report page coverage
and retain provenance. Inventory, full audits, and acceptance checks are triggered
by their specific need rather than routine research. Load the registration
procedure only for discovery/addition tasks. No background synchronization or
second maintained catalog is introduced.

---

## 2026-09-19 - Perform routine index maintenance without renewed permission

The user explicitly reaffirmed that interaction with the Research Paper Index
is required research workflow and must not trigger repeated permission requests.
Standing authorization covers reads/searches, registration, supported record and
coverage updates, necessary native-table extension, and verification readbacks
across conversations. Proceed after the existing live-data checks; do not add a
user approval checkpoint for a Drive spreadsheet write. Preserve human fields
and the separate source-paper policy. Distinguish any actual enforced tool or
platform approval from project authorization; this instruction does not bypass
enforced controls.

The user subsequently authorized Google Drive's app-specific Allow all actions
setting for the secondary AI-project account, with explicit project boundaries:
interact only with M.Sc. Research and descendants, and do not add/create, upload,
copy, or delete Drive files/folders unless specifically asked. Adding/updating
index rows and extending its native table remain routine workflow. The app-wide
approval setting does not technically enforce these folder/task boundaries;
AGENTS.md and the paper workflow carry them as persistent agent instructions.

The user then requested reverting the Drive permission change. Restored the
app override to inherit (Use my default; Allow low-risk actions). Research-folder
and file-creation/deletion boundaries remain. Local user-config auto-approval
overrides for spreadsheet cell reads and batch updates remain: the filesystem
approval request to remove those two overrides was declined. Do not describe
this as removal of all local approval exceptions.

---

## 2026-10-02 - Start the oscillator benchmark in a readable Mathematica notebook

Use `calculations/mathematica/oscillator_uv_matching.nb` as the primary working
artifact for this miniproject, as explicitly requested by the user. Keep short
input cells, visible intermediate results, descriptive symbols, and explanatory
text. Add textual `.wl` representations when reusable pieces mature; avoid two
independently edited implementations during exploration. Built-in Wolfram
Language functions suffice for the mechanical model.

Keep the conceptual roadmap and learning checkpoints in the vault's
`03 Calculations/Oscillator Toy Model - UV Matching and Runaway Solutions.md`.
The researcher leads physical reasoning; AI assistance focuses on Mathematica
implementation, debugging, and checks. Use the previously proposed healthy
coordinate-coupled oscillators. Specify the low-energy state separately from the
UV action, and distinguish finite-order data matching, exact projection for a
given truncation, and order reduction. Track trajectory growth separately from
Ostrogradsky energy unboundedness and assess errors over stated time intervals.

---

## 2026-10-05 - Generate notebook input using native parsed boxes

For generated notebook cells, parse source under `HoldComplete` and format it
with `MakeBoxes`; do not construct executable multiline cells from flat regex
token lists. Keep leading prose explanations in Text cells, preserve top-level
statement breaks, and let interactive evaluation generate its own cell labels.
Validate the saved notebook in a fresh kernel and distinguish that check from
interactive front-end verification. The oscillator repair preserves existing
outputs and passes 49 inputs and 38 calculation checks; front-end confirmation
is still pending.

---

## 2026-10-06 - Keep final oscillator figures beside the vault calculation note

Retain the six final Mathematica figure exports in the vault's
`03 Calculations/figures/oscillator_uv_matching/` and embed them in the
toy-model note using Obsidian links, with captions stating parameters, time
intervals, and the quantity plotted. Keep temporary exports and numerical
tables in ignored repository `output/`; the notebook remains the calculation
source. Distinguish trajectory approximation errors, isolated growing-mode
contributions, and numerical integration errors in both captions and analysis.

---

## 2026-10-09 - Report access problems and complete required source reading

The user requires explicit disclosure whenever a needed source is inaccessible.
Access failure does not justify omitting required reading or presenting an
abstract, general knowledge, or another source as a reading of that paper.
State the actual access/read status, work with the user to obtain readable access,
and complete the required reading once available. Existing note-first rules and
explicit user instructions still determine reading scope; platform controls and
the research-folder boundary remain in force.

Stelle (1977), DOI `10.1103/PhysRevD.16.953`, is P040. The user supplied its PDF in
Papers/Theory; authenticated Drive text retrieval now succeeds through the
appendix and references. Prose was sampled beyond the abstract; full proof
analysis and visual checks of exact equations remain for the theoretical
discussion. The live index records its location and access verification.

---

## 2026-10-09 - Separate the gravity overview from the renormalizability derivation

At the user's request, use the vault's `01 Concepts/Higher-Derivative Gravity.md`
as the connection point for quadratic gravity and related higher-derivative
questions. Keep the detailed Feynman-diagram power count in the separate linked
`01 Concepts/Quadratic Gravity - Renormalizability and Power Counting.md`.
Extend these notes as the concepts develop; preserve source locators and
coverage limits, and keep the live index's paper coverage distinct from the
researcher's familiarity. This creates two concept notes without reorganizing
existing vault material.
