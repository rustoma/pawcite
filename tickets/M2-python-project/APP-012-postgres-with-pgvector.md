---
id: APP-012
title: PostgreSQL with pgvector in docker compose
milestone: APP-M2 · Python project
labels: database, docker
size: S (about 45 min)
depends_on: APP-011
---

# APP-012 · PostgreSQL with pgvector in docker compose

## Goal
`docker compose up -d db` starts PostgreSQL with the pgvector extension, ready for papers and embeddings.

## Why it matters
Papers, chunks, embeddings and users will all live here.

## You will learn
- pgvector stores vectors in a normal table column and finds the nearest ones.
- `<=>` is cosine distance: smaller means more similar.

## Steps
1. Create `compose.yaml` at the repo root with a `db` service: image `pgvector/pgvector:pg17`,
   user/password/database `pawcite`, a named volume, port `5432`, and a health check
   (`pg_isready -U pawcite`).
2. `docker compose up -d db`, then `docker compose exec db psql -U pawcite`.
3. In psql:
   ```sql
   CREATE EXTENSION IF NOT EXISTS vector;
   CREATE TABLE topics (name text, embedding vector(3));
   INSERT INTO topics VALUES ('leash training', '[0.9,0.1,0.0]'),
                             ('puppy sleep', '[0.1,0.9,0.1]'),
                             ('recall training', '[0.8,0.2,0.1]');
   SELECT name, embedding <=> '[1,0,0]' AS distance FROM topics ORDER BY distance;
   ```
4. Stop and start the container; check the data is still there (the volume).
5. Drop the practice table.

## Acceptance criteria
- [ ] The query lists the two training topics before "puppy sleep".
- [ ] Data survives a container restart.

## Explain it back
1. Why did the training topics come first?
2. What keeps the data when the container is removed?
