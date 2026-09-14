[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)][string]$FilePath,
    [switch]$RequireSmokePass
)

$ErrorActionPreference = 'Stop'
try {
    $source = (Resolve-Path -LiteralPath $FilePath).Path
    if ([IO.Path]::GetExtension($source) -ne '.wl') {
        throw 'Select a saved .wl source file.'
    }
    $executable = (Get-Command wolframscript -CommandType Application -ErrorAction Stop).Source
    $smokePassed = $false
    & $executable -local -file $source | ForEach-Object {
        Write-Output $_
        if ($_ -eq 'PASS: MATHEMATICA_SMOKE_TEST') { $smokePassed = $true }
    }
    $kernelExitCode = $LASTEXITCODE
    if ($kernelExitCode -ne 0) { exit $kernelExitCode }
    # Some launcher failures return zero without executing any Wolfram code.
    if ($RequireSmokePass -and -not $smokePassed) {
        throw 'Wolfram returned without the smoke-test PASS marker. Check local kernel licensing and launcher access.'
    }
    exit 0
} catch {
    [Console]::Error.WriteLine($_.Exception.Message)
    exit 1
}
