---
id: APP-025
title: A typed API client from OpenAPI
milestone: APP-M4 · First mobile app
labels: mobile, api
size: S (about 45 min)
depends_on: APP-024
---

# APP-025 · A typed API client from OpenAPI

## Goal
The app's request and response types are generated from the API's OpenAPI spec, so a change in
the Python models shows up as a TypeScript error in the app.

## Why it matters
Two languages, one contract, checked by the compiler.

## You will learn
FastAPI publishes `/openapi.json`; `openapi-typescript` turns it into TypeScript types.

## Steps
1. With the API running: `npx openapi-typescript http://localhost:8000/openapi.json -o src/api/schema.d.ts`
2. Add `"gen:api"` to `package.json` scripts with that command.
3. Use the generated types for `askQuestion`'s request and response.
4. Experiment: rename `answer` to `text` in the Python response model, regenerate, and watch
   `tsc` fail. Then undo it.

## Acceptance criteria
- [ ] `askQuestion` uses only generated types; no hand-written copies of the API types.
- [ ] The rename experiment produced a type error.

## Explain it back
1. What problem does generating types solve compared with writing them by hand?
