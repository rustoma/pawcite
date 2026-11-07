---
id: APP-021
title: The Ask screen
milestone: APP-M4 · First mobile app
labels: mobile, hands-on
size: M (about 1.5 h)
depends_on: APP-020
---

# APP-021 · The Ask screen

## Goal
The home screen has a question box and an Ask button, and shows the question below after tapping.

## Why it matters
This is the main screen of the app.

## You will learn
- `TextInput`, `Pressable` and `useState` in React Native.
- Styling with `StyleSheet.create` and flexbox (the default direction is **column**).
- `KeyboardAvoidingView`, so the keyboard does not cover the input.

## Steps
1. In `src/app/index.tsx`: a title, a multi-line `TextInput`, an Ask button and a result area.
2. Disable the button while the question has fewer than 3 characters (the same rule as the API).
3. On tap, show "You asked: …" below the button.
4. Wrap the screen in `KeyboardAvoidingView`.
5. Try it on your phone, including with the keyboard open.

## Acceptance criteria
- [ ] The button is disabled for short questions and enabled from 3 characters.
- [ ] The keyboard never hides the input.

## Explain it back
1. Why check the 3-character rule in the app if the API checks it too?

## Notes for the AI
Hands-on: the human writes the screen. Help with React Native differences from React DOM.
