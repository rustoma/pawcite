---
description: Find the next ticket whose dependencies are done
---

Work out what I should do next.

1. Read `LEARNING-PATH.md` (the order across both repos) and `ROADMAP.md` (what is ticked here).
2. Cross-check against GitHub: `gh issue list --state all --limit 100 --json number,title,state`
   — a merged pull request closes its issue, so a closed issue means done even if `ROADMAP.md`
   was not ticked. If they disagree, tell me which and offer to fix `ROADMAP.md`.
3. Find the first unticked ticket whose `depends_on` is satisfied.
4. Remember the path crosses repos: parts 1, 2, 5 and 7 are in `llm-gateway`, parts 3, 4 and 6 are
   here in `pawcite`. If the next ticket is a `GW-*` one, say so and tell me to switch repos
   rather than trying to start it here.

Then tell me, briefly:

- The ticket ID, title and size.
- Its one-sentence Goal.
- What it needs that I may not have installed yet.
- Whether it is `hands-on` (I write the code) or not.

Do not start it. If I want to, I will say `/start-ticket <id>`.
