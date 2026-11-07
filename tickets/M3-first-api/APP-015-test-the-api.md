---
id: APP-015
title: Test the API
milestone: APP-M3 · First API
labels: python, testing
size: S (about 45 min)
depends_on: APP-014
---

# APP-015 · Test the API

## Goal
Automated tests cover `/health`, a valid `/ask`, and an invalid `/ask`.

## You will learn
- `TestClient` calls your app in-process, with no running server (≈ supertest).
- pytest fixtures: reusable setup, injected by parameter name.

## Steps
1. Create `api/tests/test_main.py` with a `client` fixture returning `TestClient(app)`.
2. Tests: health is ok; a valid question returns an answer and a citation; `"hi"` returns 422.
3. Remove the placeholder test from APP-009.
4. Run all checks.

## Acceptance criteria
- [ ] Three tests pass locally and in CI.

## Explain it back
1. How does pytest know what to pass as the `client` argument?
