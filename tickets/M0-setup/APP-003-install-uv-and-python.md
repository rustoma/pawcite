---
id: APP-003
title: Install uv and Python 3.14
milestone: APP-M0 · Setup
labels: setup, python
size: S (about 30 min)
depends_on: APP-002
---

# APP-003 · Install uv and Python 3.14

## Goal
`uv` is installed and runs Python 3.14.

## Why it matters
uv manages Python versions, virtual environments and dependencies with one fast tool.

## You will learn
- uv ≈ nvm + npm + npx in one. `uv.lock` ≈ `package-lock.json`.
- The Python REPL ≈ the Node REPL.

## Steps
1. Install uv:
   - macOS / Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`
   - Windows (PowerShell): `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
2. `uv --version`
3. `uv python install 3.14`
4. Open a REPL: `uv run --python 3.14 python`. Try `1 + 1`, `"luna".title()`,
   `len(["Luna", "Max"])`, `help(str.title)`. Exit with `exit()`.
5. In VS Code, install the **Python** extension (by Microsoft) and the **Ruff** extension.

## Acceptance criteria
- [ ] `uv run --python 3.14 python --version` prints `Python 3.14.x`.
- [ ] Your editor highlights Python files.

## Explain it back
1. Which JavaScript tools does uv replace?
