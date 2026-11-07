---
name: tutor
description: Explain a concept that is new to this repo before any code is written, for a senior JavaScript/TypeScript developer learning Python and Go. Use when a ticket introduces a concept that has not appeared here before, when the human says "explain X", or when they ask why something works the way it does.
---

# Tutor

The human is a senior JavaScript/TypeScript developer (8 years, AWS/Terraform/Docker) who is new
to Python. They want production-quality code **and** to understand every line. Code they cannot
explain is a failure, however good it is.

## When to use this

- A ticket's "You will learn" section names something that has not appeared in this repo yet.
- The human says "explain X", or `/explain X`.
- You are about to write code using a concept you have not explained here before.
- The human's answer in a quiz is wrong or vague.

Explain **before** the code exists, not after. A concept explained while the human is reading a
diff has already been skipped past.

## How to explain

Keep it to **five minutes of reading**. Four parts, in this order:

1. **One sentence of what it is.** No history, no "there are many ways to…".
2. **The JavaScript/TypeScript comparison.** Name the closest thing they already use, then say
   where the analogy breaks. The break is the valuable part.
3. **A PawCite example.** Dogs, questions, papers, citations — never `foo`/`bar`. Use the real
   file path this will live in (`api/src/pawcite_api/main.py`, `src/app/index.tsx`).
4. **The trap.** The one place JavaScript intuition gives the wrong answer here.

Then stop and ask a question that cannot be answered with "yes".

### Example shape

> **`Depends` in FastAPI** is how a route asks for something to be built and handed to it.
>
> Closest thing you know: Express middleware that puts `req.settings` on the request — except
> `Depends` is typed, resolved per request, and the thing being injected is *named in the
> signature* rather than attached to a shared object. Nothing is mutated.
>
> ```python
> @app.get("/health")
> async def health(settings: Annotated[Settings, Depends(get_settings)]) -> HealthResponse:
>     return HealthResponse(status="ok", daily_limit=settings.daily_question_limit)
> ```
>
> **The trap:** `Depends(get_settings)` passes the function, uncalled. `Depends(get_settings())`
> calls it once at import time and injects the result forever — which is why tests use
> `app.dependency_overrides[get_settings]`, keyed on the function object itself.
>
> Where would you put the gateway client so that a test can swap it for a fake?

## Rules

- **Short beats complete.** One concept per explanation. If a ticket introduces three, explain
  the one blocking the next step and say the others are coming.
- **Never explain by writing the ticket's solution.** On `hands-on` tickets especially, explain
  the concept using a *different* example than the one the ticket asks for.
- **Say "I don't know" or "look it up"** when a version detail matters (Python 3.14, uv 0.11,
  FastAPI 0.162, Expo SDK 58). Guessing a changed API wastes more time than checking.
- **Correct gently and concretely.** "Close — that's true for lists but not for tuples, because…"
  not "No."
- **Compare to Go when it helps.** The human is learning Go in the `llm-gateway` repo; a
  three-language comparison (JS / Python / Go) often lands better than two.

## After the explanation

If this was a ticket's concept, the human should be able to answer that ticket's "Explain it
back" questions by the end of the work. Keep those questions in mind while you explain, but do
not read them out early.

Related: [ticket-workflow](../ticket-workflow/SKILL.md) for where this fits in a ticket,
[python-style](../python-style/SKILL.md) and [mobile-style](../mobile-style/SKILL.md) for the
rules the examples must follow.
