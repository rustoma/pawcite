---
id: APP-007
title: Python for JS developers - type hints and async
milestone: APP-M1 · Python basics
labels: python, learning, hands-on
size: M (about 1 h)
depends_on: APP-006
---

# APP-007 · Python for JS developers: type hints and async

## Goal
Fetch three "papers" at the same time with `asyncio`, with full type hints checked by mypy.

## Why it matters
FastAPI is built on async, and the API will wait on the gateway and the database concurrently.

## You will learn
- Type hints are **not enforced at runtime**; mypy checks them (≈ `tsc --noEmit`).
- `list[str]`, `dict[str, int]`, `str | None`.
- `async def`, `await`, and `asyncio.gather(...)` (≈ `Promise.all`).
- The event loop: like Node's, it runs one thing at a time and switches while something waits.

## Steps
1. Create `playground/papers.py` with `async def fetch_paper(paper_id: str) -> dict[str, str]`
   that waits with `await asyncio.sleep(1)` and returns a fake paper.
2. Fetch three papers one after another and time it; then with `asyncio.gather` and time it.
3. Run `uvx mypy --strict playground/papers.py` and fix every complaint.
4. Add a deliberate type error, see mypy catch it, then remove it.

## Acceptance criteria
- [ ] Sequential takes about 3 seconds; `gather` takes about 1 second.
- [ ] `uvx mypy --strict playground/papers.py` passes.

## Explain it back
1. If type hints are not enforced, why use them?
2. What would happen if `fetch_paper` called `time.sleep(1)` instead of `await asyncio.sleep(1)`?
