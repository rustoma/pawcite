---
id: APP-009
title: Ruff, mypy and pytest
milestone: APP-M2 · Python project
labels: python, testing
size: M (about 1 h)
depends_on: APP-008
---

# APP-009 · Ruff, mypy and pytest

## Goal
Linting, formatting, strict type checking and tests all run with one command each, and the first
real function has tests.

## Why it matters
These checks run in CI, before every commit, and in the AI's workflow.

## You will learn
- Ruff ≈ ESLint + Prettier, very fast. mypy ≈ `tsc --noEmit`. pytest ≈ Jest.
- pytest finds `test_*.py` files and `test_*` functions; plain `assert` is enough.
- `@pytest.mark.parametrize` ≈ Jest's `test.each`.

## Steps
1. From `python/`: `uv add --dev ruff mypy pytest`
2. In `python/pyproject.toml`:
   ```toml
   [tool.ruff]
   line-length = 100

   [tool.ruff.lint]
   select = ["E", "F", "I", "UP", "B", "SIM"]

   [tool.ruff.lint.isort]
   known-first-party = ["pawcite_core", "pawcite_api"]

   [tool.mypy]
   strict = true
   files = ["core/src", "api/src", "core/tests", "api/tests"]

   [tool.pytest.ini_options]
   testpaths = ["core/tests", "api/tests"]
   addopts = "--import-mode=importlib"
   ```
   (`known-first-party` keeps your own packages in their own import group;
   `--import-mode=importlib` lets two packages both have a `test_main.py`.)
3. Create `core/src/pawcite_core/text.py` with `normalize_question(text: str) -> str`: trim,
   collapse repeated spaces, and add a `?` if missing.
4. Create `core/tests/test_text.py` with a parametrized test (at least five cases) and an empty
   `api/tests/` folder with a placeholder test.
5. Run `uv run ruff check . && uv run ruff format --check . && uv run mypy && uv run pytest`

## Acceptance criteria
- [ ] All four commands pass.
- [ ] Breaking a type hint makes mypy fail; breaking a case makes pytest fail.

## Explain it back
1. What does mypy catch that pytest would not?
