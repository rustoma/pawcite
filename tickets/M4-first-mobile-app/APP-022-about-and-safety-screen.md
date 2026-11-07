---
id: APP-022
title: About and safety screen
milestone: APP-M4 · First mobile app
labels: mobile
size: S (about 45 min)
depends_on: APP-021
---

# APP-022 · About and safety screen

## Goal
An About screen explains what the app is, that it is not veterinary advice, and what to do in an
emergency. The Ask screen links to it.

## Why it matters
The safety message must be easy to find from the start.

## You will learn
- Adding a route: a new file `src/app/about.tsx`.
- `Stack` navigation in `_layout.tsx`, with screen titles.
- `Link` from `expo-router` (≈ Next.js `Link`).

## Steps
1. Create `src/app/about.tsx` with three short sections: what PawCite does, "not veterinary
   advice", and "in an emergency, contact a vet immediately".
2. In `_layout.tsx`, use a `Stack` with titles "PawCite" and "About".
3. Add a link from the Ask screen to About.

## Acceptance criteria
- [ ] You can open About from the Ask screen and go back.
- [ ] The emergency text is visible without scrolling.

## Explain it back
1. How does Expo Router know `about.tsx` is reachable at `/about`?
