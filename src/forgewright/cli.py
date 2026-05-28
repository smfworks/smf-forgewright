from __future__ import annotations

import argparse
import json
import platform
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

SAMPLE_USE_CASES = [
    {
        "id": "open-source-project-watchtower",
        "title": "Open-source project watchtower",
        "description": "Track public GitHub repositories, release pages, and docs for change signals with evidence screenshots and dashboard-ready JSON.",
        "source_mode": "source-registry-first",
        "auth": "public unauthenticated",
    },
    {
        "id": "product-release-monitor",
        "title": "Product release monitor",
        "description": "Watch public release notes, docs, and product pages for changes and summarize field impact.",
        "source_mode": "source-registry-first",
        "auth": "public unauthenticated",
    },
    {
        "id": "competitive-watchtower",
        "title": "Competitive watchtower",
        "description": "Track public project/product pages, positioning, release notes, and docs.",
        "source_mode": "source-registry-first",
        "auth": "public unauthenticated",
    },
    {
        "id": "policy-regulatory-monitor",
        "title": "Policy and regulatory monitor",
        "description": "Monitor public policy, regulatory, and compliance sources with provenance and confidence labels.",
        "source_mode": "source-registry-first",
        "auth": "public unauthenticated",
    },
]


def run(cmd: list[str]) -> tuple[int, str]:
    try:
        completed = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, check=False)
        return completed.returncode, (completed.stdout + completed.stderr).strip()
    except FileNotFoundError as exc:
        return 127, str(exc)


def doctor(_: argparse.Namespace) -> int:
    checks = []
    checks.append(("OS", platform.platform()))
    checks.append(("Python", platform.python_version()))
    code, out = run(["python", "--version"])
    checks.append(("python command", out if code == 0 else f"missing: {out}"))
    code, out = run(["python", "-c", "import playwright; print('playwright ok')"])
    checks.append(("playwright package", out if code == 0 else "not installed"))
    code, out = run(["python", "-m", "playwright", "--version"])
    checks.append(("playwright cli", out if code == 0 else "not installed"))
    print(json.dumps({"root": str(ROOT), "checks": dict(checks)}, indent=2))
    return 0


def examples(_: argparse.Namespace) -> int:
    print(json.dumps({"sample_use_cases": SAMPLE_USE_CASES}, indent=2))
    return 0


def bootstrap(_: argparse.Namespace) -> int:
    code, doctor_output = run(["python", "-m", "forgewright.cli", "doctor"])
    doctor_payload = json.loads(doctor_output) if code == 0 else {"error": doctor_output}
    payload = {
        "status": "ready" if code == 0 else "needs_setup",
        "message": "Forgewright public demo bootstrap",
        "recommended_first_demo": "open-source-project-watchtower",
        "next_prompt_for_ai": (
            "Use the open-source-project-watchtower example. Show the source registry, "
            "explain the evidence contract, then walk me through a first run, local "
            "SkillOpt-style tuning, and dashboard refresh."
        ),
        "sample_use_cases": SAMPLE_USE_CASES,
        "doctor": doctor_payload,
        "public_safety_boundary": [
            "Use public unauthenticated sources for the demo.",
            "Do not use private workspace data.",
            "Do not use confidential organization names or confidential data.",
            "Do not send, post, draft, schedule, purchase, or change external state.",
        ],
    }
    print(json.dumps(payload, indent=2))
    return 0


def slugify(value: str) -> str:
    return "".join(ch.lower() if ch.isalnum() else "-" for ch in value).strip("-").replace("--", "-") or "use-case"


def ask(prompt: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    value = input(f"{prompt}{suffix}: ").strip()
    return value or default


def init_use_case(_: argparse.Namespace) -> int:
    title = ask("Use-case title", "Open-source project watchtower")
    use_case_id = ask("Use-case id", slugify(title))
    audience = ask("Audience", "project maintainers and technical evaluators")
    primary_question = ask("Primary question", "What changed publicly across these projects that this audience should know?")
    source_boundary = ask("Source boundary", "public unauthenticated only")
    output_format = ask("Output format", "markdown-json")
    workspace = ROOT / "outputs" / use_case_id
    playbook = ROOT / "playbooks" / f"{use_case_id}.md"
    source_registry = ROOT / "playbooks" / "sources" / f"{use_case_id}-sources.json"
    workspace.mkdir(parents=True, exist_ok=True)
    source_registry.parent.mkdir(parents=True, exist_ok=True)

    playbook.write_text(f"""# Webwright Playbook: {title}

## Purpose

Create a repeatable Webwright-style workflow for {audience}.

## Primary question

{primary_question}

## Recommended command

```text
/webwright:craft Build a reusable {title} collector. Read the maintained source registry at {source_registry.as_posix()}. Visit seeded public sources directly; do not rely on search-result pages as the primary scheduled-run discovery mechanism. Capture source URLs, visible dates or evergreen/undated labels, screenshots, source tier, direct evidence versus inference, confidence, recommended action, Markdown report, structured JSON, final_script.py path, and rerun command.
```

## Suggested parameters

| Parameter | Type | Default | Notes |
|---|---:|---|---|
| `source_config` | path | {source_registry.as_posix()} | Maintained source registry |
| `lookback_days` | int | 30 | Dated items; evergreen pages allowed when labeled |
| `max_items` | int | 25 | Keeps output reviewable |
| `max_child_pages` | int | 2 | High-relevance same-site child pages |
| `output_format` | str | {output_format} | Markdown plus JSON recommended |
| `today` | str | current date | YYYY-MM-DD |

## Critical points

- CP1: Use source registry and source-native pages first.
- CP2: Capture URL, date or evergreen label, source tier, and screenshot for each included item.
- CP3: Separate direct evidence from inference.
- CP4: Include confidence and recommended action.
- CP5: Produce Markdown and structured JSON.
- CP6: Log empty, thin, blocked, or stale-source cases explicitly.
- CP7: Avoid login-walled sources unless explicitly authorized.
- CP8: Do not perform outbound or state-changing actions.

## Source boundary

{source_boundary}

## Workspace

```text
{workspace.as_posix()}
```
""", encoding="utf-8")

    source_registry.write_text(json.dumps({
        "version": "1.0",
        "description": f"Source registry for {title}.",
        "sources": [
            {
                "name": "Example public source",
                "url": "https://example.com/",
                "category": "public",
                "source_tier": "public",
                "auth": "public",
                "tags": ["example"],
                "notes": "Replace with approved seeded sources."
            }
        ],
        "blocked_or_excluded_sources": []
    }, indent=2), encoding="utf-8")

    print(json.dumps({
        "created": True,
        "use_case_id": use_case_id,
        "playbook": str(playbook),
        "source_registry": str(source_registry),
        "workspace": str(workspace),
        "next_steps": [
            "Replace example sources in the registry.",
            "Ask your AI to run the recommended /webwright:craft command.",
            "Use generated run artifacts to create frozen SkillOpt fixtures.",
            "Create dashboard from the structured JSON output."
        ]
    }, indent=2))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="SMF Forgewright CLI")
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("doctor", help="Check local environment")
    p.set_defaults(func=doctor)
    p = sub.add_parser("examples", help="List sample use cases")
    p.set_defaults(func=examples)
    p = sub.add_parser("bootstrap", help="Show setup status, safe demo choices, and the next AI prompt")
    p.set_defaults(func=bootstrap)
    p = sub.add_parser("init-use-case", help="Interactively create a use-case playbook and source registry")
    p.set_defaults(func=init_use_case)
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
