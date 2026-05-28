# Example: SkillOpt-style tuning loop

1. Freeze the current playbook as `source-playbook.md`.
2. Freeze source registry and prior run artifacts.
3. Create train/val/test fixtures.
4. Score baseline against `templates/skillopt-rubric-template.md`.
5. Propose at most three bounded edits.
6. Apply edits to `candidate-playbook.md` only.
7. Re-score validation.
8. If validation improves and has zero automatic failures, score test.
9. Write `scorecard.json`, `provenance.md`, `accepted-diff.patch`, `best_playbook.md`, and `promotion-packet.md`.
10. Promote only after human approval.
