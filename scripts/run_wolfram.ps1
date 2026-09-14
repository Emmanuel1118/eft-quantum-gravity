[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)][string]$FilePath,
    [switch]$RequireSmokePass
)

$ErrorActionPreference = 'Stop'
$kernelProcess = $null
try {
    $source = (Resolve-Path -LiteralPath $FilePath).Path
    if ([IO.Path]::GetExtension($source) -ne '.wl') {
        throw 'Select a saved .wl source file.'
    }
    $sourceBytes = [IO.File]::ReadAllBytes($source)
    if ($sourceBytes.Length -ge 3 -and $sourceBytes[0] -eq 239 -and
        $sourceBytes[1] -eq 187 -and $sourceBytes[2] -eq 191) {
        throw 'Save the .wl source as UTF-8 without BOM; this kernel can misinterpret the BOM.'
    }
    $projectRoot = Split-Path -Parent $PSScriptRoot
    $runDirectory = Join-Path $projectRoot ('output/wolfram-runs/' + [guid]::NewGuid().ToString('N'))
    New-Item -ItemType Directory -Path $runDirectory -Force | Out-Null
    $stdoutPath = Join-Path $runDirectory 'stdout.txt'
    $stderrPath = Join-Path $runDirectory 'stderr.txt'
    $env:EFT_WOLFRAM_SOURCE = $source
    $env:EFT_WOLFRAM_COMPLETION = Join-Path $runDirectory 'completed.txt'
    $bootstrap = Join-Path $PSScriptRoot 'wolfram_run.wl'
    $configPath = Join-Path $projectRoot 'context/wolfram.local.json'
    if (Test-Path -LiteralPath $configPath) {
        $config = Get-Content -Raw -LiteralPath $configPath | ConvertFrom-Json
        $executable = (Resolve-Path -LiteralPath $config.kernelPath).Path
        $env:WOLFRAM_USERBASE = Join-Path $projectRoot 'output/wolfram-userbase'
        New-Item -ItemType Directory -Path $env:WOLFRAM_USERBASE -Force | Out-Null
        $arguments = @('-noicon', '-noprompt', '-script', ('"' + $bootstrap + '"'))
    } else {
        $executable = (Get-Command wolframscript -CommandType Application -ErrorAction Stop).Source
        $env:WOLFRAMSCRIPT_CONFIGURATIONPATH = Join-Path $projectRoot 'output/WolframScript.conf'
        $arguments = @('-local', '-file', ('"' + $bootstrap + '"'))
    }
    Write-Output ('Wolfram logs: ' + $runDirectory)
    $startInfo = New-Object System.Diagnostics.ProcessStartInfo
    $startInfo.FileName = $executable
    $startInfo.Arguments = $arguments -join ' '
    $startInfo.WorkingDirectory = (Get-Location).Path
    $startInfo.UseShellExecute = $false
    $startInfo.CreateNoWindow = $true
    $startInfo.RedirectStandardOutput = $true
    $startInfo.RedirectStandardError = $true
    $kernelProcess = New-Object System.Diagnostics.Process
    $kernelProcess.StartInfo = $startInfo
    if (-not $kernelProcess.Start()) { throw 'Could not start the local Wolfram process.' }
    # Drain both pipes concurrently, including short-lived processes, and wait
    # for complete output before checking results.
    $stdoutRead = $kernelProcess.StandardOutput.ReadToEndAsync()
    $stderrRead = $kernelProcess.StandardError.ReadToEndAsync()
    $kernelProcess.WaitForExit()
    $kernelExitCode = $kernelProcess.ExitCode
    $stdoutText = $stdoutRead.GetAwaiter().GetResult()
    $stderrText = $stderrRead.GetAwaiter().GetResult()
    [IO.File]::WriteAllText($stdoutPath, $stdoutText)
    [IO.File]::WriteAllText($stderrPath, $stderrText)
    $stdout = @($stdoutText -split '\r?\n')
    $stderr = @($stderrText -split '\r?\n' | Where-Object { $_ -ne '' })
    $stdout | Write-Output
    $stderr | ForEach-Object { [Console]::Error.WriteLine($_) }
    if ($kernelExitCode -ne 0) { exit $kernelExitCode }
    if (-not (Test-Path -LiteralPath $env:EFT_WOLFRAM_COMPLETION) -or
        (Get-Content -Raw -LiteralPath $env:EFT_WOLFRAM_COMPLETION) -ne 'COMPLETED') {
        throw 'Wolfram exited without completing the source. Inspect the startup errors in the run logs.'
    }
    if ($RequireSmokePass -and $stdout -notcontains 'PASS: MATHEMATICA_SMOKE_TEST') {
        throw 'Wolfram returned without the smoke-test PASS marker. Inspect the run logs.'
    }
    exit 0
} catch {
    [Console]::Error.WriteLine($_.Exception.Message)
    exit 1
} finally {
    if ($null -ne $kernelProcess) {
        if (-not $kernelProcess.HasExited) { $kernelProcess.Kill() }
        $kernelProcess.Dispose()
    }
}
