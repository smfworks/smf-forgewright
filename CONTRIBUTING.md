# Contributing

Contributions should preserve Forgewright's safety defaults and artifact-first workflow.

## Guidelines

- Keep setup cross-platform.
- Do not add required cloud services for core operation.
- Do not commit secrets, tokens, cookies, or private data.
- Add or update templates when changing output contracts.
- Keep examples public-source and unauthenticated.
- Prefer small, reviewable changes.

## Validation

Before opening a PR:

```bash
pip install -e .
forgewright examples
forgewright doctor
```
