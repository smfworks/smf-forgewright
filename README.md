# SMF Forgewright

SMF Forgewright is an AI-guided browser-automation and self-tuning workbench. It packages a Webwright-style reproducible browser workflow with a SkillOpt-style local tuning loop so an AI assistant such as OpenClaw, Hermes, ClawPilot, Claude Code, Codex, or another coding agent can set up a repeatable web automation, present sample use cases, guide configuration, run it, score it, tune it, and prepare dashboards.

Forgewright is designed for cross-platform use on Windows, macOS, and Linux.

## What this repo gives an AI agent

- A clear `AGENTS.md` bootstrap contract.
- OpenClaw and Hermes specific onboarding guides.
- Cross-platform setup scripts.
- A Python CLI wizard for use-case intake and scaffolding.
- Playbook, source registry, SkillOpt rubric, fixture, and dashboard templates.
- Sample public-source use cases.
- A static dashboard pattern with JSON payload injection.
- Safety guardrails for credentials, private data, and outbound actions.

## Quick start for a human

```bash
git clone https://github.com/smfworks/smf-forgewright.git
cd smf-forgewright
python -m venv .venv
# Windows PowerShell: .\.venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -e .
playwright install firefox
forgewright doctor
forgewright examples
forgewright init-use-case
```

Or use the setup script for your platform:

```powershell
# Windows PowerShell
.\scripts\setup.ps1
```

```bash
# macOS/Linux
bash scripts/setup.sh
```

## Quick start for an AI agent

Tell your AI assistant:

```text
Read AGENTS.md in this repository. Set up Forgewright, show me the sample use cases, ask me which one I want, then walk me through configuration, first run, SkillOpt tuning, and dashboard setup.
```

## Core workflow

1. Select or define a use case.
2. Capture source boundaries, auth requirements, evidence needs, output shape, and dashboard goals.
3. Generate a playbook and source registry.
4. Run a Webwright-style collection that produces `plan.md`, `final_script.py`, screenshots, logs, Markdown, and JSON.
5. Freeze local fixtures from playbook and run artifacts.
6. Run a SkillOpt-style tuning pass with bounded edits.
7. Human-review the promotion packet.
8. Promote the tuned playbook if approved.
9. Wire JSON output into a dashboard.

## Repository map

```text
AGENTS.md                         AI bootstrap contract
OPENCLAW.md                       OpenClaw-specific instructions
HERMES.md                         Hermes-specific instructions
docs/                             Engineering and safety docs
scripts/                          Cross-platform setup and dashboard helpers
src/forgewright/                  Python CLI wizard and utilities
templates/                        Playbook, source registry, rubric, fixtures, dashboard templates
playbooks/                        Example playbooks
playbooks/sources/                Example source registries
examples/                         Sample use-case kits
skillopt/                         SkillOpt-style harness templates
dashboards/                       Static dashboard templates
```

## Safety defaults

Forgewright defaults to public/frozen/local sources. It does not authorize live M365 reads, private customer data access, credentials in code, outbound messages, posts, purchases, scheduling, or state-changing actions. Those require explicit user authorization and should remain human-reviewed.

## License

MIT. See `LICENSE`.
