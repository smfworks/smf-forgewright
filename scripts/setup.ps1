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
# hsf_5eeb129e1510a742c74afd73: playwright is version-pinned in pyproject.toml
# so every install resolves the same driver and downloads the same Firefox
# build. After install, print the resolved playwright version so the operator
# can confirm it matches pyproject.toml before any browser use.
& $python -m pip install -e .
& $python -m playwright install firefox
& $python -c "import json, subprocess; resolved = subprocess.run(['pip', 'show', 'playwright'], capture_output=True, text=True).stdout; version = next((l.split(':', 1)[1].strip() for l in resolved.splitlines() if l.startswith('Version:')), 'unknown'); print(json.dumps({'playwright_resolved_version': version, 'expected': '1.49.1'}))"
& $python -m forgewright.cli doctor

Write-Host "Setup complete. Try: forgewright examples"
