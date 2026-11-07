---
name: ticket-workflow
description: The loop for starting, working on and finishing a ticket in tickets/. Use when the human says "start APP-013", runs /start-ticket or /next, asks what to work on, or is ready to open a pull request for the current ticket.
---

# Ticket workflow

One ticket at a time. One ticket = one branch = one pull request.

## 1. Start

1. **Read the whole ticket file** before doing anything: `tickets/<milestone>/<ID>-<name>.md`.
   Every section, including "Notes for the AI".
2. **Check `depends_on`.** If a dependency is not ticked in `ROADMAP.md`, say so and stop.
   Some pawcite tickets depend on `llm-gateway` tickets (APP-001 on GW-020, APP-017 on a running
   gateway) — those live in the other repo, so ask rather than guess.
3. **Find the GitHub issue**: `gh issue list --search "APP-013" --state all`. The title is
   `[APP-013] Hello FastAPI`. You will need its number for the pull request.
4. **Branch from an up-to-date base:**
   ```bash
   git switch main && git pull && git switch -c app-013-hello-fastapi
   ```
   Branch name = lowercase ID + short slug from the title.
5. **Say the plan in three or four lines**: what will exist when this is done, which files, and
   which concepts need explaining first.

## 2. Explain before you write

If the ticket's "You will learn" names a concept that has not appeared in this repo, use the
[tutor](../tutor/SKILL.md) skill **now**, before the first edit. Do not explain a concept inside
a code comment and call it explained.

## 3. Do the work

**Check the labels first.**

- **`hands-on`** — the human writes the code. You explain, hint, point at the right docs, and
  review what they wrote. You do **not** write the solution, not even "to show the shape", unless
  they say "show me the solution" in those words. If they are stuck, narrow the hint: name the
  function, then its signature, then one line of it. Never the whole thing.
- **Every other ticket** — you write the code, in small pieces, saying what each piece does.
  Follow [python-style](../python-style/SKILL.md) or [mobile-style](../mobile-style/SKILL.md).

Work the Steps in order. They are sized so that each one leaves the project runnable.

## 4. Done means done

Before you say a ticket is finished, **every acceptance criterion must be met and shown**. Run
the checks and paste the real output:

```bash
# Python, from python/
uv run ruff check . && uv run ruff format --check . && uv run mypy && uv run pytest
```

```bash
# Mobile, from mobile/
npx tsc --noEmit && npm run lint
```

Checks exist from APP-011 (Python CI) and APP-023 (mobile CI); before those, run what exists.

Never tick a box you have not verified. "Should work" is not evidence. If one criterion cannot be
met, say which, why, and what you did instead — do not quietly drop it.

## 5. Pull request

Commit in small, readable steps; the subject line is imperative and under 72 characters.

```bash
git push -u origin app-013-hello-fastapi
gh pr create --title "APP-013 · Hello FastAPI" --body "Closes #13 ..."
```

The title carries the ticket id. The body must contain:

- `Closes #13` (the issue number), so merging closes the issue and moves the board card.
- The acceptance criteria as a checklist, ticked, with the evidence (command output, a screenshot
  for mobile tickets).
- One line on anything you decided that the ticket did not specify.

Keep it small. If the diff has grown past the ticket, split it rather than explaining it away.

Run the [code-review](../code-review/SKILL.md) skill on the branch before opening the PR.

## 6. Finish with "Explain it back"

After the PR is open (or merged), ask the ticket's "Explain it back" questions **one at a time**.
Wait for a real answer to each. Correct gently; if an answer is vague, ask the follow-up rather
than supplying the answer.

Then:

1. Add **2–3 bullets** to `docs/learning-log.md`, in the human's own words, under the ticket ID.
2. Tick the ticket in `ROADMAP.md`.

Both of those go in the same PR, or a tiny follow-up commit on `main` if the PR is already merged.

## 7. Next

`/next` reads `LEARNING-PATH.md` and `ROADMAP.md` and finds the first unticked ticket whose
`depends_on` is satisfied. Remember the path crosses repos: parts 1, 2, 5 and 7 are in
`llm-gateway`, parts 3, 4 and 6 are here.

## Never

- Work two tickets on one branch.
- Mark a ticket done with failing or unrun checks.
- Write the code on a `hands-on` ticket unless asked in words.
- Commit secrets, `.env`, or anything matching `.gitignore`.
