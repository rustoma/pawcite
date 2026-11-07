---
id: APP-006
title: Python for JS developers - classes, errors, modules
milestone: APP-M1 · Python basics
labels: python, learning, hands-on
size: M (about 1.5 h)
depends_on: APP-005
---

# APP-006 · Python for JS developers: classes, errors, modules

## Goal
The dog script becomes typed data classes in a module, with proper error handling.

## Why it matters
Data classes and exceptions are how the API will represent papers, answers and failures.

## You will learn
- `@dataclass`: a class with fields and no boilerplate (≈ a TypeScript type plus a constructor).
- `Enum` for fixed choices like dog size.
- Exceptions: `raise ValueError(...)`, `try / except / finally`, and your own exception class.
- Modules: every `.py` file is a module; `from dogs import Dog`.
- `with open(...) as f:`: closes the file automatically (≈ `finally`, or Go's `defer`).

## Steps
1. Create `playground/dogs.py` with `@dataclass class Dog` (name, breed, age, size: `Size`).
2. Add a method `is_senior(self) -> bool` (8 years or older).
3. Add `class InvalidAgeError(ValueError)` and a function `parse_age(text: str) -> int` that
   raises it for negative or non-numeric input.
4. Create `playground/main.py` that imports from `dogs`, parses ages from a list of strings, and
   prints a friendly message for each error.
5. Read dog names from `playground/dogs.txt` using `with open(...)`.

## Acceptance criteria
- [ ] `uv run playground/main.py` handles valid, negative and non-numeric ages without crashing.
- [ ] The file is read with `with`.

## Explain it back
1. What does `@dataclass` generate for you?
2. Why subclass `ValueError` instead of `Exception` for `InvalidAgeError`?
