---
description: Start work on a ticket - read it, check dependencies, branch, explain the new concepts
argument-hint: <ticket-id, e.g. APP-013>
---

Start ticket **$1**.

Follow the `ticket-workflow` skill (`.claude/skills/ticket-workflow/SKILL.md`), section 1 and 2:

1. Find and read the whole ticket file under `tickets/` for $1 — every section, including
   "Notes for the AI".
2. Check `depends_on` against `ROADMAP.md`. If a dependency is unticked, say so and stop before
   touching anything. Dependencies on `GW-*` tickets live in the `llm-gateway` repo — ask rather
   than assume.
3. Find the GitHub issue number: `gh issue list --search "$1" --state all`.
4. Create the branch from an up-to-date `main`, named `<lowercase-id>-<slug>`.
5. Tell me, in three or four lines: what will exist when this is done, which files change, and
   which concepts you are going to explain first.
6. If the ticket's "You will learn" names anything new to this repo, explain it now with the
   `tutor` skill — before the first edit.
7. If the ticket is labelled `hands-on`, say so explicitly and remember that **I** write the
   code. You explain, hint and review.

Then wait for me before writing anything.
