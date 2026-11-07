# 06 Project Structure

> Status: Draft. The layout is proposed and requires owner approval in Phase 1 (see [23_Architecture_Decisions.md](23_Architecture_Decisions.md)).

## Purpose

This document explains the proposed repository layout, what belongs in each folder, and the conventions that apply across it.

## Goals

- Make the location of any piece of code predictable.
- Encode the dependency rules of the architecture in the folder layout.
- Keep the structure free of folders without a current purpose.

## Table of Contents

- [Principles](#principles)
- [Proposed Layout](#proposed-layout)
- [Folder Responsibilities](#folder-responsibilities)
- [Dependency Direction](#dependency-direction)
- [Coding Conventions](#coding-conventions)
- [Future Expansion Points](#future-expansion-points)
- [Related Documents](#related-documents)

## Principles

- Folders are created when they have content, not in anticipation.
- Every folder contains a README describing its purpose.
- Business logic does not import from provider or framework folders.

## Proposed Layout

```text
voiceos/
├── docs/            Documentation and decision records
├── backend/         Python backend
│   ├── app/
│   │   ├── api/             HTTP and WebSocket entry points
│   │   ├── core/            Configuration and shared foundations
│   │   ├── domain/          Entities and business rules
│   │   ├── services/        Application use cases
│   │   ├── pipeline/        Conversation workflow and voice pipeline stages
│   │   ├── providers/       Adapters for STT, LLM, TTS, vector store
│   │   ├── persistence/     Storage access
│   │   └── observability/   Logging, metrics, tracing
│   └── tests/
├── frontend/        React and TypeScript client
├── scripts/         Developer and maintenance scripts
├── deploy/          Deployment definitions (Phase 7)
└── .github/         Repository automation and templates
```

The backend subfolders correspond to the layers in [09_Low_Level_Design.md](09_Low_Level_Design.md).

## Folder Responsibilities

| Folder | Belongs here | Does not belong here |
| --- | --- | --- |
| docs | Design documents, ADRs, journal | Generated or temporary files |
| backend/app/api | Request and message handling, validation, serialization | Business rules, provider calls |
| backend/app/core | Configuration loading, shared constants, error types | Feature logic |
| backend/app/domain | Entities and rules independent of frameworks | Framework or provider imports |
| backend/app/services | Use cases that coordinate domain and ports | Transport or provider specifics |
| backend/app/pipeline | Workflow definition and pipeline stage coordination | Provider-specific code |
| backend/app/providers | One adapter per provider, grouped by capability | Business decisions |
| backend/app/persistence | Repositories and storage mapping | Business rules |
| backend/app/observability | Logging, metrics, tracing setup | Feature logic |
| backend/tests | Tests mirroring the application layout, with fake providers | Tests requiring live providers by default |
| frontend | Client application, audio handling, UI | Provider keys or business rules |
| scripts | Repeatable developer tasks | Application code |
| deploy | Container and environment definitions | Application code |

## Dependency Direction

Dependencies point inward: api and providers depend on services and domain; domain depends on nothing outside itself. Providers implement contracts defined by the inner layers, never the reverse. The full rule and enforcement approach are in [22_Engineering_Principles.md](22_Engineering_Principles.md).

## Coding Conventions

**General**

- Names state intent; avoid abbreviations that are not universal.
- Named constants replace magic numbers.
- Comments explain why, not what.
- Public modules, interfaces, and non-obvious decisions are documented.

**Backend**

- Type annotations on all public functions.
- Asynchronous by default for I/O; blocking work is isolated from the event loop.
- Dependencies are injected at a single composition root, not constructed inside business logic.
- Configuration comes from the environment through one configuration module.

**Frontend**

- TypeScript strict mode.
- Protocol message types are defined once and shared across components.
- Side effects such as audio and network access are isolated from presentational components.

**Repository**

- One logical change per commit, with a message that explains the reason.
- Architectural changes update documentation and ADRs in the same change.

## Future Expansion Points

- Decision on a single repository versus separate repositories for backend and frontend.
- A shared contracts location if client and server types need synchronization.
- Package boundaries if the backend is split into installable components.

## Related Documents

[05_Tech_Stack.md](05_Tech_Stack.md), [07_System_Architecture.md](07_System_Architecture.md), [09_Low_Level_Design.md](09_Low_Level_Design.md), [22_Engineering_Principles.md](22_Engineering_Principles.md)
