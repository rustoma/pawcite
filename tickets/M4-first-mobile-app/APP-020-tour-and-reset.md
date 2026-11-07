---
id: APP-020
title: Tour the project and reset it
milestone: APP-M4 · First mobile app
labels: mobile, learning
size: S (about 45 min)
depends_on: APP-019
---

# APP-020 · Tour the project and reset it

## Goal
You understand how the template is organised, then reset it to a clean starting point.

## You will learn
- Expo Router: files in `src/app/` are screens, and the file path is the route
  (≈ the Next.js App Router).
- `_layout.tsx` wraps the screens in a folder (navigation, themes).
- React Native primitives: `View` (≈ `div`), `Text` (all text must be inside one), no CSS files.

## Steps
1. With the AI, read `src/app/_layout.tsx`, `src/app/index.tsx` and `src/app/explore.tsx`.
   Ask how the tabs are created.
2. Run `npm run reset-project` and answer **Y** to keep the example in an `example/` folder.
3. Look at the new, minimal `src/app/index.tsx` and `_layout.tsx`.
4. Commit: `APP-020: reset Expo template`.

## Acceptance criteria
- [ ] The app shows the minimal starting screen.
- [ ] You can explain how a file in `src/app/` becomes a screen.

## Explain it back
1. What happens if you put a plain string directly inside a `View`?
