# 25 Interview Notes

> Status: Draft. Introduced in Phase 0.

## Purpose

This document collects interview questions that this project prepares the reader to answer, with the points a strong answer covers. It is a study aid and a way of checking understanding of the system's design.

## Goals

- Connect project decisions to commonly discussed engineering topics.
- Record the key points of a good answer, not scripted responses.
- Grow as the implementation produces real experience to draw on.

## Table of Contents

- [How to Use These Notes](#how-to-use-these-notes)
- [System Design Questions](#system-design-questions)
- [Backend Questions](#backend-questions)
- [Voice AI Questions](#voice-ai-questions)
- [LLM Questions](#llm-questions)
- [Project-Specific Questions](#project-specific-questions)
- [Future Expansion Points](#future-expansion-points)
- [Related Documents](#related-documents)

## How to Use These Notes

Answer each question aloud before reading the points. Refine answers using what was learned while building. Where an answer rests on a project decision, be ready to give the alternative considered and why it was not chosen.

## System Design Questions

**Design a real-time voice agent from browser to response.**
Cover the pipeline stages, streaming between stages, where state lives, latency accumulation, interruption, and failure behavior. See [07_System_Architecture.md](07_System_Architecture.md) and [11_Data_Flow.md](11_Data_Flow.md).

**How would you scale it to many concurrent sessions?**
Sessions are long-lived and stateful. Discuss session affinity versus shared state, capacity limits, separating compute-heavy components, and provider rate limits. See [20_Deployment.md](20_Deployment.md).

**How do you make providers replaceable?**
Contracts owned by inner layers, adapters per provider, configuration-based selection, normalized errors, and contract tests. See [09_Low_Level_Design.md](09_Low_Level_Design.md).

**How would you design observability for it?**
Correlation identifiers, per-stage timing, distributions rather than averages, token and cost attribution, and privacy of content. See [19_Observability.md](19_Observability.md).

**What would you do differently at ten times the scale?**
Identify measured bottlenecks first. Discuss moving to shared storage and coordination, media server separation, and caching, each justified by evidence.

## Backend Questions

**Why asynchronous programming for this workload?**
The workload is I/O-bound with many concurrent connections. Explain the event loop, why blocking calls harm all sessions, and how blocking work is isolated.

**How do you handle cancellation in an async pipeline?**
Cancellation must propagate through every stage; discuss cleanup, partial results, and cost of work not cancelled.

**What is dependency injection and why use it here?**
Collaborators are supplied from outside, enabling substitution and testing. Relate to the composition root.

**How do you handle backpressure?**
Bounded buffers, slow consumers, and dropping or pausing policies per stream type.

**SQLite versus PostgreSQL: when do you move?**
Concurrency, multi-instance deployment, and operational needs. Explain how the repository boundary limits migration cost.

## Voice AI Questions

**Why WebRTC instead of WebSockets for audio?**
Transport characteristics, loss behavior, browser capture and processing, NAT traversal, and the cost in complexity. See [12_WebRTC.md](12_WebRTC.md).

**Explain ICE, STUN, and TURN.**
Candidate gathering, public address discovery, relay as a last resort, and the bandwidth implications of TURN.

**Streaming versus batch speech recognition: trade-offs?**
Latency, complexity, interim results changing, and approximating streaming with a non-streaming model. See [13_Speech_to_Text.md](13_Speech_to_Text.md).

**How do you detect that a user has finished speaking?**
Voice activity detection, silence thresholds, premature cutoff versus delay, and tuning with measurement.

**How do you handle interruption?**
Detection, stopping playback, cancelling synthesis and generation, and recording what the user actually heard.

**What contributes to perceived latency, and how do you reduce it?**
Decompose the stages, overlap them through streaming, and measure the distribution.

## LLM Questions

**How does function calling work and how do you make it safe?**
The model requests, the application validates and executes. Cover schema validation, authorization, limits, and confirmation of consequential actions. See [17_Tool_Calling.md](17_Tool_Calling.md).

**What is prompt injection and how do you mitigate it?**
Untrusted text treated as instructions. Cover separation, least capability, external validation, and testing. See [21_Security.md](21_Security.md).

**Explain a RAG pipeline and its failure modes.**
Chunking, embedding, retrieval, ranking, assembly. Failure modes include poor chunking, embedding mismatch, irrelevant context, and poisoned sources. See [15_RAG.md](15_RAG.md).

**How do you evaluate a RAG system?**
Representative question sets, retrieval relevance measures, and answer review, with changes accepted on evidence.

**How do you manage conversation memory within a context limit?**
Recent turns verbatim, summarization of older ones, budgeting, and retention. See [16_Memory.md](16_Memory.md).

**Why LangGraph rather than plain code?**
Explicit state, branching, and checkpointing versus the cost of an added model. Be ready to argue both sides.

**How do you control cost?**
Token accounting per turn, context budgets, model selection, and caching. See [14_LLM.md](14_LLM.md).

## Project-Specific Questions

**Why documentation first?**
Reduces rework, forces clarity, and creates a record of reasoning. Acknowledge the risk of designing in the abstract and how the Phase 1 spike addresses it.

**What is the biggest technical risk in this project?**
Real-time latency and transport complexity are strong candidates. Justify with specifics.

**What decision are you least sure about, and how would you test it?**
Pick an open decision from [23_Architecture_Decisions.md](23_Architecture_Decisions.md) and describe an experiment.

**Which part would you change first with hindsight?**
Answerable only after implementation; update this entry with real experience.

## Future Expansion Points

- Worked answers drawn from real implementation experience.
- Diagrams to draw from memory for system design practice.
- Mock interview scenarios and retrospectives.
- Questions tagged by seniority level.

## Related Documents

[07_System_Architecture.md](07_System_Architecture.md), [22_Engineering_Principles.md](22_Engineering_Principles.md), [24_Learning_Journal.md](24_Learning_Journal.md)
