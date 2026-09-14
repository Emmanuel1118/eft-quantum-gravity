# Local Wolfram execution

Use the installed local Mathematica kernel and `wolframscript` on PATH.
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

The runner calls `wolframscript -local -file <source>` and preserves nonzero
exit codes. The smoke task also requires an explicit final PASS marker because
the installed launcher has returned exit code zero without evaluating code
when launched in the Codex Windows sandbox. A zero exit code alone is not proof
that a calculation ran; inspect its expected results.

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
No local configuration file is needed for the verified normal-user installation.

Durable sources belong here as `.wl`; retain `.nb` when interactivity is useful.
Write generated artifacts beneath the repository's ignored `output/` directory.

CLI reference: [WolframScript documentation](https://reference.wolfram.com/language/ref/program/wolframscript.html).
