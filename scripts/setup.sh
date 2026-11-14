#!/usr/bin/env bash
set -euo pipefail

echo "Setting up SMF Forgewright..."

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 was not found. Install Python 3.10+ and rerun." >&2
  exit 1
fi

if [ ! -d .venv ]; then
  python3 -m venv .venv
fi

. .venv/bin/activate
python -m pip install --upgrade pip
# hsf_5eeb129e1510a742c74afd73: playwright is version-pinned in pyproject.toml
# so every install resolves the same driver and downloads the same Firefox
# build. After install, print the resolved playwright version so the operator
# can confirm it matches pyproject.toml before any browser use.
python -m pip install -e .
python -m playwright install firefox
python - <<'PY'
import json, subprocess
resolved = subprocess.run(["pip", "show", "playwright"], capture_output=True, text=True).stdout
version = next((l.split(":", 1)[1].strip() for l in resolved.splitlines() if l.startswith("Version:")), "unknown")
print(json.dumps({"playwright_resolved_version": version, "expected": "1.49.1"}))
PY
python -m forgewright.cli doctor

echo "Setup complete. Try: forgewright examples"
