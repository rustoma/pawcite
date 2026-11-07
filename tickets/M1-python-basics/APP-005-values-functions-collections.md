---
id: APP-005
title: Python for JS developers - values, functions, collections
milestone: APP-M1 · Python basics
labels: python, learning, hands-on
size: M (about 1.5 h)
depends_on: APP-004
---

# APP-005 · Python for JS developers: values, functions, collections

## Goal
A script that manages a small list of dogs using Python's core building blocks.

## Why it matters
Every later ticket uses these: questions are strings, papers are dicts, results are lists.

## You will learn
- f-strings: `f"{name} is {age}"` (≈ template literals).
- `list` (≈ array), `dict` (≈ object/`Map`), `set`, `tuple` (an immutable list).
- List comprehensions: `[d["name"] for d in dogs if d["age"] > 2]` (≈ `filter` + `map`).
- Functions with type hints, default values and keyword arguments.
- `None` (≈ `null`), and truthiness: **empty lists, dicts and strings are falsy** (unlike JS arrays).
- Indentation is syntax: blocks are defined by indentation, not braces.

## Steps
1. Create `playground/basics.py`.
2. Make a list of five dogs as dicts: `{"name": "Luna", "breed": "Beagle", "age": 3}`.
3. Print the names of dogs older than 2 with a list comprehension.
4. Count dogs per breed in a dict and print it sorted by breed.
5. Write `def describe(name: str, age: int, *, loves: str = "papers") -> str` and call it with
   and without the keyword argument.
6. Run it: `uv run playground/basics.py`

## Acceptance criteria
- [ ] The script prints the filtered names, the sorted breed counts and two descriptions.
- [ ] You used at least one comprehension, one f-string and one keyword argument.

## Explain it back
1. What does `if dogs:` check, and how is that different from `if (dogs)` in JavaScript?
2. What does the `*` in the parameter list force callers to do?

## Notes for the AI
Hands-on. Use dog examples; point out every place where JavaScript intuition would mislead.
