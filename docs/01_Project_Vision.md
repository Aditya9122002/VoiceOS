# 01 Project Vision

> Status: Draft. Introduced in Phase 0.

## Purpose

This document defines why VoiceOS exists and the direction it is meant to take over the long term. It is the reference against which scope decisions in [03_Goals_and_Scope.md](03_Goals_and_Scope.md) are judged.

## Goals

- State the vision and mission in terms that can guide decisions.
- Identify who VoiceOS is for.
- Define how progress and success are judged.
- State explicitly what the project will not attempt.

## Table of Contents

- [Vision](#vision)
- [Mission](#mission)
- [Philosophy](#philosophy)
- [Target Audience](#target-audience)
- [Success Metrics](#success-metrics)
- [Non-Goals](#non-goals)
- [Future Expansion Points](#future-expansion-points)
- [Related Documents](#related-documents)

## Vision

A developer should be able to build a real-time voice agent by composing well-defined, replaceable parts, with production concerns such as observability, security, and scalability addressed by the architecture rather than added afterward.

Voice AI should not require every team to rediscover how to stream audio, sequence speech recognition, language models, and speech synthesis, manage conversation state, and avoid lock-in to a single vendor.

## Mission

Provide an open-source, thoroughly documented, modular framework for building production-grade real-time AI voice agents, and develop it in public so that its design decisions and trade-offs are available for others to learn from.

## Philosophy

The principles below shape every later decision. Their operational form is in [22_Engineering_Principles.md](22_Engineering_Principles.md).

- **Architecture before implementation.** Design is written down and reviewed before code.
- **Documentation first.** Documentation is a deliverable, not an afterthought.
- **Modularity.** Components have narrow responsibilities and explicit boundaries.
- **Provider independence.** Vendors are implementation details behind interfaces.
- **Production mindset.** Boundaries are designed for scale and reliability from the start, without premature optimization.
- **Learning in public.** Decisions, trade-offs, and mistakes are recorded openly.

## Target Audience

| Audience | What they need from VoiceOS |
| --- | --- |
| Backend and AI engineers building voice agents | A reference architecture and reusable components so they do not start from nothing |
| Teams comparing providers | A way to evaluate and switch STT, LLM, TTS, and vector store providers without rewriting application logic |
| Engineers learning production AI systems | Documented reasoning behind each design choice |
| Open-source contributors | Clear boundaries, conventions, and decision records that make contribution tractable |

## Success Metrics

Numeric targets are intentionally not set in Phase 0. They are set after baseline measurements exist, so that targets reflect observed behavior rather than guesses.

| Metric | What it measures | How it is judged |
| --- | --- | --- |
| Provider replaceability | Cost of swapping a provider | A swap changes adapter code and configuration only, never business logic |
| Time to first conversation | Onboarding quality | A new developer reaches a spoken conversation by following the documented quickstart |
| Documentation currency | Whether docs track reality | Every architectural change updates a document or an ADR in the same change |
| Latency visibility | Operability | Every conversational turn exposes per-stage timings (see [19_Observability.md](19_Observability.md)) |
| Testability | Engineering confidence | The core pipeline can be tested without calling external providers |
| Community health | Open-source viability | Contributions, issue quality, and discussion activity |

## Non-Goals

- A hosted platform or commercial service. Products may be built on VoiceOS, but VoiceOS itself is a framework.
- Training, fine-tuning, or hosting foundation models.
- Acting as a telephony carrier or network operator.
- A general text chatbot framework. Text is supported only as far as it serves voice agents.
- A no-code or visual agent builder.
- Re-implementing capabilities that providers already supply well.

## Future Expansion Points

- Public success metrics dashboard once baselines exist.
- A governance document if the contributor base grows.
- Audience-specific guides, for example for teams deploying in regulated environments.

## Related Documents

[02_Problem_Statement.md](02_Problem_Statement.md), [03_Goals_and_Scope.md](03_Goals_and_Scope.md), [22_Engineering_Principles.md](22_Engineering_Principles.md)
