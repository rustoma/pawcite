---
description: Review the current branch against this repo's rules before the pull request
---

Review the current branch against `main`.

Follow the `code-review` skill (`.claude/skills/code-review/SKILL.md`) in order:

```bash
git fetch origin && git diff origin/main...HEAD
```

1. **Blockers** — secrets, the safety rule (no diagnosis, no doses, emergencies to a vet), the
   gateway boundary (no direct provider calls).
2. **Does it meet the ticket** — read the acceptance criteria from the ticket file and check each
   one has real evidence. Flag anything in the diff that is bigger than the ticket.
3. **Correctness** — async/blocking calls, error paths, boundary inputs, whether `mypy --strict`
   passes honestly.
4. **Tests** — do they run with no network and no API key? Is the failure case covered? Are the
   safety rules tested?
5. **Style** — `python-style` / `mobile-style`.
6. **Can I explain it** — flag anything clever, and ask me what the two most interesting lines do.

Report grouped as **Blocker** / **Should fix** / **Consider**, most serious first, with file,
line and the input that breaks it. Say plainly if it is clean — do not pad the list.

Also run the checks and show me the real output:
- Python, from `python/`: `uv run ruff check . && uv run ruff format --check . && uv run mypy && uv run pytest`
- Mobile, from `mobile/`: `npx tsc --noEmit && npm run lint`
