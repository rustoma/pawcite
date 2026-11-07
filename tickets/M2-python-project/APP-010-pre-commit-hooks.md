---
id: APP-010
title: Run checks before every commit
milestone: APP-M2 · Python project
labels: python, ci
size: S (about 30 min)
depends_on: APP-009
---

# APP-010 · Run checks before every commit

## Goal
Ruff and mypy run automatically on `git commit` and block badly formatted or badly typed code.

## You will learn
pre-commit ≈ husky + lint-staged.

## Steps
1. Install it once: `uv tool install pre-commit`
2. Create `.pre-commit-config.yaml` at the repo root:
   ```yaml
   repos:
     - repo: https://github.com/astral-sh/ruff-pre-commit
       rev: v0.17.4
       hooks:
         - id: ruff-check
           args: [--fix]
           files: ^python/
         - id: ruff-format
           files: ^python/
     - repo: local
       hooks:
         - id: mypy
           name: mypy (python)
           entry: uv run --directory python mypy
           language: system
           pass_filenames: false
           files: ^python/
   ```
3. `pre-commit install`, then `pre-commit run --all-files`.
4. Try to commit code with a formatting problem and watch the hook fix or block it.

## Acceptance criteria
- [ ] `pre-commit run --all-files` passes.
- [ ] A badly formatted file cannot be committed unchanged.

## Explain it back
1. Why run mypy through `uv run` instead of a separate pre-commit environment?
