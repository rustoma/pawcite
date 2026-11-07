---
name: python-style
description: Rules for writing or changing Python in python/ — the uv workspace, FastAPI, Pydantic, async, typing and tests. Use before editing any .py file or adding a Python dependency.
---

# Python style

Python 3.14. A uv workspace in `python/`. Read this before touching a `.py` file.

## Layout

```
python/
  pyproject.toml        [tool.uv.workspace] members = ["core", "api"]
  uv.lock               committed
  .env.example          every setting, fake values
  core/src/pawcite_core/   retrieval, prompts, LLM client — shared
  api/src/pawcite_api/     FastAPI service
  ml/                      evals, data processing (later)
```

Package name `pawcite-core`, import name `pawcite_core`. Hyphens on disk and in metadata,
underscores in `import`.

## Dependencies

Always name the workspace member — never a bare `uv add`, never `pip`:

```bash
uv add --package pawcite-api "fastapi[standard]"
uv add --package pawcite-core openai
uv add --package pawcite-api --dev pytest-asyncio
```

Shared code goes in `core`; only the web layer goes in `api`. If the API grows a dependency that
the evals will also need, it belongs in `core`.

## Typing

- Type hints on **every** function signature, including `-> None`.
- `uv run mypy` runs `--strict`. No `Any`, no bare `# type: ignore` — if you must ignore, name the
  rule: `# type: ignore[arg-type]` with a comment saying why.
- Builtin generics: `list[str]`, `dict[str, int]`, `str | None`. Not `List`, not `Optional`.
- `Annotated[Settings, Depends(get_settings)]` for injected parameters.

## FastAPI and Pydantic

Pydantic models at the **edges** — request bodies, response bodies, settings. Plain dataclasses or
simple types inside. Do not thread a Pydantic model through five layers of business logic.

```python
class AskRequest(BaseModel):
    question: str = Field(min_length=3, max_length=500)

class AskResponse(BaseModel):
    answer: str
```

Declare the response model on the route (`response_model=AskResponse` or the return annotation) so
`/docs` and the generated TypeScript client stay correct — APP-025 builds the mobile client from
this OpenAPI schema, so a sloppy schema becomes a sloppy app.

Raise `HTTPException` for client errors. Let Pydantic produce the 422; do not hand-validate.

## Async

Endpoints are `async def`. Inside an async function, **only async clients**:

- `AsyncOpenAI`, not `OpenAI`
- `httpx.AsyncClient`, not `requests`
- `asyncio.sleep`, not `time.sleep`

One blocking call freezes the whole event loop for every request. If something is genuinely
blocking and has no async version, push it to `anyio.to_thread.run_sync`.

Create clients once at startup (lifespan) and reuse them. A new `AsyncClient` per request leaks
connections.

## Model calls

Every model call goes through the Go gateway, using the OpenAI SDK with `base_url` pointed at it.
Never call `api.openai.com` or `api.anthropic.com` from this repo.

```python
client = AsyncOpenAI(
    base_url=settings.gateway_url,                     # http://localhost:8080/v1
    api_key=settings.gateway_api_key.get_secret_value(),
)
```

## Settings and secrets

`pydantic-settings` with a `Settings` class, `get_settings()` wrapped in `@lru_cache`. Secrets are
`SecretStr`, so they print as `**********`. Real values live in `python/.env` (git-ignored); every
setting is listed with a fake value in `.env.example`.

Never log, print, commit or put a secret in an error message.

## Tests

- `pytest`, with `TestClient` (or `httpx.AsyncClient`) against the app.
- **Tests never touch a real model or a real network.** Use a fake client and
  `app.dependency_overrides[...]` to inject it. A test that needs an API key is a broken test.
- Name tests for the behaviour: `test_short_question_is_rejected`, not `test_ask_2`.
- Test the safety rules explicitly — they are product requirements, not nice-to-haves.

## Checks

From `python/`, all four must pass before a pull request:

```bash
uv run ruff check . && uv run ruff format --check . && uv run mypy && uv run pytest
```

Ruff needs `known-first-party = ["pawcite_core", "pawcite_api"]` or it sorts the workspace
packages as third-party and the format check fails in CI but not locally.

## Safety (product rule, enforced in code and prompts)

The app **never** diagnoses a specific dog and **never** gives a medication dose. Emergencies
("my dog ate chocolate", "she is bleeding", "he collapsed") go to a vet, immediately and without
hedging. Every prompt, every response model and every test respects this.

## Naming

`snake_case` for functions and variables, `PascalCase` for classes, `UPPER_SNAKE` for constants.
A leading underscore means private. Modules are short and lowercase: `settings.py`, `prompts.py`.
