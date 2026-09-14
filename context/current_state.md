# Current Research State

_Last updated: 2026-09-14_

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

1. establish project context files;
2. establish backup/version control for the Obsidian vault;
3. Codex IDE agent setup complete; ordinary sandbox checks and Drive URL access verified;
4. connect Mathematica execution through `wolframscript`.

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

### Stage 4: implemented; sandbox acceptance still blocked

The existing local Wolfram 14.3 installation, FeynCalc 10.2.0, and FeynGrav 4.0
were verified on 2026-09-14 under the licensed Windows user account. Both
packages are on its default `$Path`; `Needs["FeynCalc`"]` followed by
`Needs["FeynGrav`"]` works without custom paths or a desktop notebook.

Added shared `calculations/mathematica/setup.wl`, a package smoke test, and
the VS Code tasks `Wolfram: Smoke Test` and `Wolfram: Run Current File`.
Both task commands passed through the local kernel with escalation. The
current-file probe printed `4` with its source directory as the working
directory and was removed. VS Code menu invocation itself was not tested.

Ordinary sandbox execution is not reliable: automatic kernel discovery reports
failure opening the WolframScript configuration and can exit zero without
executing the source. Explicitly selecting `WolframKernel.exe` reports a license
error. The smoke-task runner requires its final PASS marker as well as exit
code zero. Earlier isolated `2+2` success did not reproduce reliably.

Next step remains Stage 4: establish supported local licensing/launcher access
for the sandbox account without weakening isolation, then rerun both tasks and
the fresh-conversation acceptance test without escalation. No package reinstall,
license-file copy, permission-policy change, or cloud fallback was performed.
Stages 5 onward have not begun. Machine paths are in `context/local_environment.md`;
details are in `output/wolfram-stage4-2026-09-14.md`.
