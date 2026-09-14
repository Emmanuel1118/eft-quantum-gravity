# Integration checks against the installed local kernel; fixtures are disposable.
$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path -Parent $PSScriptRoot
$fixtureDirectory = Join-Path $projectRoot ('output/runner test ' + [guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Path $fixtureDirectory | Out-Null
$runner = Join-Path $projectRoot 'scripts/run_wolfram.ps1'
$cases = @(
    @{ Name = 'success'; Code = 'Print["CWD: ", Directory[]]; Print["SOURCE: ", $InputFileName]; If[FileNameSplit[Directory[]] =!= FileNameSplit[DirectoryName[$InputFileName]], Exit[2]]; Print["RESULT: ", 2 + 2];'; Exit = 0; Match = 'RESULT: 4' },
    @{ Name = 'explicit_exit'; Code = 'Print["RESULT: explicit exit"]; Exit[0];'; Exit = 0; Match = 'RESULT: explicit exit' },
    @{ Name = 'nonzero'; Code = 'Exit[7];'; Exit = 7; Match = $null },
    @{ Name = 'abort'; Code = 'Abort[];'; Exit = 1; Match = $null },
    @{ Name = 'syntax'; Code = 'Print['; Exit = 1; Match = $null },
    @{ Name = 'missing_completion'; Code = 'Clear[$Epilog]; Exit[0];'; Exit = 1; Match = 'Wolfram exited without completing the source.' },
    @{ Name = 'utf8_bom'; Code = 'Print[4];'; BOM = $true; Exit = 1; Match = 'Save the .wl source as UTF-8 without BOM' }
)
try {
    Push-Location $fixtureDirectory
    foreach ($case in $cases) {
        $fixture = Join-Path $fixtureDirectory ($case.Name + '.wl')
        # Windows PowerShell's UTF8 option adds a BOM that this kernel treats as
        # part of the first symbol. .NET writes UTF-8 without that prefix.
        if ($case.BOM) {
            [IO.File]::WriteAllText($fixture, $case.Code, (New-Object Text.UTF8Encoding($true)))
        } else {
            [IO.File]::WriteAllText($fixture, $case.Code)
        }
        # Capture the deliberately failing cases without PowerShell treating their
        # stderr as a terminating error before we can inspect the exit code.
        $ErrorActionPreference = 'Continue'
        $lines = & powershell.exe -NoProfile -ExecutionPolicy RemoteSigned -File $runner -FilePath $fixture 2>&1
        $actualExit = $LASTEXITCODE
        $ErrorActionPreference = 'Stop'
        $outputText = $lines | Out-String
        if ($actualExit -ne $case.Exit -or
            ($case.Match -and -not $outputText.Contains($case.Match))) {
            throw ('FAIL: ' + $case.Name + ', exit=' + $actualExit + "`n" + $outputText)
        }
        Write-Output ('PASS: ' + $case.Name)
    }
} finally {
    Pop-Location
    # Only delete these exact generated fixtures; no recursive deletion.
    foreach ($case in $cases) {
        $fixture = Join-Path $fixtureDirectory ($case.Name + '.wl')
        if (Test-Path -LiteralPath $fixture) { Remove-Item -LiteralPath $fixture }
    }
    Remove-Item -LiteralPath $fixtureDirectory
}
