# Roadmap

Tick a ticket when its pull request is merged. Later milestones list planned tickets; their
detailed files are written when you reach them.

## APP-M0 · Setup
- [ ] APP-001 Create the repository on GitHub
- [ ] APP-002 Connect your AI assistant to this repo
- [ ] APP-003 Install uv and Python 3.14
- [ ] APP-004 Create issues and add them to the board

## APP-M1 · Python basics
- [ ] APP-005 Values, functions, collections *(hands-on)*
- [ ] APP-006 Classes, errors, modules *(hands-on)*
- [ ] APP-007 Type hints and async *(hands-on)*

## APP-M2 · Python project
- [ ] APP-008 Create the Python workspace
- [ ] APP-009 Ruff, mypy and pytest
- [ ] APP-010 Run checks before every commit
- [ ] APP-011 CI for Python
- [ ] APP-012 PostgreSQL with pgvector in docker compose

## APP-M3 · First API
- [ ] APP-013 Hello FastAPI
- [ ] APP-014 Request and response models
- [ ] APP-015 Test the API
- [ ] APP-016 Settings and secrets
- [ ] APP-017 Your first LLM call through the gateway
- [ ] APP-018 Answer questions with the LLM (no papers yet)

## APP-M4 · First mobile app
- [ ] APP-019 Create the Expo app and open it on your phone
- [ ] APP-020 Tour the project and reset it
- [ ] APP-021 The Ask screen *(hands-on)*
- [ ] APP-022 About and safety screen
- [ ] APP-023 Type checks, lint and CI for the app
- [ ] APP-024 Connect the app to your API
- [ ] APP-025 A typed API client from OpenAPI
- [ ] APP-026 Milestone demo: ask from your phone

---

## Planned (tickets written later)

### APP-M5 · Papers in
Search Europe PMC · store paper metadata (SQLAlchemy and Alembic) · download open-access full
text and record licences · parse the XML into sections · chunk sections · embeddings through the
gateway · an ingestion worker (Procrastinate)

### APP-M6 · Answers with citations
Vector search · full-text search · hybrid search · prompts with sources · citations in the API ·
citations in the app (tap to open the paper) · streaming answers to the phone

### APP-M7 · Paper cards and evidence badges
Extract study type, species, sample size and limitations per paper · batch processing ·
evidence badges in answers and in the app

### APP-M8 · Evals in Python
Golden set of questions · retrieval metrics · LLM judges (faithfulness, overstating evidence) ·
human labels (optional FastAPI labeling tool) · calibration · CI gate

### APP-M9 · Accounts and limits
Better Auth service with email codes · the app signs in · FastAPI verifies tokens · daily
question limits · account deletion

### APP-M10 · Research agent and digests
LangGraph agent with Postgres checkpointing · weekly digest per topic · push notifications ·
deep-research mode with approval

### APP-M11 · Observability and deployment
OpenTelemetry traces from the app through the gateway · Terraform using the gateway's module ·
deploy-and-destroy on AWS

### APP-M12 · Safety and red-teaming
Safety test suite (no doses, no diagnosis, emergencies to a vet) · prompt-injection tests with
planted papers · CI gate

### APP-M13 · Distillation
Training data from the paper-card extractor · LoRA fine-tuning on a rented GPU · served behind
the gateway · evaluated against the large model
