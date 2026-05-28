$ErrorActionPreference = "Stop"

Write-Host "Setting up SMF Forgewright..."

if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
  throw "Python was not found on PATH. Install Python 3.10+ and rerun."
}

if (-not (Test-Path ".venv")) {
  python -m venv .venv
}

$python = Join-Path (Get-Location) ".venv\Scripts\python.exe"
& $python -m pip install --upgrade pip
& $python -m pip install -e .
& $python -m playwright install firefox
& $python -m forgewright.cli doctor

Write-Host "Setup complete. Try: forgewright examples"
