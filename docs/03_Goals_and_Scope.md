# 03 Goals and Scope

> Status: Draft. Introduced in Phase 0. MVP scope is proposed and requires owner approval.

## Purpose

This document defines what VoiceOS will deliver, in what order of ambition, and what is deliberately excluded, so that scope decisions can be made against written criteria.

## Goals

- Separate long-term goals from the minimum viable product.
- Make exclusions explicit.
- Provide testable success criteria.

## Table of Contents

- [Project Goals](#project-goals)
- [MVP Goals](#mvp-goals)
- [Out of Scope](#out-of-scope)
- [Future Goals](#future-goals)
- [Success Criteria](#success-criteria)
- [Future Expansion Points](#future-expansion-points)
- [Related Documents](#related-documents)

## Project Goals

1. Provide a modular framework in which STT, LLM, retrieval, and TTS providers are replaceable.
2. Support real-time, streaming, browser-based voice conversation.
3. Orchestrate conversations through explicit, inspectable workflows.
4. Support retrieval-augmented answers, conversation memory, and tool calling.
5. Include observability, security, and testing as architectural concerns.
6. Maintain complete, current documentation and decision records.

## MVP Goals

The MVP is the smallest system that demonstrates the architecture end to end. It uses the initial stack in [05_Tech_Stack.md](05_Tech_Stack.md).

- A browser client that captures microphone audio and plays synthesized responses.
- A backend that runs the voice pipeline for one conversation at a time per session.
- One STT provider, one LLM provider, and one TTS provider behind interfaces.
- One retrieval source backed by the initial vector store.
- Short-term conversation memory within a session.
- Per-turn timing information for each pipeline stage.
- Demonstrated replacement of at least one provider with no change to business logic.

## Out of Scope

Out of scope for the MVP, and for the framework unless later promoted through an ADR:

- Telephony and SIP integration.
- Multi-tenant administration and billing.
- Voice cloning.
- Native mobile clients.
- Plugin system and marketplace.
- Model training, fine-tuning, or hosting.
- High-availability and multi-region deployment.

## Future Goals

Directions the architecture should not preclude, described in [26_Future_Roadmap.md](26_Future_Roadmap.md): long-term memory, additional providers, telephony, plugin extensibility, enterprise features, and agentic workflows.

## Success Criteria

| Area | Criterion |
| --- | --- |
| Functionality | A spoken question in the browser produces a spoken, retrieval-informed answer |
| Modularity | Swapping one provider changes only its adapter and configuration |
| Observability | Each turn reports per-stage latency |
| Testability | The pipeline runs in tests using fake providers |
| Documentation | Every subsystem has a current document and every significant decision an ADR |
| Reproducibility | A new contributor can run the MVP by following documented steps |

## Future Expansion Points

- Convert MVP goals into tracked milestones at the start of Phase 2.
- Add numeric performance criteria after baseline measurement.
- Add a scope-change procedure if contribution volume grows.

## Related Documents

[01_Project_Vision.md](01_Project_Vision.md), [04_Product_Roadmap.md](04_Product_Roadmap.md), [26_Future_Roadmap.md](26_Future_Roadmap.md)
