# Safety model

Forgewright is designed to make browser automation reviewable and bounded.

## Defaults

- Use public unauthenticated sources.
- Keep all run artifacts local.
- Capture screenshots, source URLs, logs, JSON, and provenance.
- Separate direct evidence from inference.
- Require human review before promotion or external sharing.

## Prohibited by default

- Private workspace data reads.
- Customer system login.
- Credentials, secrets, tokens, cookies, or session data in code.
- Sending, posting, drafting, scheduling, purchasing, deleting, or changing external state.
- Silent promotion of tuned playbooks.

## Allowed with explicit authorization

A user may authorize a specific run to use internal or authenticated sources. In that case:

1. Confirm scope and purpose.
2. Do not store credentials.
3. Prefer environment variables or interactive login.
4. Mark outputs with sensitivity/provenance.
5. Require review before sharing.
