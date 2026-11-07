---
id: APP-016
title: Settings and secrets
milestone: APP-M3 · First API
labels: python, api
size: S (about 1 h)
depends_on: APP-015
---

# APP-016 · Settings and secrets

## Goal
The API reads its settings (gateway URL and key, daily question limit) from the environment or a
`.env` file, validated at startup, and tests can override them.

## Why it matters
The same code runs on your laptop, in CI and in the cloud with different settings and no secrets
in the code.

## You will learn
- `pydantic-settings`: a typed settings class filled from environment variables and `.env`.
- `SecretStr`: a value that never shows up in logs or `repr`.
- FastAPI dependencies (`Depends`) and `app.dependency_overrides` for tests (dependency injection).

## Steps
1. `uv add --package pawcite-api pydantic-settings`
2. `api/src/pawcite_api/settings.py`: `Settings` with `gateway_url` (default
   `http://localhost:8080/v1`), `gateway_api_key: SecretStr`, `daily_question_limit: int = 20`;
   `get_settings()` wrapped in `@lru_cache`.
3. `.env.example` at `python/` listing every setting with fake values; your real `.env` stays local.
   Until the gateway has API keys (gateway milestone GW-M6), any value works for `gateway_api_key`.
4. Inject settings into `/health` and return the daily limit (never the key).
5. Test: override `get_settings` to return a limit of 5 and check `/health` shows 5.

## Acceptance criteria
- [ ] Missing `gateway_api_key` makes the app fail at startup with a clear message.
- [ ] Printing the settings shows `**********` for the key.
- [ ] The override test passes.

## Explain it back
1. Why is `get_settings` cached?
2. How does `dependency_overrides` make testing easier?
