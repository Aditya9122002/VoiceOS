# 10 API Design

> Status: Draft. Introduced in Phase 0. This document defines conventions and categories. Specific endpoints and message schemas are defined in Phase 1.

## Purpose

This document defines how VoiceOS exposes functionality to clients: the REST and WebSocket interfaces, naming, versioning, error handling, and authentication strategy.

## Goals

- Establish conventions before individual interfaces are designed.
- Keep the external interface stable while internals change.
- Make errors and authentication consistent across all interfaces.

## Table of Contents

- [Principles](#principles)
- [REST API](#rest-api)
- [WebSocket API](#websocket-api)
- [Naming Conventions](#naming-conventions)
- [Versioning](#versioning)
- [Error Handling](#error-handling)
- [Authentication Strategy](#authentication-strategy)
- [Open Decisions](#open-decisions)
- [Future Expansion Points](#future-expansion-points)
- [Related Documents](#related-documents)

## Principles

- The API is a contract; internals may change, the contract changes deliberately.
- Request and message shapes are validated at the boundary.
- The API contains no business logic; it translates and delegates.
- The same conventions apply to REST and WebSocket interfaces.

## REST API

REST is used for operations that are request and response in nature and not time-critical in the audio path. Candidate resource categories:

- **Sessions:** creating, inspecting, and ending conversation sessions.
- **Knowledge sources:** adding and managing documents for retrieval.
- **Agent configuration:** selecting providers and behavior for an agent.
- **System:** health and readiness information.

Resource categories are candidates until finalized in Phase 1.

## WebSocket API

WebSockets carry real-time, bidirectional control events during a session. Candidate message categories:

- **Session control:** start, end, and state changes.
- **Signaling:** exchange of connection setup information if WebRTC signaling uses this channel.
- **Conversation events:** transcripts, response text, and turn state changes.
- **Interruption:** client signals that the user is speaking over the agent.
- **Errors:** notification of failures during a session.

Audio itself travels over the media transport described in [12_WebRTC.md](12_WebRTC.md), not through these messages.

Every message carries a type identifier and a session identifier, and the set of message types is closed and documented.

## Naming Conventions

- Resource names are plural nouns; actions are expressed through standard HTTP methods where possible.
- Names use a single consistent casing convention across the API; the convention is fixed in Phase 1.
- WebSocket message types use a consistent namespaced naming pattern describing the domain and the event.
- Identifiers are opaque to clients.
- Time values use a single unambiguous standard format.

## Versioning

- The API carries an explicit version visible in the request path.
- Breaking changes require a new version; additive changes do not.
- A deprecation policy states how long a prior version is supported.
- WebSocket protocol versions are negotiated at connection time.

## Error Handling

All errors use a consistent structure containing a stable machine-readable code, a human-readable message, a request or correlation identifier, and optional details. Rules:

- Codes are stable and documented; messages may change.
- HTTP status codes follow standard semantics.
- Internal details, stack traces, and provider error text are never exposed.
- WebSocket errors use the same structure as REST errors.
- Normalized provider failure categories from [09_Low_Level_Design.md](09_Low_Level_Design.md) map to documented codes.

## Authentication Strategy

Proposed, subject to ADR:

- **Server-to-server callers:** API keys, stored hashed, revocable, scoped.
- **Browser clients:** short-lived session credentials issued by the backend, so long-lived secrets never reach the browser.
- **Transport:** all interfaces served over TLS in any non-local environment.
- **Authorization:** checks occur in the service layer, not only at the edge.

Details and threats are covered in [21_Security.md](21_Security.md).

## Open Decisions

- Whether WebRTC signaling uses the WebSocket channel or REST.
- The casing convention and the exact error code taxonomy.
- Whether and how API keys are scoped per capability.

## Future Expansion Points

- Machine-readable API specifications generated from the implementation.
- Pagination, filtering, and idempotency conventions once list-style resources exist.
- A client SDK if external adoption warrants it.

## Related Documents

[08_High_Level_Design.md](08_High_Level_Design.md), [11_Data_Flow.md](11_Data_Flow.md), [12_WebRTC.md](12_WebRTC.md), [21_Security.md](21_Security.md)
