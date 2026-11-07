---
id: APP-023
title: Type checks, lint and CI for the app
milestone: APP-M4 · First mobile app
labels: mobile, ci
size: S (about 45 min)
depends_on: APP-022
---

# APP-023 · Type checks, lint and CI for the app

## Goal
TypeScript and lint checks run locally and on every pull request that touches `mobile/`.

## Steps
1. From `mobile/`: `npx tsc --noEmit`, then `npm run lint`. The first lint run sets up ESLint;
   commit the config it creates.
2. Create `.github/workflows/mobile.yml`:
   - triggers: `pull_request` and `push` to `main`, with `paths: ["mobile/**"]`
   - `defaults.run.working-directory: mobile`
   - `actions/checkout@v7`
   - `actions/setup-node@v7` with `node-version: lts/*`, `cache: npm` and
     `cache-dependency-path: mobile/package-lock.json`
   - `npm ci`, `npx tsc --noEmit`, `npm run lint`
3. Open a pull request and watch it pass.

## Acceptance criteria
- [ ] Both checks pass locally and in CI.
- [ ] A type error makes CI fail.

## Explain it back
1. Why use `npm ci` instead of `npm install` in CI?
