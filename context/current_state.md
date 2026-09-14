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
4. connect local Mathematica execution (direct kernel route now verified).

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

### Stage 4: sandbox execution works; final acceptance checks pending

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

The user confirmed the original smoke task passes from the VS Code menu.
Confirmation of both tasks after the runner change has been requested.
Next: finish those menu checks and the handout's fresh-conversation acceptance
test using the documented runner. Fresh kernels are verified in this conversation;
a genuinely new conversation has not yet been tested. Stages 5 onward have not
begun. Paths are in `context/local_environment.md`; diagnostic history is in
`output/wolfram-stage4-2026-09-14.md`.
