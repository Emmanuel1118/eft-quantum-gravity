# Local Wolfram execution

Use the installed local Mathematica kernel through the project runner.
In VS Code, choose **Terminal > Run Task > Wolfram: Smoke Test**.
For a saved `.wl` file, choose **Wolfram: Run Current File**; its working
directory is the source file's directory. These Windows tasks use PowerShell
and contain no personal executable paths.

Equivalent smoke-test command from the repository root:

```powershell
powershell.exe -NoProfile -ExecutionPolicy RemoteSigned -File scripts/run_wolfram.ps1 -FilePath tests/mathematica_smoke_test.wl -RequireSmokePass
```

The task selects `RemoteSigned` only for its PowerShell process so locally
created scripts can run; it does not change the system execution policy or
Codex sandbox permissions.

On this machine the ignored `context/wolfram.local.json` supplies `kernelPath`
for the existing `wolfram.exe`. The runner uses `-noicon -noprompt -script`.
This direct route passed under the dedicated sandbox account with the existing
machine-wide license. Without that JSON file the portable default remains
`wolframscript -local -file`; it is still unreliable inside this machine's sandbox.

Kernel user files go under ignored `output/wolfram-userbase/`. Package paths
come from ignored `local_config.wl`; packages stay in their existing installation.
The WolframScript route uses `output/WolframScript.conf`. No persistent environment
variables, license files, or sandbox permissions are changed by the runner.

Both routes execute `scripts/wolfram_run.wl`, which checks source syntax and
installs an `$Epilog` completion marker. All runs require that marker and exit
code zero; smoke runs also require `PASS: MATHEMATICA_SMOKE_TEST`. Signal failed
calculations with `Exit[1]` or `$Failed`; ordinary warning messages alone do not
make a run fail. Do not replace `$Epilog`, which is reserved for completion checks.

Stdout and stderr are captured concurrently, displayed on completion, and retained
under a unique `output/wolfram-runs/` directory. `$InputFileName` refers to the
actual source, and the task's working directory is preserved. Custom script
arguments are not forwarded. Save `.wl` as UTF-8 without a BOM: Windows
PowerShell's `Set-Content -Encoding UTF8` adds a prefix that this kernel can
misinterpret as part of the first expression.
The runner rejects this BOM explicitly rather than allowing a misleading result.

Load shared setup in a calculation directly under this directory with:

```wl
If[Get[FileNameJoin[{DirectoryName[$InputFileName], "setup.wl"}]] =!= True,
  Exit[1]
];
```

`setup.wl` loads FeynCalc followed by FeynGrav using `Needs`. It does not reset
the global context or impose gauge, dimensional, or kinematic assumptions.
FeynGrav's own initialization loads its default libraries. Specify any extra
libraries and calculation-specific conventions in the calculation itself.

If existing packages are outside `$Path`, the ignored `local_config.wl` beside
`setup.wl` may extend `$Path`. Record installation locations in the ignored
`context/local_environment.md`; do not copy packages or old notebooks here.
The current direct-kernel setup uses this file to reference the existing
FeynCalc and FeynGrav Applications directory.

Durable sources belong here as `.wl`; retain `.nb` when interactivity is useful.
Write generated artifacts beneath the repository's ignored `output/` directory.

For the oscillator miniproject, the user requested a notebook as the primary
working artifact: [oscillator_uv_matching.nb](oscillator_uv_matching.nb).
Open it in Mathematica and evaluate the implemented input cells from the top in
a fresh kernel. The UV setup and stability checks are implemented; later sections
contain learning milestones. It requires only built-in functions. Its conceptual
roadmap is the vault's `03 Calculations/Oscillator Toy Model - UV Matching and
Runaway Solutions.md`. Reusable `.wl` pieces can follow as the calculation matures.
The existing **Run Current File** task accepts `.wl` only; it does not evaluate
this notebook.

CLI reference: [WolframScript documentation](https://reference.wolfram.com/language/ref/program/wolframscript.html).

Direct route: [Wolfram kernel documentation](https://reference.wolfram.com/language/ref/program/wolfram.html).

Runner regression checks (fresh kernels and disposable source files):

```powershell
powershell.exe -NoProfile -ExecutionPolicy RemoteSigned -File tests/wolfram_runner_test.ps1
```
