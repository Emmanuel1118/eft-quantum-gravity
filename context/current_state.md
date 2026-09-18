# Current Research State

_Last updated: 2026-09-18_

## Active investigation

Understand the origin and structure of the one-loop corrections to the
Newtonian gravitational potential in effective quantum gravity.

The current reference point is Eq. 20 in Donoghue's treatment and the
calculation underlying it.

## Current conceptual focus

Important issues currently being investigated include:

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

## Next physics direction

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

## Immediate infrastructure task

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
