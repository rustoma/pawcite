---
id: APP-001
title: Create the repository on GitHub
milestone: APP-M0 · Setup
labels: setup
size: S (about 15 min)
depends_on: GW-020 (llm-gateway repo)
---

# APP-001 · Create the repository on GitHub

## Goal
This starter kit is a public GitHub repository named `pawcite`.

## Why it matters
This repo holds the app people use: the Python API, the mobile app, and later the evals.
The gateway lives in its own repo because it is a separate product.

## Steps
1. Unzip the starter kit and open a terminal in the `pawcite` folder.
2. First commit:
   ```bash
   git init -b main
   git add .
   git commit -m "APP-001: starter kit"
   ```
3. `gh repo create pawcite --public --source . --push`
4. Open it: `gh repo view --web`.

## Acceptance criteria
- [ ] The repo exists on GitHub with the README, `AGENTS.md`, `tickets/` and `.claude/` visible.

## Explain it back
1. Why are the gateway and the app in separate repositories?
