# Webwright Playbook: Public HLS Field Intelligence

## Purpose

Create a reusable source-seeded workflow for public healthcare and life sciences field intelligence.

## Primary question

What public account, market, Microsoft, or competitor signal should a field team know before engagement?

## Recommended command

```text
/webwright:craft Build a reusable public HLS field intelligence collector. Read the maintained source registry at playbooks/sources/public-hls-field-intelligence-sources.json. Visit seeded public sources directly; do not rely on search-result pages as the primary scheduled-run discovery mechanism. Capture source URLs, visible dates or evergreen/undated labels, screenshots, source tier, direct evidence versus inference, confidence, recommended seller motion, discovery questions, Markdown report, structured JSON, final_script.py path, and rerun command.
```

## Suggested parameters

| Parameter | Type | Default | Notes |
|---|---:|---|---|
| `source_config` | path | playbooks/sources/public-hls-field-intelligence-sources.json | Maintained source registry |
| `lookback_days` | int | 30 | Dated news; evergreen pages allowed when labeled |
| `max_items` | int | 25 | Keeps output reviewable |
| `max_child_pages` | int | 2 | Same-site high-relevance child pages |
| `output_format` | str | markdown-json | Markdown plus JSON |

## Critical points

- CP1: Use source registry and source-native pages first.
- CP2: Capture source URL, visible date or evergreen label, source tier, and screenshot for each included item.
- CP3: Separate direct evidence from inference.
- CP4: Include confidence, seller motion, and discovery questions.
- CP5: Produce Markdown and structured JSON.
- CP6: Log empty, thin, blocked, or stale-source cases explicitly.
- CP7: Avoid login-walled sources unless explicitly authorized.
- CP8: Do not perform outbound or state-changing actions.

## Workspace

```text
outputs/public-hls-field-intelligence
```
