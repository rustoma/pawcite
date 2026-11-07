---
id: APP-014
title: Request and response models
milestone: APP-M3 · First API
labels: python, api
size: S (about 1 h)
depends_on: APP-013
---

# APP-014 · Request and response models

## Goal
`POST /ask` accepts a question and returns a placeholder answer with placeholder citations, with
validation done by Pydantic.

## Why it matters
This request/response shape is the contract between the phone and the API. The real answers
arrive later; the shape stays.

## You will learn
- Pydantic models (≈ Zod schemas): validation and types in one place.
- `Field(min_length=3, max_length=500)`; invalid input returns **422** with a clear message.
- `response_model` makes the OpenAPI spec exact, which the app's typed client will rely on.

## Steps
1. Models: `AskRequest(question: str)` with length limits; `Citation(title: str, year: int, doi: str)`;
   `AskResponse(answer: str, citations: list[Citation])`.
2. `POST /ask` returns a fixed answer mentioning the question, plus one example citation.
3. In `/docs`, send a valid question, then `"hi"`, and read the 422 response.

## Acceptance criteria
- [ ] A valid question returns 200 with the answer and a citation.
- [ ] A two-character question returns 422 explaining the minimum length.

## Explain it back
1. Who writes the 422 response, and what does it contain?
