# Webwright Playbook: Open-source Project Watchtower

## Purpose

Create a reusable source-seeded workflow for tracking public open-source project signals.

## Primary question

What changed publicly across selected open-source browser automation and agent tooling projects that a technical evaluator should know?

## Recommended command

```text
/webwright:craft Build a reusable open-source project watchtower. Read the maintained source registry at playbooks/sources/open-source-project-watchtower-sources.json. Visit seeded public repositories, release pages, changelogs, and documentation pages directly; do not rely on search-result pages as the primary scheduled-run discovery mechanism. Capture source URLs, visible dates or evergreen/undated labels, screenshots, source tier, direct evidence versus inference, confidence, recommended action, Markdown report, structured JSON, final_script.py path, and rerun command.
```

## Suggested parameters

| Parameter | Type | Default | Notes |
|---|---:|---|---|
| `source_config` | path | playbooks/sources/open-source-project-watchtower-sources.json | Maintained source registry |
| `lookback_days` | int | 30 | Dated releases and changelog entries; evergreen docs allowed when labeled |
| `max_items` | int | 25 | Keeps output reviewable |
| `max_child_pages` | int | 2 | High-relevance same-site child pages |
| `output_format` | str | markdown-json | Markdown plus JSON |

## Critical points

- CP1: Use source registry and source-native pages first.
- CP2: Capture source URL, visible date or evergreen label, source tier, and screenshot for each included item.
- CP3: Separate direct evidence from inference.
- CP4: Include confidence, recommended action, and review questions.
- CP5: Produce Markdown and structured JSON.
- CP6: Log empty, thin, blocked, or stale-source cases explicitly.
- CP7: Avoid login-walled sources unless explicitly authorized.
- CP8: Do not perform outbound or state-changing actions.

## Workspace

```text
outputs/open-source-project-watchtower
```
