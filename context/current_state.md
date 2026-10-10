# Current Research State

_Last updated: 2026-10-10_

## Active investigation

For the next few days, investigate how treating higher-derivative gravity as
an EFT restricts its admissible solutions and initial data, and what explicit
UV matching contributes beyond bulk Wilson coefficients (user focus, 2026-09-18).

Active starting calculation: the healthy coordinate-coupled light/heavy
oscillator model. The vault's `03 Calculations/Oscillator Toy Model - UV Matching
and Runaway Solutions.md` now records goals, steps, and learning checkpoints.
The primary working artifact is `calculations/mathematica/oscillator_uv_matching.nb`,
following the user's notebook preference. Its completed calculation covers UV
modes/data, heavy response, derivative truncation, matching/order reduction, and
evolution/error comparisons; fresh-kernel verification is recorded below.
The vault note records steps 1–7. Step 3 retains heavy initial data in the retarded
response and records exact local elimination with its UV data map. Step 4 separates
exponential roots, failure of the derivative hierarchy, and the unbounded canonical
Hamiltonian. Step 5 records order reduction, the prescription comparison, and the
fast-amplitude formula: finite-order UV matching differs from exact oscillatory
projection, while both projected and reduced frequencies agree with UV through
$M^{-6}$. Step 6 includes six figures and practical implications for each
prescription. At $\omega=1,M=10,g=3,q_0=1,v_0=0$, projection and reduction have
maximum sampled amplitude-normalized errors of $3.48\times10^{-6}$ and
$1.14\times10^{-4}$ over $0\le t\le100$, with phase drift and $O(M^{-8})$
frequency errors. Generic, finite-order-matched, and exact-UV additional data
all excite growth under unreduced fourth-order evolution. The acceleration
mismatch scan demonstrates logarithmic gains in threshold time; the short
precision/tolerance scan controls solver error but does not establish long-time
stability. The Ostrogradsky concept note explains why exact UV elimination
inherits a positive energy and a different Hamiltonian structure. Step 7
interprets UV state information and consistent data/evolution selection,
compares the method and conclusions with Burgess–Williams v1 §§1–3, and states
the interaction, time-dependent, quantum, and gravity limits. This is an explicit
benchmark of their perturbative argument, not a new general ghost-removal
theorem. Next: review the interpretation and choose an extension; the proposed
first test is a weak, slowly switched drive with heavy-state and source matching.
The researcher leads interpretation; AI assistance focuses on readable Mathematica
implementation. Record each step only when requested; steps 6–7 were summarized
directly at the user's request. Gravity follows this benchmark.

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
from exact all-orders convergence. The matching/error benchmark and its
interpretation are documented through step 7. Extensions and gravitational
branch classification remain pending.

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

P024, Lü/Perkins/Pope/Stelle (2015), arXiv:1502.01028v2, now has a
substantial paper note in the vault, plus Numerical Shooting and Black Hole
Solution Branches and Black Hole Thermodynamics in Higher-Derivative Gravity.
All four original PDF pages, Eqs. (1)-(11), horizon coefficients, entropy
formula and Figs. 1-3 were read and visually checked on 2026-10-10. Coverage
includes Ricci-flat Schwarzschild/Kerr persistence, the static R=0 identity,
the failure of the Ricci-tensor positivity argument, horizon-series shooting,
the additional/negative-mass branch and Wald thermodynamics. Proposed uses are
high-precision branch continuation and independent first-law checks between
horizon and asymptotic data, followed by an EFT curvature/gradient audit.
Radial boundary-data tuning is distinct from temporal initial-data matching;
static existence, energy boundedness and dynamical stability remain separate.
The researcher reported skimming the full paper. No black-hole integration,
Eq. (4) derivation or thermodynamic fit has been independently reproduced.
This gravity benchmark does not replace the active oscillator extension.
Supporting entropy references are registered as P041 (Wald 1993, abstract/
mention only), P042 (Iyer--Wald 1994, selected HTML equations), and P043
(Fan--Lü 2015 v3, selected PDF introduction). Their full derivations remain
unread; the index records these limits separately from P024's coverage.

The vault's `01 Concepts/Quadratic Gravity - Renormalizability and Power
Counting.md` now records the requested theoretical discussion, centered on the
Feynman-diagram derivation of the loop-independent four-derivative bound. It
covers internal ghosts, subdivergences, gauge symmetry, counterterms, the
Einstein comparison, and exact versus EFT propagators. The separate
`01 Concepts/Higher-Derivative Gravity.md` is the overview for quadratic gravity,
extra modes, EFT branches and related research questions. Both link to existing
notes and distinguish explanatory algebra from source results.

P040, Stelle (1977), is readable from Papers/Theory; its live index now records
Partial summary coverage in these concept notes. Selected original PDF pages
2, 4, 7-8, 10-12 and 16 were checked for the action/spectrum, gauge fixing,
power counting, invariant counterterms and propagator. The full BRST proof,
explicit divergent loops, beta functions and contour analysis remain open.
Continue at the researcher's pace. Selected source caches remain under ignored
`output/paper_cache/stelle-1977*`.

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

Notebook evaluation repair (2026-10-05): the completed oscillator notebook's
35 generated input cells were rebuilt using native parsed boxes, with their
leading explanations retained as Text cells and saved evaluation labels removed.
All 49 input cells and 38 calculation checks pass in a fresh command-line kernel;
stored output boxes are unchanged. Interactive front-end evaluation remains to
be confirmed: the desktop connection was unavailable and an isolated hidden
front-end test did not complete. The pre-repair notebook and verification
record are under ignored `output/oscillator_meeting/`. This troubleshooting does
not update the scientific roadmap or replace the researcher's interpretation.

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
