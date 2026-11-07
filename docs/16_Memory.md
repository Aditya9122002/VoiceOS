# 16 Memory

> Status: Draft. Introduced in Phase 0. The scope of long-term memory in the MVP is an open decision.

## Purpose

This document describes how VoiceOS retains conversation context: short-term memory, long-term memory, the role of LangGraph's memory features, and checkpointing.

## Goals

- Distinguish the kinds of memory and their lifetimes.
- Define how memory fits the workflow without coupling it to storage.
- Address privacy and retention from the start.

## Table of Contents

- [Role in the System](#role-in-the-system)
- [Short-Term Memory](#short-term-memory)
- [Long-Term Memory](#long-term-memory)
- [LangGraph Memory](#langgraph-memory)
- [Checkpointing](#checkpointing)
- [Context Budget](#context-budget)
- [Privacy and Retention](#privacy-and-retention)
- [Voice-Specific Considerations](#voice-specific-considerations)
- [Future Expansion Points](#future-expansion-points)
- [Related Documents](#related-documents)

## Role in the System

Memory lets the agent stay coherent within a conversation and, optionally, across conversations. The Memory subsystem provides context to the Orchestrator and persists through repository contracts.

## Short-Term Memory

Short-term memory is the history of the current session: user turns, agent turns, and tool interactions. Considerations:

- It is the primary source of conversational continuity.
- It grows without bound unless managed; strategies include keeping recent turns verbatim and summarizing older ones.
- It records what the user actually heard, which differs from what was generated when the user interrupts.

## Long-Term Memory

Long-term memory persists information across sessions, such as user preferences or facts established earlier. Considerations:

- Deciding what is worth remembering is a design problem; storing everything is neither useful nor safe.
- Remembered items need provenance and the ability to be corrected and deleted.
- Recall may use retrieval techniques similar to [15_RAG.md](15_RAG.md).
- Whether long-term memory is in the MVP is undecided; the architecture reserves a place for it without implementing it prematurely.

## LangGraph Memory

LangGraph distinguishes state that belongs to a single conversation thread from memory shared across threads. Thread state is saved through checkpointers. Cross-thread memory is provided by a store abstraction. VoiceOS intends to use these facilities within the orchestration layer while keeping memory storage behind VoiceOS's own repository contracts where practical, so that workflow and storage can each be replaced. The exact boundary is an open decision and should be validated against the current LangGraph documentation in Phase 1.

## Checkpointing

Checkpointing persists the workflow state at defined points so that a conversation can resume after interruption or restart. Considerations:

- Checkpoints enable recovery, inspection, and debugging of past turns.
- Checkpoint frequency trades durability against write overhead on the latency-sensitive path.
- Checkpoint storage must support the concurrency of the deployment; the initial store is SQLite and its limits are noted in [05_Tech_Stack.md](05_Tech_Stack.md).
- Checkpoints contain conversation content and fall under the same retention rules as history.

## Context Budget

Only part of memory can be sent to the model. A budget determines how much history and recalled memory is included, balancing coherence against latency and cost. Budget decisions are made in prompt assembly, see [14_LLM.md](14_LLM.md).

## Privacy and Retention

- Conversation content may be sensitive. Retention periods are defined and configurable.
- Users or operators can delete stored conversation data.
- Memory is scoped by tenant and user, and never shared across them.
- Sensitive categories are not stored without an explicit decision. See [21_Security.md](21_Security.md).

## Voice-Specific Considerations

- Transcripts contain recognition errors; storing them verbatim preserves errors.
- Interrupted responses are stored as delivered, not as generated.
- Session identity for voice may be weaker than for logged-in users, which affects how long-term memory is attributed.

## Future Expansion Points

- Summarization strategies and evaluation.
- Memory extraction and correction workflows.
- User-facing controls for viewing and deleting memory.
- Migration of checkpoint storage when persistence changes.

## Related Documents

[08_High_Level_Design.md](08_High_Level_Design.md), [14_LLM.md](14_LLM.md), [15_RAG.md](15_RAG.md), [21_Security.md](21_Security.md)
