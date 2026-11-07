---
id: APP-004
title: Create issues and add them to the board
milestone: APP-M0 · Setup
labels: setup, learning
size: S (about 40 min)
depends_on: APP-003
---

# APP-004 · Create issues and add them to the board

## Goal
All `APP` tickets are GitHub issues on the same project board as the gateway tickets.

## You will learn
How to read your first Python program: `scripts/create_issues.py`.

## Steps
1. Preview: `uv run scripts/create_issues.py --dry-run`
2. Create everything: `uv run scripts/create_issues.py`
3. Add the new issues to your `PawCite learning` board (Projects → your board → add items from `pawcite`).
4. Read the script with the AI. Find and explain:
   - `def` with type hints (`def gh(*args: str) -> str:`)
   - an f-string
   - a list and a dict
   - a set comprehension (`{... for ... in ...}`)
   - reading a file with `Path.read_text`
   - `if __name__ == "__main__":`

## Acceptance criteria
- [ ] All `APP` tickets are issues with labels and milestones, on the shared board.
- [ ] Running the script again creates nothing new.
- [ ] You can explain the six Python constructs in step 4.

## Explain it back
1. What does `*args` mean in `def gh(*args: str)`?
2. Why does the script check `if __name__ == "__main__":`?

## Notes for the AI
Compare each construct to its JavaScript equivalent. Do not change the script.
