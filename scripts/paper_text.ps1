# Use the installed modern runtime rather than the machine's Python 3.7.
$paperPython = Join-Path $env:USERPROFILE '.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe'
if (-not (Test-Path -LiteralPath $paperPython)) {
    $paperPython = (Get-Command python -ErrorAction Stop).Source
}
& $paperPython (Join-Path $PSScriptRoot 'paper_text.py') @args
exit $LASTEXITCODE
