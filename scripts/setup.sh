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
python -m pip install -e .
python -m playwright install firefox
python -m forgewright.cli doctor

echo "Setup complete. Try: forgewright examples"
