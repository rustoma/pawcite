# PawCite

A dog-research assistant: ask a question about dogs and get an answer grounded in published
studies, with citations and an honest label for how strong the evidence is.

> **Status:** early. Built ticket by ticket as a learning project. See [ROADMAP.md](ROADMAP.md).
> PawCite shares research; it is not veterinary advice.

## Architecture

```
 Expo app (TypeScript)
        │  questions
        ▼
 API + RAG (Python, FastAPI) ──▶ llm-gateway (Go, separate repo) ──▶ model providers
        │
        ▼
 PostgreSQL + pgvector ◀── workers (Python): papers from Europe PMC, PubMed, OpenAlex
```

| Part | Technology | Folder |
|---|---|---|
| Mobile app | Expo, React Native, TypeScript | `mobile/` |
| API and RAG | Python 3.14, FastAPI, Pydantic, uv | `python/` |
| Model access | The Go gateway, through the OpenAI SDK | separate repo |
| Data | PostgreSQL with pgvector | `compose.yaml` |

## Working on this repo

- Start with [LEARNING-PATH.md](LEARNING-PATH.md) and the first ticket in [tickets/](tickets/).
- AI assistants follow [AGENTS.md](AGENTS.md); skills and commands are in [.claude/](.claude/).
- What I learned along the way: [docs/learning-log.md](docs/learning-log.md).
