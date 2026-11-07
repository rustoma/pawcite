---
description: Ask the current ticket's "Explain it back" questions, one at a time
argument-hint: <ticket-id, optional - defaults to the current branch>
---

Quiz me on **$ARGUMENTS** (if that is empty, work out the ticket from the current branch name).

1. Open that ticket file and find its "Explain it back" section.
2. Ask the questions **one at a time**. Ask the first one, then stop and wait for my answer.
3. Judge each answer:
   - Right: say so in one line, add the one detail I missed if there is one, move on.
   - Partly right: name the part that is right, then ask a narrowing follow-up. Do not hand me
     the answer.
   - Wrong or vague: correct it gently and concretely, with the "why", then re-ask in a different
     form later.
4. Do not reveal a later question while an earlier one is open, and never answer your own question
   in the same message you ask it.

When all the questions are done, draft **2–3 bullets for `docs/learning-log.md`** under this
ticket's ID — in my words from the answers I gave, not a summary of the ticket. Show me the
bullets, let me edit them, then write them to the file.
