# OpenClaw guide for SMF Forgewright

OpenClaw can use this repository as a local skill/workbench.

## Suggested OpenClaw prompt

```text
Read AGENTS.md and OPENCLAW.md. Set up SMF Forgewright, run the doctor check, show me the sample use cases, and guide me through creating a source-seeded Webwright playbook, first run, SkillOpt tuning pass, and dashboard setup.
```

## OpenClaw operating pattern

1. Use `AGENTS.md` as the bootstrap contract.
2. Use `forgewright examples` to present starter use cases.
3. Use `forgewright init-use-case` to create a configured playbook workspace.
4. Use the generated playbook to author a reproducible browser script.
5. Keep run artifacts local and reviewable.
6. Use the SkillOpt templates to freeze fixtures and tune playbook instructions.
7. Ask the user before promoting a candidate playbook.

## Integration notes

- Keep generated use cases under `outputs/` or a user-specified workspace.
- Prefer public sources and source registries for scheduled runs.
- If OpenClaw has browser or shell tools, it can run the generated scripts directly.
- If OpenClaw has no browser tool, it can still generate playbooks, fixtures, dashboards, and SkillOpt packets for another runner.
