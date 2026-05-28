# Webwright Playbook: <Use Case Name>

## Purpose

Describe the repeatable browser workflow and the decision it supports.

## Primary question

What should this workflow answer every time it runs?

## Recommended command

```text
/webwright:craft Build a reusable <use case> collector. Read the maintained source registry at playbooks/sources/<use-case>-sources.json. Visit seeded public sources directly; do not rely on search-result pages as the primary scheduled-run discovery mechanism. Capture source URLs, visible dates or evergreen/undated labels, screenshots, source tier, direct evidence versus inference, confidence, recommended action, Markdown report, structured JSON, final_script.py path, and rerun command.
```

## Suggested parameters

| Parameter | Type | Default | Notes |
|---|---:|---|---|
| `source_config` | path | playbooks/sources/<use-case>-sources.json | Maintained source registry |
| `lookback_days` | int | 30 | Dated items; evergreen pages allowed when labeled |
| `max_items` | int | 25 | Keeps output reviewable |
| `max_child_pages` | int | 2 | Same-site high-relevance child pages |
| `output_format` | str | markdown-json | Markdown plus JSON |
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

## Workspace

```text
outputs/<use-case>
```
