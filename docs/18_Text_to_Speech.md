# 18 Text to Speech

> Status: Draft. Introduced in Phase 0. Provider characteristics must be verified against current provider documentation before decisions are finalized.

## Purpose

This document describes speech synthesis in VoiceOS: provider options, streaming audio, and voice cloning considerations.

## Goals

- Describe candidate providers and the trade-offs between them.
- Explain how streaming synthesis fits the pipeline.
- Treat voice cloning as a capability with explicit risks.

## Table of Contents

- [Role in the System](#role-in-the-system)
- [Providers](#providers)
- [Streaming Audio](#streaming-audio)
- [Interruption](#interruption)
- [Voice Selection](#voice-selection)
- [Voice Cloning](#voice-cloning)
- [Evaluation Criteria](#evaluation-criteria)
- [Design Implications](#design-implications)
- [Future Expansion Points](#future-expansion-points)
- [Related Documents](#related-documents)

## Role in the System

TTS converts response text into audio. Its time to first audio is a major component of perceived latency, and its voice quality shapes the experience. It is accessed through the speech synthesis contract in [09_Low_Level_Design.md](09_Low_Level_Design.md).

## Providers

| Provider | General character |
| --- | --- |
| Edge TTS | Access to Microsoft's online voices without an account; useful for development; an informal integration with no service guarantee. Initial provider |
| ElevenLabs | Hosted service known for high-quality and expressive voices, with streaming and voice cloning features |
| OpenAI | Hosted speech synthesis offered alongside its other model APIs |

This table gives orientation only. Voices, languages, pricing, streaming behavior, licensing, and limits change and must be confirmed from each provider's documentation when evaluated. Terms of use, particularly for an informal integration, should be reviewed before any production use.

## Streaming Audio

Synthesis can begin before the full response text exists. The pipeline groups streamed model output into speakable units, typically sentences, and sends each to TTS as it completes. Audio is forwarded to the client as it is produced.

Considerations:

- Unit size trades latency against prosody: very small units sound disjointed, large units delay the first audio.
- Providers differ in whether they stream audio within a unit or return it whole.
- Audio format and sample rate differences are handled by the adapter and the pipeline's audio handling.
- Text sent to TTS is prepared for speech: formatting symbols, abbreviations, and numbers may need normalization.

## Interruption

When the user interrupts, queued audio is discarded, pending synthesis is cancelled, and the session records how much of the response was delivered. See [11_Data_Flow.md](11_Data_Flow.md). Providers vary in how cleanly in-flight synthesis can be cancelled, which affects cost and must be measured.

## Voice Selection

Voice is a per-agent and possibly per-session configuration, expressed in VoiceOS terms and mapped by the adapter to provider voices. Language and voice must match the language of the response.

## Voice Cloning

Voice cloning creates a synthetic voice resembling a real person. It is out of scope for the MVP ([03_Goals_and_Scope.md](03_Goals_and_Scope.md)) and recorded here so that the architecture does not preclude it and so that its risks are considered in advance:

- Consent of the person whose voice is cloned must be explicit and recorded.
- Misuse for impersonation is a serious abuse case.
- Legal requirements vary by jurisdiction and provider terms.
- Cloned voice assets are sensitive data and need access control.

Adoption requires an ADR that addresses these points.

## Evaluation Criteria

- Naturalness and intelligibility for target languages and domain vocabulary.
- Time to first audio.
- Streaming support and cancellation behavior.
- Language and voice availability.
- Cost at expected volume.
- Licensing and terms of use.
- Reliability.

## Design Implications

- The contract yields audio as a stream with explicit format information.
- Cancellation is a first-class operation.
- Text preparation is a separate step from synthesis, so it is testable independently.
- Frequently used fixed phrases are candidates for caching.

## Future Expansion Points

- Provider benchmark results.
- Emotion and speaking style control where providers support it.
- Phrase caching.
- Controlled voice cloning support.

## Related Documents

[09_Low_Level_Design.md](09_Low_Level_Design.md), [11_Data_Flow.md](11_Data_Flow.md), [14_LLM.md](14_LLM.md), [21_Security.md](21_Security.md)
