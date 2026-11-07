# Tickets

Small, numbered steps. Each one teaches something and leaves the project working.

## Where things are

```
tickets/
├── M0-setup/              APP-001 … APP-004
├── M1-python-basics/      APP-005 … APP-007
├── M2-python-project/     APP-008 … APP-012
├── M3-first-api/          APP-013 … APP-018
└── M4-first-mobile-app/   APP-019 … APP-026
```

The order across both repos (`llm-gateway` and `pawcite`) is in `../LEARNING-PATH.md`.
Progress is ticked in `../ROADMAP.md`. Tickets for later milestones are written when you get there,
so they can build on what you have learned.

## Ticket format

Every ticket has a header (read by `scripts/create_issues.py`) and the same sections:

| Section | What it holds |
|---|---|
| Header | `id`, `title`, `milestone`, `labels`, `size`, `depends_on` |
| Goal | The result, in one or two sentences |
| Why it matters | How this fits the PawCite app |
| You will learn | The new concepts, with JavaScript comparisons |
| Steps | Small, ordered steps |
| Acceptance criteria | Checkboxes that must all be true |
| Explain it back | Questions to answer before closing the ticket |
| Notes for the AI | Extra instructions for the coding assistant (optional) |

## Sizes and labels

- **S**: about an hour or less. **M**: one to two hours.
- `hands-on`: **you** write the code; the AI explains, hints and reviews.
- Other labels describe the area: `python`, `api`, `llm`, `mobile`, `database`, `testing`, `ci`, `docker`, `setup`, `ai`, `learning`.

## How to work on a ticket

1. In Claude Code: `/start-ticket APP-005` (or say "start APP-005").
2. Follow the steps with the AI; ask `/explain <topic>` whenever something is unclear.
3. `/review` before opening the pull request.
4. The pull request says `Closes #<issue>`; merging moves the card to Done.
5. `/quiz` for the "Explain it back" questions, then add your notes to `docs/learning-log.md`.

## Definition of done

- All acceptance criteria are ticked, with evidence in the pull request.
- Checks pass locally and in CI (from APP-011 on for Python, APP-023 for mobile).
- You can answer the "Explain it back" questions without looking.
