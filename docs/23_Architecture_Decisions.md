# 23 Architecture Decisions

> Status: Draft. Introduced in Phase 0.

## Purpose

This document defines how VoiceOS records architectural decisions, provides the template, and holds the initial decision log.

## Goals

- Make the reasoning behind significant decisions durable and searchable.
- Separate decisions that are made from decisions that are still open.
- Provide a consistent, lightweight format.

## Table of Contents

- [What Is an ADR](#what-is-an-adr)
- [When to Write One](#when-to-write-one)
- [Lifecycle](#lifecycle)
- [Template](#template)
- [Decision Log](#decision-log)
- [Initial Decisions](#initial-decisions)
- [Open Decisions](#open-decisions)
- [Future Expansion Points](#future-expansion-points)
- [Related Documents](#related-documents)

## What Is an ADR

An Architecture Decision Record captures a single significant decision: its context, the options considered, the choice, and its consequences. ADRs are short, immutable once accepted, and superseded rather than edited when circumstances change.

## When to Write One

- A choice that is costly to reverse, such as a core framework or storage model.
- A choice that affects multiple subsystems or the public interface.
- A choice between genuinely competing options.
- Adopting or removing a significant dependency.
- Any major architectural change, which requires owner approval before implementation.

Routine implementation choices do not need an ADR.

## Lifecycle

| Status | Meaning |
| --- | --- |
| Proposed | Under discussion; not yet binding |
| Accepted | Decided and binding |
| Superseded | Replaced by a later ADR, which is referenced |
| Rejected | Considered and not adopted; kept so the reasoning is not lost |

## Template

```markdown
# ADR-NNNN Title

- Status: Proposed | Accepted | Superseded by ADR-NNNN | Rejected
- Date: YYYY-MM-DD
- Deciders: names or roles

## Context
The situation, constraints, and forces that require a decision.

## Options Considered
Each option with its advantages and disadvantages.

## Decision
The choice made, stated clearly.

## Consequences
What becomes easier, what becomes harder, and what must follow.

## Related
Links to affected documents and other ADRs.
```

Each ADR is a separate file, numbered sequentially, and listed in the decision log below.

## Decision Log

| ID | Title | Status |
| --- | --- | --- |
| ADR-0001 | Record architecture decisions | Accepted |
| ADR-0002 | Backend in Python with FastAPI and AsyncIO | Accepted |
| ADR-0003 | Client in React and TypeScript | Accepted |
| ADR-0004 | Provider abstraction for external capabilities | Accepted |
| ADR-0005 | LangGraph for conversation orchestration | Accepted |
| ADR-0006 | Initial providers: faster-whisper, Gemini, Edge TTS, FAISS | Accepted |
| ADR-0007 | SQLite as the initial persistence store | Accepted |
| ADR-0008 | WebRTC for audio transport, with WebSockets for control | Accepted |

The individual ADR files for these entries are written in Phase 1, using the summaries below as their starting context.

## Initial Decisions

These decisions were made by the project owner before Phase 0 documentation began.

- **ADR-0001:** Decisions are recorded in ADRs so reasoning survives turnover and time.
- **ADR-0002:** FastAPI and AsyncIO fit the real-time, I/O-bound workload. See [05_Tech_Stack.md](05_Tech_Stack.md).
- **ADR-0003:** React with TypeScript for the browser client.
- **ADR-0004:** All external capabilities sit behind contracts so that providers are replaceable without changing business logic. See [09_Low_Level_Design.md](09_Low_Level_Design.md).
- **ADR-0005:** LangGraph provides explicit, stateful workflows. Workflow code is isolated in the orchestration layer.
- **ADR-0006:** The initial provider set minimizes setup cost; each is expected to be replaceable.
- **ADR-0007:** SQLite is sufficient for early, single-instance use; migration to PostgreSQL is anticipated and must not require business logic changes.
- **ADR-0008:** WebRTC for real-time audio, WebSockets for control events. The server-side WebRTC approach is a separate open decision.

## Open Decisions

To be resolved in Phase 1, each through a proposed ADR:

- Repository layout, including single versus multiple repositories ([06_Project_Structure.md](06_Project_Structure.md)).
- Server-side WebRTC approach and signaling channel ([12_WebRTC.md](12_WebRTC.md), [10_API_Design.md](10_API_Design.md)).
- Ownership of speech boundary detection ([13_Speech_to_Text.md](13_Speech_to_Text.md)).
- Prompt storage and loading ([14_LLM.md](14_LLM.md)).
- Boundary between LangGraph memory facilities and VoiceOS repositories ([16_Memory.md](16_Memory.md)).
- Scope of long-term memory in the MVP.
- Adoption and scope of MCP ([17_Tool_Calling.md](17_Tool_Calling.md)).
- Ordering of the audio and AI pipeline phases ([04_Product_Roadmap.md](04_Product_Roadmap.md)).
- API conventions: casing and error code taxonomy ([10_API_Design.md](10_API_Design.md)).

## Future Expansion Points

- Individual ADR files in a dedicated folder, with an automated index.
- A review checklist for proposed ADRs.
- Links from code modules to the ADRs that shaped them.

## Related Documents

[04_Product_Roadmap.md](04_Product_Roadmap.md), [05_Tech_Stack.md](05_Tech_Stack.md), [22_Engineering_Principles.md](22_Engineering_Principles.md)
