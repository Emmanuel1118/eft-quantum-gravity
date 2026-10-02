# Current Research State

_Last updated: 2026-10-02_

## Active investigation

For the next few days, investigate how treating higher-derivative gravity as
an EFT restricts its admissible solutions and initial data, and what explicit
UV matching contributes beyond bulk Wilson coefficients (user focus, 2026-09-18).

Active starting calculation: the healthy coordinate-coupled light/heavy
oscillator model. The vault's `03 Calculations/Oscillator Toy Model - UV Matching
and Runaway Solutions.md` now records goals, steps, and learning checkpoints.
The primary working artifact is `calculations/mathematica/oscillator_uv_matching.nb`,
following the user's notebook preference. Its UV Lagrangian, coupled equations,
energy, and potential-positivity checks passed in the local kernel. An independent
symbolic suitability check confirms stable UV modes and a spurious growing root
above the heavy scale in the first fourth-order derivative truncation.
Normal-mode/data matching and the evolution/error benchmark remain pending.
The researcher leads physical derivations and interpretation; AI assistance
focuses on readable Mathematica implementation. Next: derive exact normal modes,
then implement their low-energy initial-data map. Gravity follows this benchmark.

The vault note `04 Research Questions/Higher-Derivative Gravity - Literature
Review and Investigation Plan.md` contains the light review, prioritized
references, evidence limits, and a proposed three-day plan. Relevant prior work
includes Simon (1990), Burgess/Williams (2014), Glavan (2018), and direct
2024-2026 work on gravitational mode removal and initial-data reduction.
The general idea is established; novelty of a particular UV-matching extension
is not yet assessed.

Woodard reading is consolidated (2026-09-21) in the vault's
`02 Papers/Woodard 2015 — The Theorem of Ostrogradsky.md` and five linked
concept notes. Coverage distinguishes nondegeneracy/gauge constraints,
Hamiltonian state counting, energy unboundedness versus trajectory growth,
canonical quantization, and order reduction/initial-data branch selection.
Selected arXiv v2 equations were visually checked against the PDF; full
interacting and gravitational derivations remain. The apparent wording reversal
in Section 4.1 is flagged as an interpretation, not a confirmed erratum.
Burgess/Williams reading is consolidated (2026-09-30) in the vault's
`02 Papers/Burgess and Williams 2014 — Runaway Ghosts and Time-Dependent EFTs.md`,
three new concept notes, and an extension of the existing order-reduction note.
Coverage includes source/Legendre identities, the Goldstone model, locality and
the inverse-mass expansion, the fourth-order variation, and runaway/data selection.
Original arXiv v1 PDF pages 5–10 were visually checked; worked explanatory algebra
is distinguished from source statements. Finite-time state/Green-function matching,
full quantum contour treatment, and error bounds remain open.
The healthy light/heavy oscillator benchmark above has now started. Keep UV
state preparation explicit, and distinguish finite-order UV data matching from
exact projection onto the truncated equation's no-runaway subspace: omitted-order
data mismatch can seed its growing mode. Finite-order EFT accuracy is distinct
from exact all-orders convergence; the full matching/error benchmark and
gravitational branch classification remain pending.

The earlier one-loop Newtonian-potential investigation remains a background
thread, with Donoghue Eq. 20 as its reference point.

Bateman/Turok (2026), arXiv:2607.00096v1, is registered as P039 (High priority).
Selected main-text reading identifies a useful comparison for the ghost question:
Krein-space quantization and tree-level probability positivity in a fundamental
four-derivative scalar theory. This does not establish EFT initial-data matching
or generic gravitational branch admissibility; higher-order positivity remains
open and the gravity connection is a conformally flat limit. The planned
light/heavy benchmark remains the next calculation. A brief vault note,
`02 Papers/Bateman and Turok 2026 — Escape from Ostrogradsky via Hidden Ghost Parity.md`,
now records relevance, reading limits, and a staged follow-up; detailed
derivation checks remain pending.

## Current conceptual focus

For the new focus, distinguish spurious truncation modes, genuine retained
degrees of freedom, Ostrogradsky energy unboundedness, tachyonic growth, and
well-posedness. Keep cutoff/gradient control, initial-state preparation, and
field-redefinition consistency explicit.

The previous potential investigation includes:

- the relationship between scattering amplitudes and effective potentials;
- the origin of classical contributions from loop diagrams;
- the distinction between analytic and nonanalytic momentum dependence;
- triangle, bubble, box, and related one-loop topologies;
- Passarino-Veltman loop-integral notation;
- how the specific scattering process determines where classical and quantum
  pieces appear in perturbation theory.

## Computational status

Mathematica is being used for the calculation.

FeynCalc and FeynGrav are relevant computational tools.

Some loop-integral exploration has already been performed, including scalar
triangle integrals and Passarino-Veltman representations.

The new VS Code-centered environment is being established so calculations can
be edited, executed, version controlled, and connected directly to the
research notes.

## Previous potential thread: next physics direction

After the standard one-loop correction is understood sufficiently well,
investigate how additional terms allowed in the gravitational EFT Lagrangian
affect the correction to the potential.

In particular:

1. identify relevant higher-derivative / curvature operators;
2. determine how they modify vertices and propagators;
3. identify which one-loop amplitudes are affected;
4. isolate long-distance nonanalytic contributions;
5. determine whether they modify classical terms, quantum terms, or only
   short-distance/contact contributions.

## Background infrastructure task

Finish constructing the VS Code research environment.

Setup stages:

1. establish project context files (complete);
2. establish backup/version control for the Obsidian vault (complete);
3. Codex IDE agent setup complete; ordinary sandbox checks and Drive URL access verified;
4. connect local Mathematica execution (complete; fresh-conversation acceptance passed);
5. paper reading/search and 5B index (complete; fresh-conversation acceptance passed);
6. Obsidian editing and backup from VS Code (pending);
7. standard research workflow (pending);
8. end-to-end VS Code acceptance test (pending).

See [setup roadmap](setup_roadmap.md) for the remaining stages, acceptance
criteria, and optional tooling, incorporated from the supplied Stage 4+ plan.
Next setup step: Stage 6. Stage 5/5B fresh-conversation checks passed; see the
[acceptance record](stage5_acceptance.md).

Stage 3 status on 2026-09-13: the user removed the streamed Google Drive folder
from the VS Code workspace, leaving the research repository and Obsidian vault.
Ordinary IDE commands now run without escalation as `codexsandboxoffline`;
repository and Obsidian reads pass, and fresh setup logs report `errors=[]`.

Literature access now uses folder/file URLs through the authenticated Google
Drive connection. Folder navigation and readable text retrieval from the
Donoghue 2023 PDF passed. The library remains read-only by project policy and
separate from the repository. The local G: mount still denies sandbox access;
repairing that mount is no longer the chosen literature-access route.
See `context/local_environment.md` for URLs and `context/decisions.md` for rationale.

Stage 3 completion check at 20:18 local on 2026-09-13 passed through ordinary IDE
tools without escalation: sandbox identity, repository working directory,
repository and Obsidian reads, unique output-file creation and exact readback,
cleanup, and denial of unique file creation directly under `C:\Users\egreb`
outside the workspace (`System.UnauthorizedAccessException`). Both probe paths
were confirmed absent afterward. Fresh setup logs reported `errors=[]`.

Stage 3 is complete for the two-root local workspace plus authenticated Drive
URL access. This does not establish access to the local streamed G: mount or
constitute an exhaustive sandbox security audit.
Details: `output/windows-sandbox-repair-2026-09-13.md` (local output artifact).

### Stage 4: complete

The existing Wolfram 14.3, FeynCalc 10.2.0, and FeynGrav 4.0 installations work
under both the normal Windows account and the dedicated sandbox account.
Shared setup loads FeynCalc then FeynGrav with `Needs`; no desktop notebook is
required. Both VS Code tasks use `scripts/run_wolfram.ps1`.

On 2026-09-14 the direct route `wolfram.exe -noicon -noprompt -script` replaced
the unreliable WolframScript intermediary on this machine. It is selected by
ignored `context/wolfram.local.json`. Kernel user files
stay under `output/wolfram-userbase/`; ignored `local_config.wl` references the
existing package installation. The same `Needs` loading sequence is retained.

The current project runner passes without escalation under the dedicated
sandbox account: full FeynCalc/FeynGrav smoke test; temporary source evaluation
printing `4` with its source directory as working directory; explicit success;
nonzero exit propagation; abort detection; syntax/BOM rejection; and missing
completion detection. Temporary sources are removed by the runner regression
test, `tests/wolfram_runner_test.ps1`. Both task routes now require completion
evidence plus exit code zero; the smoke task also requires its final PASS marker.

The sandbox can read and use the same machine-wide Student license as the normal
account (`$NetworkLicense=False`). Redirecting WolframScript configuration removes
its configuration error but does not restore evaluation. The exact internal
cause of its startup failure remains unknown; direct execution avoids that
intermediary. No license copying, activation, ACL/firewall changes, sandbox
weakening, package reinstall, or cloud fallback was needed.

On 2026-09-15 both current `.vscode/tasks.json` commands were executed with their
resolved arguments and working directories through ordinary sandbox tools.
Smoke test: PASS (kernel, shared setup, FeynCalc, FeynGrav), exit 0. Run Current
File: a newly created temporary `.wl` printed `4`, verified the source-directory
working directory, and reported `CodexSandboxOffline`, exit 0. Its output was
inspected and the temporary source removed; absence was confirmed. No escalation
was needed. This verifies the task commands, not a new VS Code menu interaction;
the user previously confirmed the original smoke task through that menu.

The section 4.9 fresh-conversation acceptance test passed on 2026-09-15.
In a new conversation, the agent read `AGENTS.md`, this file,
`context/local_environment.md`, and `calculations/mathematica/setup.wl`, then
ran the documented smoke test through `scripts/run_wolfram.ps1`: all PASS
markers, exit 0. A newly created temporary `.wl` printed `4`, verified its
source-directory working directory using path components, and passed through
the same runner with exit 0. Both successful runs had completion markers and
empty stderr; output was inspected and temporary-source removal verified.
The probe's initial raw-string directory assertion failed and was corrected
before the successful rerun; no runner or setup changes were needed.
All commands used ordinary tools without escalation; `whoami` confirmed
`codexsandboxoffline` (the kernel's inherited `USERNAME` value was `egreb`).
Stage 4 is complete. Stage 5 implementation followed on 2026-09-16 below.

Paths are in `context/local_environment.md`; diagnostic history is in
`output/wolfram-stage4-2026-09-14.md`; latest results are in
`output/stage4-validation-2026-09-15.md`. Fresh-conversation evidence is in
`output/stage4-fresh-acceptance-2026-09-15.md`.

### Stage 5 and 5B: complete

On 2026-09-16 the authenticated Drive connection inventoried all eight PDFs in
Papers and its four subfolders. Filename search and readable text retrieval
passed. The selected Donoghue arXiv v2 PDF was retrieved into the ignored cache;
local extraction reads 26 pages and finds nonanalytic terms on pages 9-11.
Eq. 20 was visually verified on original page 10, Section 5.1.

`scripts/paper_text.ps1` runs the reusable PDF extraction/search/render utility
with the installed modern Python runtime. Eleven PDF/catalog tests passed.
No new packages were installed. Selected-file downloads needed network approval;
local processing did not.

The native Research Paper Index in Papers contains 18 records: eight stored
PDFs and ten external references. It holds bibliographic sources, versions,
Drive locations, Obsidian coverage, priorities and human familiarity. The user
reported Donoghue as `Read substantially`; other records remain `Not assessed`.
Five publication years remain unverified and blank. Native creation, readback,
dropdowns, live row addition, sorting, ID-based updates, human-field preservation
and duplicate checks passed. The connector already permits spreadsheet writes;
no new access scope or sharing change was needed. Index maintenance is authorized.

See [paper workflow](paper_workflow.md) and [acceptance record](stage5_acceptance.md).
URLs are in `local_environment.md`; generated evidence is under `output/stage5/`.
Both exported spreadsheet tabs were visually inspected; exact native chip
appearance remains unverified because CUA reported no browser.

Paper usage optimization is implemented (2026-09-18): start with relevant vault
sections, use targeted index reads, and open source pages only for evidence gaps
or exact source checks. New papers follow the metadata-first, batched procedure
in [paper registration](paper_registration.md); registration alone does not
require PDF reading, summarization, or a library inventory. `paper_text.ps1`
supports compact snippets/page lists and cache-only JSON search; `paper_index.py`
supports compact identity lookup and conflicting-identifier checks. Eighteen
paper utility tests pass. P001's note and live Summary coverage now distinguish
Eq. 20 from reference-only Eqs. 16/18; human fields are preserved. These changes
do not complete the pending Stage 6 backup/editing acceptance or Stages 7-8.

On 2026-09-18 a new conversation reconstructed context from project files and
passed the recorded acceptance check: authenticated index metadata and P001
readback, PDF filename search and readable text retrieval, local page-10
extraction and original-page visual verification of Eq. 20, and concept search
on pages 9-11. The linked Obsidian summary was read and confirmed. P001 was
resolved again by stable ID before updating only Last verified to 2026-09-18.
Full table readback showed that single cell change; familiarity, its reported
date, and the blank personal comment were preserved. The live snapshot validator
found 18 records, zero issues, and one match for the versioned arXiv identifier.
Source PDFs and vault notes were unchanged; Stages 6-8 remain pending.
