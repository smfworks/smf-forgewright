# Forgewright engineering guide

## Concept

Forgewright combines two patterns:

1. Webwright-style browser automation: a coding AI writes reproducible Playwright scripts, captures screenshots, logs every meaningful step, and produces durable artifacts.
2. SkillOpt-style tuning: local frozen fixtures, rubrics, bounded candidate edits, validation/test scoring, provenance, and human-reviewed promotion.

The result is a repo an AI can read, set up, and use to guide a human from use-case selection to running and tuning a repeatable browser workflow.

## Cross-platform support

Supported platforms:

- Windows PowerShell
- macOS Bash/Zsh
- Linux Bash

The Python package provides the same CLI across platforms. Setup scripts create a virtual environment, install the package in editable mode, and install Firefox for Playwright.

## Use-case flow

1. `forgewright examples`
2. `forgewright init-use-case`
3. Edit generated source registry.
4. Ask the AI to run the generated `/webwright:craft` command.
5. Inspect artifacts under `outputs/<use-case>`.
6. Freeze fixtures under `skillopt/<use-case>`.
7. Score baseline against the rubric.
8. Apply at most three bounded edits to the playbook candidate.
9. Re-score validation, then test.
10. Human reviews promotion packet.
11. Promote candidate playbook if approved.
12. Refresh dashboard from JSON output.

## Webwright artifact contract

Repeatable runs should emit:

```text
plan.md
final_runs/run_<n>/final_script.py
final_runs/run_<n>/final_script_log.txt
final_runs/run_<n>/screenshots/*.png
final_runs/run_<n>/report.md
final_runs/run_<n>/data.json
```

## SkillOpt artifact contract

Tuning runs should emit:

```text
scorecard.json
provenance.md
accepted-diff.patch or rejected-edits.md
best_playbook.md, if accepted
promotion-packet.md
```

## Dashboard contract

Dashboards consume JSON, not screenshots or markdown. Use `templates/dashboard-data-contract.json` as the expected schema. Static dashboards can embed the latest payload in:

```html
<script id="payload" type="application/json">{}</script>
```

## Safety gates

- Public/frozen/local sources by default.
- No private workspace data reads by default.
- No credentials in files.
- No login-walled sources without explicit authorization.
- No outbound/state-changing actions without explicit confirmation.
- Human approval before promotion.
