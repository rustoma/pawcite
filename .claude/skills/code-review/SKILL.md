---
name: code-review
description: Review the current branch before its pull request is merged, against this repo's rules — safety, secrets, the gateway boundary, async correctness, typing and tests. Use when the human says "review" or runs /review, and always before opening a pull request.
---

# Code review

Review the branch against `main`, in this order. Stop at the first section that fails — a leaked
secret matters more than a naming nit, and burying it under twelve style comments hides it.

```bash
git fetch origin && git diff origin/main...HEAD
```

## 1. Blockers — these stop the review

**Secrets.** Any key, token, password or connection string in the diff. Check `.env` is not
staged, that nothing was added to `EXPO_PUBLIC_*` that is not a public URL, and that no secret
reaches a log line, an error message or a test fixture. If one was ever committed, it is burned:
say so and say it needs rotating, not just removing.

**Safety.** Does anything here let the app diagnose a specific dog, give a medication dose, or
answer an emergency with something other than "see a vet now"? Check prompts, response models,
fallback text and on-screen copy. This is a product requirement, not a preference.

**The gateway boundary.** Every model call goes through the Go gateway via the OpenAI SDK with
`base_url`. A direct call to `api.openai.com` or `api.anthropic.com` fails review.

## 2. Does it meet the ticket?

Open the ticket file and read the acceptance criteria. For each one: is it actually true, and is
there **evidence** — real command output, a screenshot for mobile? "Looks right" is not evidence.

Then: is the diff **bigger than the ticket**? Unrelated refactors, drive-by renames and "while I
was in there" changes belong in their own ticket. Say so.

## 3. Correctness

- **Async**: a blocking call inside `async def` (`requests`, `time.sleep`, a sync `OpenAI`
  client) freezes the event loop for every user. A client created per request leaks connections.
- **Error paths**: what happens when the gateway is down, slow, or returns a 429? A bare `except:`
  or an `except Exception: pass` hides exactly the failure you will spend an evening on.
- **Boundaries**: empty question, whitespace-only question, a 10,000-character question, a
  non-ASCII question. The API is the real boundary — client-side validation is a convenience, not
  a defence.
- **Types**: does `mypy --strict` actually pass, or did an `Any` or a bare `# type: ignore` make
  it pass? The second one is worse than a failing check.

## 4. Tests

- Do they **run without a network and without an API key**? A test calling a real model is broken
  even when it is green.
- Do they test the behaviour or the implementation? A test that breaks on every refactor is a
  liability.
- Are the safety rules tested explicitly?
- Is there a test for the failure case, not only the happy path?

## 5. Style and clarity

Only after everything above. [python-style](../python-style/SKILL.md),
[mobile-style](../mobile-style/SKILL.md). Naming, dead code, comments that explain *why* rather
than restating the line.

## 6. Can the human explain it?

This repo has a second goal: the human must understand every line. So:

- Flag anything clever. Clever code the human cannot explain in a month is a defect here, even
  when it is correct and fast.
- If the branch used a concept that was never explained, say so and offer
  [tutor](../tutor/SKILL.md) before the merge, not after.
- Pick the one or two most interesting lines in the diff and ask what they do. A review that ends
  with the human understanding the code is worth more than one that ends with zero comments.

## How to report

Group by severity, most serious first, and be specific — file and line, what breaks, and the
concrete input that breaks it:

- **Must fix** — must change before merge (secret, safety, gateway, failing criterion).
- **Should fix** — a real bug or a missing test, but not a merge stopper.
- **Consider** — style, naming, a simpler shape. The human may decline these.

Say plainly when the branch is clean. Do not invent findings to look thorough; three real
comments beat twelve padded ones.
