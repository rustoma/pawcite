# AGENTS.md: rules for AI coding assistants

This file is for AI assistants (Claude Code, Codex and others). Humans are welcome to read it too.

## About this project

**PawCite** is a dog-research assistant: people ask questions about dogs (behaviour, training,
health research) and get answers grounded in published studies, with citations and an honest
label for how strong the evidence is.

```
Expo app (TypeScript) ──▶ API + RAG (Python, FastAPI) ──▶ llm-gateway (Go, separate repo) ──▶ models
                                   │
                          PostgreSQL + pgvector
```

It is also a **learning project**. The human:
- is a senior JavaScript/TypeScript developer (8 years) who knows AWS, Terraform and Docker,
- is **new to Python** (and is learning Go in the `llm-gateway` repo),
- wants production-quality code **and** to understand every line of it.

Both goals matter equally. Fast code the human cannot explain is a failure.

## How we work

1. **One ticket at a time.** Tickets live in `tickets/<milestone>/<ID>-<name>.md`. Read the whole
   ticket before doing anything. The order is in `LEARNING-PATH.md`; check `depends_on`.
2. **Explain before you write.** When a ticket uses a concept that has not appeared in this repo
   before, explain it first with the `tutor` skill. Keep it short and concrete.
3. **Respect `hands-on` tickets.** The human writes the code. You explain, hint and review. Do not
   write the solution unless the human explicitly asks "show me the solution".
4. **Small changes.** One ticket = one branch = one pull request. Branch names: `app-013-hello-fastapi`.
5. **Done means done.** Never mark a ticket done until every acceptance criterion is met and the
   checks pass. Show the evidence.
6. **Finish with "Explain it back".** Ask the ticket's questions one at a time, wait, correct
   gently. Then add 2–3 bullets to `docs/learning-log.md`.

## Repository layout

```
mobile/    Expo app (TypeScript)                 created in APP-019
python/    uv workspace                          created in APP-008
  core/    shared code: retrieval, prompts, LLM client
  api/     FastAPI service
  ml/      evals, data processing (later)
auth/      Better Auth service (later)
infra/     Terraform (later)
tickets/   the work, one file per ticket
```

## Technical rules

**Python** (details: `python-style` skill)
- Python 3.14, uv workspace in `python/`. Add dependencies with `uv add --package <member> <dep>`.
- FastAPI and Pydantic at the edges; type hints everywhere (`mypy --strict` must pass).
- Async endpoints use async clients only (`AsyncOpenAI`, `httpx.AsyncClient`); never block the event loop.
- Tests never call real models or networks: use fakes and dependency overrides.
- Checks (from `python/`): `uv run ruff check . && uv run ruff format --check . && uv run mypy && uv run pytest`

**Mobile** (details: `mobile-style` skill)
- Expo with Expo Router, TypeScript strict, no `any`.
- `EXPO_PUBLIC_*` variables are bundled into the app and visible to anyone: never put secrets in them.
- Checks (from `mobile/`): `npx tsc --noEmit && npm run lint`

**Everywhere**
- All model calls go through the gateway with the OpenAI SDK (`base_url` = gateway). Never call a
  provider directly from app code.
- Secrets come from environment variables or `.env` (git-ignored). Never commit or print them.
- **Safety:** the app never diagnoses a specific dog and never gives medication doses. Emergencies
  ("my dog ate chocolate") are always sent to a vet. Every prompt and screen respects this.

## Skills

Skills live in `.claude/skills/<name>/SKILL.md`. When a task matches a skill, read that file first.

| Skill | Use it when |
|---|---|
| `tutor` | A new concept appears, or the human asks you to explain something |
| `ticket-workflow` | Starting, working on or finishing a ticket |
| `code-review` | Reviewing changes before a pull request is merged |
| `python-style` | Writing or changing Python code |
| `mobile-style` | Writing or changing the Expo app |

## Phrases the human may use

| The human says | You do |
|---|---|
| "start APP-013" | Follow `ticket-workflow` for ticket APP-013 |
| "explain dataclasses" | Follow `tutor` |
| "review" | Follow `code-review` for the current branch |
| "quiz me" | Ask the current ticket's "Explain it back" questions |
| "next" | Find the next ticket in `LEARNING-PATH.md` whose dependencies are done |

Claude Code also has these as slash commands in `.claude/commands/`.
