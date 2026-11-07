# 13 Speech to Text

> Status: Draft. Introduced in Phase 0. Provider characteristics must be verified against current provider documentation before decisions are finalized.

## Purpose

This document explains speech recognition options for VoiceOS, the difference between streaming and batch recognition, and the criteria used to choose and replace providers.

## Goals

- Describe the candidate providers and their general character.
- Explain streaming versus batch trade-offs.
- Define evaluation criteria so that provider choices are evidence-based.

## Table of Contents

- [Role in the System](#role-in-the-system)
- [Providers](#providers)
- [Streaming vs Batch](#streaming-vs-batch)
- [Speech Boundaries and Endpointing](#speech-boundaries-and-endpointing)
- [Trade-offs](#trade-offs)
- [Evaluation Criteria](#evaluation-criteria)
- [Design Implications](#design-implications)
- [Future Expansion Points](#future-expansion-points)
- [Related Documents](#related-documents)

## Role in the System

STT converts user audio to text for the workflow. Its latency and accuracy directly affect the whole conversation. It is accessed through the speech recognition contract in [09_Low_Level_Design.md](09_Low_Level_Design.md).

## Providers

| Provider | General character |
| --- | --- |
| Whisper (faster-whisper) | Open model run locally; strong multilingual accuracy; not designed as a native streaming recognizer; consumes local compute. Initial provider |
| Deepgram | Hosted service oriented toward real-time streaming recognition |
| AssemblyAI | Hosted service offering streaming and asynchronous recognition |
| Sarvam | Hosted service focused on Indian languages and accents |

This table gives orientation only. Capabilities, pricing, languages, and limits change and must be confirmed from each provider's documentation when evaluated.

## Streaming vs Batch

- **Batch recognition** processes a complete audio segment and returns a final result. It is simple and often accurate, but the user waits for the full segment to be recognized after they stop speaking.
- **Streaming recognition** processes audio as it arrives and returns interim results that are later finalized. It reduces perceived latency and enables early processing, but adds protocol complexity and means interim text can change.

A model that is not natively streaming can approximate streaming by processing short overlapping segments, trading latency, compute, and accuracy against each other. The design of the Voice Pipeline must work with both modes so that the choice remains a provider decision.

## Speech Boundaries and Endpointing

Deciding that the user has finished speaking is a separate concern from transcription, though some providers combine them. Ending too early cuts users off; ending too late adds delay. Voice activity detection can run in VoiceOS or be supplied by the provider. Which owns it is an open decision affecting provider replaceability and is tracked in [23_Architecture_Decisions.md](23_Architecture_Decisions.md).

## Trade-offs

| Dimension | Local model | Hosted streaming service |
| --- | --- | --- |
| Latency | Depends on hardware and segmentation | Typically designed for low latency |
| Cost | Compute cost, no per-use fee | Usage-based fees |
| Privacy | Audio stays local | Audio sent to a third party |
| Operations | Model hosting and resources | Dependency on service availability |
| Language and domain coverage | Model dependent | Provider dependent |

## Evaluation Criteria

Choices are made against the same measurements for every provider:

- Accuracy on audio representative of the target users and domain.
- Latency from end of speech to final transcript.
- Language and accent coverage.
- Behavior under noise and telephony-quality audio.
- Cost at expected volume.
- Data handling terms.
- Reliability and rate limits.

## Design Implications

- The contract supports both interim and final results, and providers that only return final results simply never emit interim ones.
- Audio format conversion is the adapter's responsibility.
- Language is passed as a hint and is configurable per session.
- Transcript confidence, where available, is retained for diagnostics, not relied on for business logic.

## Future Expansion Points

- An evaluation harness and benchmark results across providers.
- Speaker handling for multi-party audio.
- Domain vocabulary support.
- Partial-transcript-driven early retrieval.

## Related Documents

[09_Low_Level_Design.md](09_Low_Level_Design.md), [11_Data_Flow.md](11_Data_Flow.md), [12_WebRTC.md](12_WebRTC.md), [19_Observability.md](19_Observability.md)
