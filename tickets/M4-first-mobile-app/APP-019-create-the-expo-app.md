---
id: APP-019
title: Create the Expo app and open it on your phone
milestone: APP-M4 · First mobile app
labels: mobile, setup
size: S (about 45 min)
depends_on: APP-018
---

# APP-019 · Create the Expo app and open it on your phone

## Goal
A new Expo app in `mobile/` runs on your own phone through Expo Go.

## Why it matters
This is the app you will carry around and use.

## You will learn
- Expo: tools and services on top of React Native, so you write React (TypeScript) and get native
  iOS and Android apps.
- Expo Go: an app from the App Store / Play Store that runs your project during development,
  with no build step.
- Metro: the bundler and dev server (≈ Vite's dev server).

## Steps
1. From the repo root: `npx create-expo-app@latest mobile`
2. If a `mobile/.git` folder was created, delete it: the app lives inside this repo, not its own.
3. `cd mobile && npx expo start`
4. Install **Expo Go** on your phone and scan the QR code (phone and laptop on the same Wi-Fi;
   if it cannot connect, try `npx expo start --tunnel`).
5. Change a text on the home screen, save, and watch the phone update.

## Acceptance criteria
- [ ] The app runs on your phone.
- [ ] Saving a change updates the phone within a few seconds.
- [ ] There is no nested `.git` folder inside `mobile/`.

## Explain it back
1. What is the difference between Expo Go and a real app build?
