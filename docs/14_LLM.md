# 14 LLM

> Status: Draft. Introduced in Phase 0.

## Purpose

This document describes how VoiceOS uses language models: the provider abstraction, prompt management, function calling, structured outputs, and streaming responses.

## Goals

- Keep business logic independent of any model vendor.
- Treat prompts as managed, versioned assets.
- Handle the voice-specific constraints of language model use.

## Table of Contents

- [Role in the System](#role-in-the-system)
- [Provider Abstraction](#provider-abstraction)
- [Prompt Management](#prompt-management)
- [Function Calling](#function-calling)
- [Structured Outputs](#structured-outputs)
- [Streaming Responses](#streaming-responses)
- [Voice-Specific Considerations](#voice-specific-considerations)
- [Usage and Cost](#usage-and-cost)
- [Failure Handling](#failure-handling)
- [Future Expansion Points](#future-expansion-points)
- [Related Documents](#related-documents)

## Role in the System

The language model generates responses and decides when tools are needed. It is invoked by the workflow in the Orchestrator, never directly from the API or transport layers. The initial provider is Gemini; replacement is a designed capability.

## Provider Abstraction

The language model contract accepts a message sequence, tool definitions, and generation settings, and yields streamed text, tool call requests, and usage information. Provider differences in message formats, tool call formats, safety behavior, and limits are absorbed by the adapter. Business logic works with VoiceOS's own message and tool representations. See [09_Low_Level_Design.md](09_Low_Level_Design.md).

Behavior is not identical across models even behind a stable contract. Prompts may need adjustment per model, so evaluation per provider is part of replacement.

## Prompt Management

- Prompts are assets, separate from code, and versioned with the repository.
- A prompt has a name, a purpose, and documented inputs.
- Prompts are assembled from labeled parts: instructions, retrieved context, conversation history, and the current user input. Assembly is covered in [15_RAG.md](15_RAG.md).
- Untrusted content, such as retrieved text and user input, is clearly delimited from instructions. See [21_Security.md](21_Security.md).
- Prompt changes are reviewed like code, and changes that alter behavior are tested.

Where prompts are stored and how they are loaded is an open decision for Phase 1.

## Function Calling

The model can request execution of defined tools. The contract carries tool definitions to the model and tool call requests back to the workflow. The workflow validates and executes calls and returns results. The model never executes anything itself. Execution rules are in [17_Tool_Calling.md](17_Tool_Calling.md).

## Structured Outputs

Where the workflow needs machine-readable output, the model is asked for output matching a defined schema and the result is validated. Rules:

- Validation is mandatory; model output is not trusted to conform.
- A defined behavior exists for invalid output, such as bounded retry, then fallback.
- Provider-native structured output features are used where available and hidden behind the contract; the validation step remains regardless.

## Streaming Responses

Responses are consumed as they are produced so that speech synthesis can begin before generation finishes. Consequences:

- Output is grouped into speakable units, typically sentences, before being passed to TTS.
- Cancellation stops generation when the user interrupts.
- Usage information may arrive only at the end of a stream and must still be captured, including for cancelled streams where the provider reports it.
- Tool call requests within a stream pause speech output until resolved.

## Voice-Specific Considerations

- Responses are heard, not read, so they are short, plain, and free of visual formatting.
- Latency to the first generated tokens matters more than total generation time.
- Prompt size affects latency and cost, so context assembly is budgeted.
- The agent must handle partial or corrected user speech gracefully.

## Usage and Cost

Every model call records the model used, input and output token counts, and latency, tied to the session and turn. Detail in [19_Observability.md](19_Observability.md).

## Failure Handling

Timeouts, rate limits, and provider errors are normalized by the adapter. The workflow has a defined fallback response, and retries are bounded and limited to calls that are safe to repeat.

## Future Expansion Points

- Provider fallback chains.
- Evaluation sets for prompt and model changes.
- Response caching where appropriate.
- Model routing by task complexity.

## Related Documents

[09_Low_Level_Design.md](09_Low_Level_Design.md), [15_RAG.md](15_RAG.md), [16_Memory.md](16_Memory.md), [17_Tool_Calling.md](17_Tool_Calling.md), [21_Security.md](21_Security.md)
