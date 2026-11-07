# 05 Tech Stack

> Status: Draft. Introduced in Phase 0.

## Purpose

This document records each technology in the stack, why it was selected, the alternatives, the trade-offs, and the likely replacement path. Provider-facing technologies are expected to be replaceable behind interfaces defined in [09_Low_Level_Design.md](09_Low_Level_Design.md).

## Goals

- Justify each technology in terms of project requirements.
- Make trade-offs and replacement paths explicit.
- Distinguish technologies adopted initially from those adopted only when a need appears.

## Table of Contents

- [Summary](#summary)
- [FastAPI](#fastapi)
- [React](#react)
- [TypeScript](#typescript)
- [WebRTC](#webrtc)
- [LangGraph](#langgraph)
- [Gemini](#gemini)
- [Whisper](#whisper)
- [FAISS](#faiss)
- [SQLite](#sqlite)
- [Redis](#redis)
- [PostgreSQL](#postgresql)
- [Docker](#docker)
- [GitHub Actions](#github-actions)
- [Additional Initial Components](#additional-initial-components)
- [Future Expansion Points](#future-expansion-points)
- [Related Documents](#related-documents)

## Summary

| Technology | Role | Adoption |
| --- | --- | --- |
| FastAPI | Backend framework | Initial |
| React | Frontend library | Initial |
| TypeScript | Frontend language | Initial |
| WebRTC | Real-time audio transport | Initial |
| LangGraph | Conversation orchestration | Initial |
| Gemini | LLM provider | Initial, replaceable |
| Whisper (faster-whisper) | STT provider | Initial, replaceable |
| FAISS | Vector search | Initial, replaceable |
| SQLite | Persistence | Initial, replaceable |
| Redis | Shared state and coordination | When a need appears |
| PostgreSQL | Persistence at scale | When SQLite no longer suffices |
| Docker | Packaging | Phase 7 |
| GitHub Actions | CI/CD | When the repository has code to verify |

## FastAPI

- **Why selected:** Native async support, type-driven request validation, WebSocket support, and a mature ecosystem. It matches the async-first requirement.
- **Alternatives:** Starlette directly, Django, Flask, Litestar, Node.js frameworks.
- **Trade-offs:** Less built-in structure than full-stack frameworks, so project structure discipline falls to the team. Async code requires care to avoid blocking the event loop.
- **Future replacements:** Unlikely. Business logic stays framework-independent, which limits the cost if this changes.

## React

- **Why selected:** Large ecosystem, widespread familiarity among contributors, and good fit for a component-based real-time interface.
- **Alternatives:** Vue, Svelte, Solid, plain web components.
- **Trade-offs:** More configuration and ecosystem churn than a smaller library; state management choices need discipline.
- **Future replacements:** The client is a thin layer over the backend protocol, so alternative clients are possible without backend changes.

## TypeScript

- **Why selected:** Static typing for protocol messages and component contracts reduces integration errors in a real-time client.
- **Alternatives:** JavaScript with JSDoc types.
- **Trade-offs:** Build tooling overhead and a learning curve for contributors unfamiliar with it.
- **Future replacements:** None expected.

## WebRTC

- **Why selected:** Purpose-built for low-latency, bidirectional media in browsers, with NAT traversal and codec support. Detail in [12_WebRTC.md](12_WebRTC.md).
- **Alternatives:** Audio over WebSockets, WebTransport, hosted real-time media platforms.
- **Trade-offs:** Substantially more complex than WebSockets, with signaling and network traversal concerns, and more demanding infrastructure for production.
- **Future replacements:** Transport sits behind a boundary so that a media server or hosted platform can replace direct peer handling.

## LangGraph

- **Why selected:** Explicit graph-based workflows with state, branching, and checkpointing, suited to conversations that include retrieval, tools, and conditional paths.
- **Alternatives:** Plain async code, LangChain chains and agents, custom state machines, other orchestration libraries.
- **Trade-offs:** Adds a dependency and a programming model contributors must learn. The workflow must not leak into provider or API layers.
- **Future replacements:** Workflow definitions are isolated in the orchestration layer so that the engine can change without affecting providers.

## Gemini

- **Why selected:** Capable model family with an accessible API, suitable as the initial LLM provider.
- **Alternatives:** OpenAI, Anthropic, open-weight models served locally or through hosting providers.
- **Trade-offs:** Hosted dependency with its own latency, quotas, pricing, and data-handling terms. Behavior differences across providers affect prompts and tool calling.
- **Future replacements:** Expected and designed for. See [14_LLM.md](14_LLM.md).

## Whisper

The initial STT provider is faster-whisper, a reimplementation of OpenAI's Whisper model intended for efficient local inference.

- **Why selected:** Runs locally, avoiding external API dependence and data transfer during development; good multilingual coverage.
- **Alternatives:** Deepgram, AssemblyAI, Sarvam, cloud provider STT services.
- **Trade-offs:** Whisper is not natively a streaming recognizer, so low-latency behavior depends on how audio is segmented. Local inference consumes compute. Detail in [13_Speech_to_Text.md](13_Speech_to_Text.md).
- **Future replacements:** Hosted streaming providers are the expected alternative.

## FAISS

- **Why selected:** Fast, widely used similarity search library with no server to operate.
- **Alternatives:** Pinecone, Qdrant, Weaviate, pgvector, Chroma.
- **Trade-offs:** FAISS is a library, not a database. Metadata, filtering, persistence, and multi-process access must be handled around it.
- **Future replacements:** A managed or server-based vector store when scale or filtering needs exceed the library approach. See [15_RAG.md](15_RAG.md).

## SQLite

- **Why selected:** Zero-configuration, file-based, sufficient for early development and single-instance operation.
- **Alternatives:** PostgreSQL, MySQL.
- **Trade-offs:** Limited write concurrency and no network access, which constrains multi-instance deployment.
- **Future replacements:** PostgreSQL, with persistence accessed through an abstraction so that the move does not affect business logic.

## Redis

- **Why selected:** Not part of the initial stack. Listed because multi-instance operation introduces needs it commonly serves: shared session state, coordination, caching, and rate limiting.
- **Alternatives:** Database-backed coordination, in-process state for single-instance operation, other stores.
- **Trade-offs:** Another service to operate; adopting it before multi-instance operation is premature.
- **Future replacements:** Not applicable until adopted. Adoption requires an ADR.

## PostgreSQL

- **Why selected:** Not part of the initial stack. It is the expected successor to SQLite when concurrency, multi-instance deployment, or operational requirements outgrow it.
- **Alternatives:** Other relational or managed databases.
- **Trade-offs:** Operational overhead compared with SQLite.
- **Future replacements:** Adoption requires an ADR and a migration path.

## Docker

- **Why selected:** Reproducible environments and a standard deployment unit. Planned for Phase 7, though contributors may use it earlier.
- **Alternatives:** Virtual environments with documented setup, other container runtimes, platform-specific packaging.
- **Trade-offs:** Real-time audio and GPU-dependent components add networking and device configuration considerations.
- **Future replacements:** Not expected.

## GitHub Actions

- **Why selected:** Integrated with the repository host, widely understood, and sufficient for lint, test, and build pipelines.
- **Alternatives:** Other CI services.
- **Trade-offs:** Tied to the repository host.
- **Future replacements:** Pipeline definitions should stay simple enough to port.

## Additional Initial Components

- **Edge TTS:** initial TTS provider; accessible without an account, but an informal integration with no service guarantee. Replacement candidates are in [18_Text_to_Speech.md](18_Text_to_Speech.md).
- **WebSockets:** control events and signaling; see [10_API_Design.md](10_API_Design.md).
- **AsyncIO:** concurrency model across the backend.

## Future Expansion Points

- A dependency policy table recording version, license, and justification for each dependency.
- Benchmark results comparing providers per layer.
- Records of technologies evaluated and rejected.

## Related Documents

[06_Project_Structure.md](06_Project_Structure.md), [09_Low_Level_Design.md](09_Low_Level_Design.md), [22_Engineering_Principles.md](22_Engineering_Principles.md), [23_Architecture_Decisions.md](23_Architecture_Decisions.md)
