# 19 Observability

> Status: Draft. Introduced in Phase 0. Tooling choices are deferred to Phase 6; this document defines what must be observable, not which products are used.

## Purpose

This document defines what VoiceOS must make observable so that the system can be operated, debugged, and improved: metrics, logging, tracing, latency, token usage, and cost.

## Goals

- Make every conversational turn explainable after the fact.
- Attribute latency and cost to specific stages and providers.
- Avoid leaking sensitive content through telemetry.

## Table of Contents

- [Principles](#principles)
- [Correlation](#correlation)
- [Metrics](#metrics)
- [Logging](#logging)
- [Tracing](#tracing)
- [Latency](#latency)
- [Token Usage](#token-usage)
- [Cost Monitoring](#cost-monitoring)
- [Privacy](#privacy)
- [Alerting](#alerting)
- [Future Expansion Points](#future-expansion-points)
- [Related Documents](#related-documents)

## Principles

- Observability is designed in, not added after problems appear.
- Telemetry is structured and machine-readable.
- The instrumentation interface belongs to the inner layers; the telemetry backend is replaceable like any other provider.
- Telemetry must not meaningfully add to latency on the conversation path.

## Correlation

Every session has an identifier and every turn has an identifier. Both propagate through all subsystems and appear in logs, metrics labels where cardinality allows, and traces. Without them a single user turn cannot be reconstructed across components.

## Metrics

Aggregated, numeric measurements, grouped by area:

| Area | Examples |
| --- | --- |
| Sessions | Active sessions, session duration, session outcomes |
| Turns | Turn count, interruption rate, failed turns |
| Stage timing | Duration of each pipeline stage |
| Providers | Request counts, error rates by category, timeouts, rate limit events |
| Retrieval | Retrieval duration, results returned |
| Tools | Calls per tool, duration, failures |
| System | Event loop lag, resource use, queue depths |

## Logging

- Logs are structured with consistent fields, including session and turn identifiers.
- Log levels have defined meanings and are used consistently.
- Errors include the normalized failure category and provider identity.
- Content of conversations is not logged by default. Debug-level content logging, if provided, is opt-in and clearly marked.
- Secrets never appear in logs.

## Tracing

A trace follows a turn through its stages, with each stage as a span carrying timing and relevant attributes such as provider and model identifiers. Traces answer where time went in a specific slow turn, which aggregated metrics cannot. A common open standard for instrumentation is the candidate approach, subject to evaluation in Phase 6.

## Latency

The primary user-facing measure is the time from end of user speech to first audio of the response. It is decomposed into stages to locate delay:

- End-of-speech detection.
- Final transcription.
- Retrieval and memory lookup.
- Time to first generated output.
- Time to first synthesized audio.
- Transport to the client.

Distributions, not just averages, are tracked, because tail latency determines how bad the experience is. Targets are set after baselines exist ([01_Project_Vision.md](01_Project_Vision.md)).

## Token Usage

Every language model call records the model identifier and the input and output token counts as reported by the provider, attributed to the session and turn. Unreported usage, for example from cancelled calls, is noted as unknown rather than estimated silently.

## Cost Monitoring

Cost is derived from recorded usage and configured pricing for each provider: tokens for language models and embeddings, audio duration or characters for speech services. Cost is attributable per turn, session, and, where applicable, tenant. Pricing configuration is explicit and dated, since provider prices change.

## Privacy

- Transcripts and audio are sensitive and excluded from general telemetry.
- Telemetry retention is limited and configurable.
- Access to detailed traces is restricted. See [21_Security.md](21_Security.md).

## Alerting

Alerts are based on conditions that need human action, such as sustained provider error rates, latency degradation, and cost anomalies. Thresholds are defined after baselines exist.

## Future Expansion Points

- Dashboards for latency, quality, and cost.
- Conversation quality metrics, such as interruption and abandonment patterns.
- Replay tooling for diagnosing a past turn from recorded events.
- Per-tenant cost reporting.

## Related Documents

[08_High_Level_Design.md](08_High_Level_Design.md), [11_Data_Flow.md](11_Data_Flow.md), [14_LLM.md](14_LLM.md), [20_Deployment.md](20_Deployment.md), [21_Security.md](21_Security.md)
