---
id: APP-017
title: Your first LLM call through the gateway
milestone: APP-M3 · First API
labels: python, llm
size: S (about 45 min)
depends_on: APP-016
---

# APP-017 · Your first LLM call through the gateway

## Goal
A Python script asks a dog question through **your Go gateway** and prints the answer and the token usage.

## Why it matters
Your two repos meet for the first time: Python app → Go gateway → model.

## You will learn
- The OpenAI Python SDK: the same API as the TypeScript one, in Python.
- `AsyncOpenAI` vs `OpenAI` (async vs blocking).

## Steps
1. Start the gateway (`llm-gateway` repo) with your real config.
2. `uv add --package pawcite-core openai`
3. Create `core/src/pawcite_core/llm.py` with `def make_client(base_url: str, api_key: str) -> AsyncOpenAI`.
4. Create `core/src/pawcite_core/hello_llm.py` that takes a question from the command line, calls the
   `fast` alias, and prints the answer and `usage`.
5. Run: `uv run python -m pawcite_core.hello_llm "Why do dogs tilt their heads?"`
6. Check the gateway's logs show the request.

## Acceptance criteria
- [ ] The script prints an answer and the input/output token counts.
- [ ] The gateway log shows the call; nothing calls the provider directly.

## Explain it back
1. What exactly did you change to send OpenAI SDK traffic through your gateway?
2. What does `python -m pawcite_core.hello_llm` do differently from running a file path?
