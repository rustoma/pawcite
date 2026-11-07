---
id: APP-011
title: CI for Python
milestone: APP-M2 · Python project
labels: python, ci
size: S (about 45 min)
depends_on: APP-010
---

# APP-011 · CI for Python

## Goal
Every pull request that touches `python/` runs lint, format check, mypy and tests on GitHub.

## Steps
1. Create `.github/workflows/python.yml`:
   - triggers: `pull_request` and `push` to `main`, with `paths: ["python/**"]`
   - `defaults.run.working-directory: python`
   - `actions/checkout@v7`
   - `astral-sh/setup-uv@v10.3.3` with `enable-cache: true`
   - `uv sync --locked`, then ruff check, ruff format --check, mypy, pytest
2. Open a pull request and watch it pass.
3. Protect `main` with a ruleset requiring the check (as in the gateway repo).

## Acceptance criteria
- [ ] The workflow passes on a pull request.
- [ ] A failing test blocks merging.

## Explain it back
1. What does `uv sync --locked` refuse to do, and why is that good in CI?
