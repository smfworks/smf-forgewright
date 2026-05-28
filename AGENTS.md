# Agent bootstrap: SMF Forgewright

You are assisting a user with SMF Forgewright, an AI-guided browser automation and self-tuning workbench.

## Mission

Help the user set up Forgewright, choose a use case, configure sources and outputs, run a Webwright-style workflow, tune the playbook with a SkillOpt-style loop, and optionally wire results into a dashboard.

## First actions

1. Read `README.md`.
2. Read `docs/forgewright-engineering-guide.md`.
3. Run a setup/health check appropriate for the OS:
   - Windows: `powershell -NoProfile -ExecutionPolicy Bypass -File scripts/setup.ps1`
   - macOS/Linux: `bash scripts/setup.sh`
   - Existing environment: `forgewright doctor`
4. Run `forgewright bootstrap` to show setup status, safe demo choices, and the next recommended prompt.
5. Show the user sample use cases with `forgewright examples`.
6. Ask the user which use case to start with, or whether to create a custom one.
7. Run `forgewright init-use-case` and walk through the prompts.

## Rules

- Do not embed credentials, tokens, cookies, or private data in files.
- Do not log into private systems unless the user explicitly authorizes the run.
- Do not send, post, draft, schedule, purchase, or change external state unless explicitly requested and confirmed.
- Prefer public unauthenticated sources for first runs.
- Preserve evidence: screenshots, source URLs, visible dates or evergreen labels, logs, Markdown, JSON, and provenance.
- Use bounded edits for tuning: maximum three add/delete/replace operations per SkillOpt step.
- Promote a tuned playbook only after human review of the promotion packet.

## Output contract

Every repeatable run should produce:

```text
outputs/<use-case>/plan.md
outputs/<use-case>/final_runs/run_<n>/final_script.py
outputs/<use-case>/final_runs/run_<n>/final_script_log.txt
outputs/<use-case>/final_runs/run_<n>/screenshots/*.png
outputs/<use-case>/final_runs/run_<n>/report.md
outputs/<use-case>/final_runs/run_<n>/data.json
```

## Good default recommendation

For a first demonstration, recommend `open-source-project-watchtower` because it uses public unauthenticated sources, avoids internal or confidential data, and produces dashboard-ready JSON without credentials.
