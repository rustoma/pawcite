---
id: APP-024
title: Connect the app to your API
milestone: APP-M4 · First mobile app
labels: mobile, api
size: M (about 1.5 h)
depends_on: APP-023
---

# APP-024 · Connect the app to your API

## Goal
Tapping Ask sends the question to your Python API (running on your laptop) and shows the real
answer, with loading and error states.

## Why it matters
The whole chain works for the first time: phone → API → gateway → model.

## You will learn
- Your phone cannot use `localhost` (that is the phone itself); it needs your laptop's network address.
- `EXPO_PUBLIC_*` variables are **bundled into the app**: fine for a URL, never for a secret.
- Loading, error and empty states for a network call.

## Steps
1. Run the API on all network interfaces:
   `uv run fastapi dev api/src/pawcite_api/main.py --host 0.0.0.0`
2. Find your laptop's local IP address (for example `192.168.1.20`).
3. `mobile/.env`: `EXPO_PUBLIC_API_URL=http://192.168.1.20:8000` (git-ignored).
4. Create `src/api/client.ts` with `askQuestion(question: string)` using `fetch`.
5. On the Ask screen: show a spinner while waiting, the answer when it arrives, and a friendly
   error if the API is unreachable.
6. Try the chocolate question from APP-018 on your phone.

## Acceptance criteria
- [ ] A question typed on the phone shows the model's answer.
- [ ] With the API stopped, the app shows a friendly error instead of crashing.

## Explain it back
1. Why can't the phone reach `http://localhost:8000`?
2. What would happen if you put an API key in an `EXPO_PUBLIC_` variable?

## Notes for the AI
If the phone cannot connect, check firewall settings on the laptop and that both devices are on
the same network. Android emulators use `10.0.2.2` to reach the host.
