#!/usr/bin/env bash
set -euo pipefail
DATA_PATH="${1:?usage: update-dashboard.sh data.json dashboard.html [dashboard ...]}"
shift
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "$SCRIPT_DIR/update_dashboard.py" "$DATA_PATH" "$@"
