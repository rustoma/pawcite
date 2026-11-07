---
id: APP-013
title: Hello FastAPI
milestone: APP-M3 · First API
labels: python, api
size: S (about 45 min)
depends_on: APP-012
---

# APP-013 · Hello FastAPI

## Goal
The API runs locally, answers `GET /health`, and shows its interactive docs at `/docs`.

## Why it matters
This is the service the phone app will talk to.

## You will learn
- Route decorators: `@app.get("/health")` (≈ `app.get("/health", handler)` in Express).
- Return a dict or a model and FastAPI turns it into JSON.
- Uvicorn runs the app (≈ Node's HTTP server); `fastapi dev` reloads on every change.
- Automatic docs from your code at `/docs`.

## Steps
1. From `python/`: `uv add --package pawcite-api "fastapi[standard]"`
2. Create `api/src/pawcite_api/main.py` with `app = FastAPI(title="PawCite API")` and
   `GET /health` returning `{"status": "ok"}`.
3. Run: `uv run fastapi dev api/src/pawcite_api/main.py`
4. Open http://127.0.0.1:8000/health and http://127.0.0.1:8000/docs and try the endpoint there.

## Acceptance criteria
- [ ] `/health` returns `{"status": "ok"}`.
- [ ] `/docs` shows the endpoint and "Try it out" works.
- [ ] Editing the response and saving reloads the server automatically.

## Explain it back
1. Where does the documentation at `/docs` come from?
