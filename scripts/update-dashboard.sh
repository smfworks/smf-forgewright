#!/usr/bin/env bash
set -euo pipefail
DATA_PATH="${1:?usage: update-dashboard.sh data.json dashboard.html}"
DASHBOARD_PATH="${2:?usage: update-dashboard.sh data.json dashboard.html}"
python - "$DATA_PATH" "$DASHBOARD_PATH" <<'PY'
from pathlib import Path
import re, sys
payload = Path(sys.argv[1]).read_text(encoding='utf-8').replace('</script>', '<\\/script>')
path = Path(sys.argv[2])
html = path.read_text(encoding='utf-8')
updated = re.sub(r'<script id="payload" type="application/json">.*?</script>', '<script id="payload" type="application/json">' + payload + '</script>', html, flags=re.S)
path.write_text(updated, encoding='utf-8')
print({'dashboard': str(path), 'data': sys.argv[1]})
PY
