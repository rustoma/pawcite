---
id: APP-002
title: Connect your AI assistant to this repo
milestone: APP-M0 · Setup
labels: setup, ai
size: S (about 20 min)
depends_on: APP-001
---

# APP-002 · Connect your AI assistant to this repo

## Goal
Claude Code (or Codex) follows this repo's rules, including the Python, mobile and safety rules.

## Why it matters
This repo has rules the gateway did not: the medical safety rule, and never putting secrets in
`EXPO_PUBLIC_*` variables.

## Steps
1. Start Claude Code in the `pawcite` folder.
2. Ask: "What are the safety rules of this project, and where do model calls have to go?"
3. Try `/explain what is FastAPI, in one minute`.
4. Skim the five skills in `.claude/skills/`; note what `python-style` and `mobile-style` cover.

## Acceptance criteria
- [ ] The assistant names the safety rule (no diagnosis, no doses, emergencies to a vet) and says
      model calls go through the gateway.
- [ ] The explanation compares FastAPI with something from Node (for example Express).

## Explain it back
1. Why does the app never call model providers directly?
