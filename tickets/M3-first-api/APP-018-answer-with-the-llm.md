---
id: APP-018
title: Answer questions with the LLM (no papers yet)
milestone: APP-M3 · First API
labels: python, api, llm, testing
size: M (about 1.5 h)
depends_on: APP-017
---

# APP-018 · Answer questions with the LLM (no papers yet)

## Goal
`POST /ask` answers with the model through the gateway, following the safety rules, and tests use a
fake model instead of a real one.

## Why it matters
The first real feature. Papers and citations come later; the safety rules start now.

## You will learn
- An `async def` endpoint calling `AsyncOpenAI`.
- System prompts as constants in `pawcite_core`, not inline in endpoints.
- Testing with a fake client injected through a dependency.

## Steps
1. In `core/src/pawcite_core/prompts.py`, a `SYSTEM_PROMPT` that: answers dog questions in plain
   language; says research citations are coming soon; never diagnoses a specific dog; never gives
   medication doses; tells the user to contact a vet immediately for emergencies.
2. `async def answer_without_sources(client, question) -> str` in `pawcite_core`.
3. `/ask` uses it through a `get_llm_client` dependency; return an empty `citations` list for now.
4. Tests: override `get_llm_client` with a fake whose `chat.completions.create` returns a fixed
   answer; check `/ask` returns it and that the system prompt was sent.
5. Manually ask "My dog ate chocolate, what should I do?" and check the answer sends you to a vet.

## Acceptance criteria
- [ ] `/ask` returns real answers when the gateway runs.
- [ ] Tests pass with no network access.
- [ ] The chocolate question gets "contact a vet now" advice, not a home treatment.

## Explain it back
1. Why is the system prompt in `core` instead of in the endpoint?
2. Why must tests never call the real model?
