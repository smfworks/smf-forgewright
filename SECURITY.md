# Security

Report security issues privately to the repository owner.

## Secret handling

Never commit credentials, PATs, tokens, cookies, private organizational data, or session exports.

## Default data boundary

Forgewright defaults to public unauthenticated sources and local frozen fixtures.

## Outbound action boundary

Forgewright examples must not send, post, draft, schedule, purchase, delete, or mutate external systems unless a user explicitly authorizes that exact action and a human confirmation gate is preserved.
