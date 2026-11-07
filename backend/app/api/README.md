# api

HTTP entry points. Modules here translate requests into calls on inner layers and results back into responses. They contain no business logic.

Currently holds the `/health` liveness endpoint. Conventions for future interfaces are in `docs/10_API_Design.md`.
