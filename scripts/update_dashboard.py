#!/usr/bin/env python3
"""Regenerate a dashboard's embedded payload from a data.json file, safely.

Fixes hsf_c8c57fa44fb445a77fa4423b: the old scripts spliced raw data.json text
into the dashboard's <script type="application/json"> tag escaping only
'</script>', letting every other HTML metacharacter through. This version
JSON-parses the data file (schema gate), re-serializes it with
json.dumps(..., ensure_ascii=False) so the embedded text is always valid JSON
with no raw HTML metacharacter sequences outside JSON string escapes, and
embeds that canonical serialization.

Usage: python update_dashboard.py data.json dashboard.html [dashboard ...]
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

PAYLOAD_TAG = re.compile(
    r'(<script id="payload" type="application/json">)(.*?)(</script>)',
    re.S,
)

# Minimal schema gate: the dashboard render script expects these keys.
REQUIRED_KEYS = {"account_results", "global_results", "empty_cases"}


def fail(msg: str) -> "NoReturn":  # type: ignore[name-defined]
    print(msg, file=sys.stderr)
    raise SystemExit(2)


def main(argv: list[str]) -> int:
    if len(argv) < 3:
        fail("usage: update_dashboard.py data.json dashboard.html [dashboard ...]")

    data_path = Path(argv[1])
    if not data_path.is_file():
        fail(f"Data file not found: {data_path}")

    try:
        payload = json.loads(data_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        fail(f"Data file is not valid UTF-8 JSON: {exc}")

    if not isinstance(payload, dict):
        fail("Data file must contain a JSON object at the top level.")

    missing = REQUIRED_KEYS - payload.keys()
    if missing:
        fail(f"Data file missing required key(s): {', '.join(sorted(missing))}")

    # Canonical re-serialization: every string is JSON-escaped, so no raw
    # '<' or '>' sequence appears outside JSON string escapes. Escape '/' after
    # '<' ('<\/' is a legal JSON string escape) so no '</script' sequence can
    # terminate the host script tag early. This is the standard HTML-inside-JSON
    # embedding defense.
    embedded = json.dumps(payload, ensure_ascii=False, indent=2).replace("</", "<\\/")

    # Defense in depth: assert the embedded text cannot terminate the tag.
    if "</script" in embedded.lower():
        fail("Internal error: serialized payload contains a raw </script sequence.")

    for dash in argv[2:]:
        path = Path(dash)
        if not path.is_file():
            fail(f"Dashboard file not found: {path}")
        html = path.read_text(encoding="utf-8")
        if not PAYLOAD_TAG.search(html):
            fail(f"Dashboard has no payload tag: {path}")
        updated = PAYLOAD_TAG.sub(
            lambda m: m.group(1) + embedded + m.group(3), html, count=1
        )
        path.write_text(updated, encoding="utf-8")
        print({"dashboard": str(path), "data": str(data_path)})

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
