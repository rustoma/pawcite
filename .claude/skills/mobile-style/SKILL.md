---
name: mobile-style
description: Rules for writing or changing the Expo app in mobile/ — Expo Router, TypeScript strict, React Native patterns, the EXPO_PUBLIC secret rule and the safety copy. Use before editing any file under mobile/.
---

# Mobile style

Expo SDK 58 with Expo Router, TypeScript strict. The app exists from APP-019.

## Layout

```
mobile/
  src/app/            routes — the file tree IS the navigation
    _layout.tsx       the stack
    index.tsx         the Ask screen
    about.tsx         About and safety
  src/components/     shared components
  src/api/            generated client (APP-025)
  app.json
```

Routes live in `src/app/`, not `app/` — that is the SDK 58 template. `npm run reset-project`
clears the example screens.

If `create-expo-app` leaves a nested `mobile/.git`, delete it. One repo, one `.git`.

## TypeScript

- `strict: true`. **No `any`** — not in props, not in a `catch`, not "temporarily".
- An unknown error is `unknown`; narrow it before using it.
- Props get a named type, not an inline object literal, once they have more than two fields.
- From APP-025 the API types are **generated from the OpenAPI schema**. Do not hand-write a type
  that mirrors a response; regenerate instead, so a changed endpoint breaks the build rather than
  the app.

## Secrets — the rule that bites

`EXPO_PUBLIC_*` variables are **bundled into the app binary** and readable by anyone who
downloads it. They are public strings, not configuration.

- `EXPO_PUBLIC_API_URL` — fine, it is a URL.
- An API key, a gateway key, a token, a database URL — **never**, under any name.

The phone talks to **your FastAPI API**. The API holds the gateway key. The app never holds a
model-provider or gateway credential, and never calls the gateway directly.

On a physical phone, `localhost` is the phone. Use the LAN address of your machine
(`http://192.168.x.x:8000`) and make sure the API listens on `0.0.0.0` (APP-024).

## React Native, not React DOM

- `View`, `Text`, `TextInput`, `Pressable`. There is no `div`, and **all text must be inside
  `<Text>`** or it throws.
- `StyleSheet.create`, not CSS. No cascade, no `className`, no units — numbers are
  density-independent pixels.
- Flexbox default direction is **`column`**, not `row`. This is the single most common surprise.
- `Pressable` over `TouchableOpacity` for new code.
- Wrap screens with a text input in `KeyboardAvoidingView` so the keyboard cannot cover it.
- Long content goes in a `ScrollView` or `FlatList`; a `View` does not scroll.

## State and data

`useState` for screen state. No state library until something actually needs it.

Every request has three visible states: **loading**, **error**, **result**. An Ask button that
does nothing visible for four seconds is a bug, not a detail. Disable the button while a request
is in flight, and keep the client-side rules in step with the API (the question minimum is 3
characters in both — the app for instant feedback, the API because it is the real boundary).

Show a real message on failure ("Could not reach the API"), never a swallowed error.

## Safety on screen

The same product rule as the API, visible to the user:

- The About screen says plainly that PawCite summarises published research and **does not
  diagnose dogs or give medication doses**.
- Answers carry that framing; an emergency answer says "contact a vet now" first, before anything
  else, and nothing on screen competes with it.

## Checks

From `mobile/`, both must pass before a pull request:

```bash
npx tsc --noEmit && npm run lint
```

For mobile tickets, the pull-request evidence is a **screenshot** from a real device or simulator
— `tsc` passing proves nothing about whether the keyboard covers the input.

## Naming

`PascalCase.tsx` for components, `camelCase.ts` for everything else. Route files are lowercase,
because the filename becomes the URL segment: `about.tsx` → `/about`.
