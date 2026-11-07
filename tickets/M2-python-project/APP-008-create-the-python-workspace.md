---
id: APP-008
title: Create the Python workspace
milestone: APP-M2 · Python project
labels: python, setup
size: M (about 1 h)
depends_on: APP-007
---

# APP-008 · Create the Python workspace

## Goal
`python/` is a uv workspace with two packages, `pawcite-core` (shared code) and `pawcite-api`
(the web service), and the API can import the core.

## Why it matters
The API, the evals and the data jobs will all import the same retrieval and prompt code from
`core`, so nothing is written twice.

## You will learn
- A uv workspace ≈ npm workspaces: several packages, one lock file, one virtual environment.
- The `src/` layout and why packages are installed in "editable" mode.
- Package name `pawcite-core` vs import name `pawcite_core`.

## Steps
1. Create `python/pyproject.toml`:
   ```toml
   [tool.uv.workspace]
   members = ["core", "api"]
   ```
2. From `python/`:
   ```bash
   uv python pin 3.14
   uv init --package --name pawcite-core core
   uv init --package --name pawcite-api api
   uv add --package pawcite-api pawcite-core
   ```
3. Look at `api/pyproject.toml`: find the dependency on `pawcite-core` and `[tool.uv.sources]`.
4. Check: `uv run python -c "import pawcite_core, pawcite_api; print('ok')"`
5. Commit `uv.lock`; check `.venv/` is ignored.

## Acceptance criteria
- [ ] The import check prints `ok`.
- [ ] `python/uv.lock` is committed and `python/.venv/` is not.

## Explain it back
1. Why is the package called `pawcite-core` but imported as `pawcite_core`?
2. What does `{ workspace = true }` in `[tool.uv.sources]` mean?
