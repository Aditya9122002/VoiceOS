# 21 Security

> Status: Draft. Introduced in Phase 0. This document states design intent and threat areas; it is not a certification or a substitute for a security review.

## Purpose

This document describes the security considerations of VoiceOS: secrets, authentication, rate limiting, transport security, API keys, prompt injection, and retrieval security.

## Goals

- Identify the main threat areas of a voice agent framework.
- Establish security measures as architectural requirements.
- Treat model inputs and tool outputs as untrusted.

## Table of Contents

- [Principles](#principles)
- [Secrets](#secrets)
- [Authentication](#authentication)
- [Rate Limiting](#rate-limiting)
- [HTTPS and Transport Security](#https-and-transport-security)
- [API Keys](#api-keys)
- [Prompt Injection](#prompt-injection)
- [RAG Security](#rag-security)
- [Data Protection](#data-protection)
- [Tool and Voice-Specific Risks](#tool-and-voice-specific-risks)
- [Supply Chain](#supply-chain)
- [Future Expansion Points](#future-expansion-points)
- [Related Documents](#related-documents)

## Principles

- Defense in depth: no single control is relied on.
- Least privilege for components, tools, and credentials.
- Untrusted input stays untrusted wherever it appears in the pipeline.
- Secure defaults: the default configuration is the safe one.

## Secrets

- Provider credentials and signing keys are supplied through the environment or a secret manager.
- Secrets are never committed, logged, returned in errors, or sent to the browser.
- Secrets can be rotated without code changes.
- Repository scanning guards against accidental commits.

## Authentication

Strategy is in [10_API_Design.md](10_API_Design.md). Security requirements:

- Browser clients use short-lived credentials issued by the backend, so no long-lived secret reaches the client.
- Authentication is required on every interface outside local development.
- Authorization is enforced in the service layer, scoped by tenant and user.
- Failed attempts are rate limited and recorded.

## Rate Limiting

Voice sessions consume expensive downstream resources, so abuse has direct cost. Limits apply to:

- Request rates per client or key.
- Concurrent sessions per client.
- Session duration and audio volume.
- Tool executions and model usage per session.

Limits fail closed and return the documented error structure. Where multiple instances run, limit state must be shared, see [20_Deployment.md](20_Deployment.md).

## HTTPS and Transport Security

- All non-local traffic uses TLS, including WebSockets.
- WebRTC media is encrypted by the protocol; signaling travels over a TLS-protected channel.
- Allowed browser origins are restricted explicitly.
- Connections to providers use TLS and verified certificates.

## API Keys

- Keys are generated with sufficient randomness and shown once.
- Keys are stored hashed, not in plain text.
- Keys are scoped, revocable, and have identifiable prefixes to ease leak detection.
- Key use is attributable in logs without logging the key.

## Prompt Injection

Language models cannot reliably distinguish instructions from data. User speech, retrieved documents, and tool results can all contain text that attempts to override the agent's instructions. Mitigations are layered, none sufficient alone:

- Separate instructions from untrusted content in the prompt, with clear delimiters.
- Give the model no more capability than the task needs; the strongest control is limiting what a manipulated model can do.
- Validate model-requested tool calls and arguments outside the model.
- Require explicit user confirmation for consequential actions.
- Do not place secrets or other tenants' data in prompts.
- Test with adversarial inputs as part of the test suite.

## RAG Security

- **Poisoning:** documents may contain instructions aimed at the model. Retrieved text is treated as data, per [15_RAG.md](15_RAG.md).
- **Access control:** retrieval enforces the same permissions as direct access to the source. Filtering happens in retrieval, not in the prompt.
- **Tenant isolation:** knowledge from one tenant is never retrievable by another.
- **Ingestion trust:** sources are vetted, and provenance is retained to trace the origin of bad content.
- **Leakage:** responses must not expose content the user is not entitled to.

## Data Protection

- Raw audio is not persisted by default.
- Transcripts and memory are stored under defined retention and can be deleted. See [16_Memory.md](16_Memory.md).
- Data sent to hosted providers is documented per provider so operators can make informed choices.
- Telemetry excludes conversation content by default. See [19_Observability.md](19_Observability.md).

## Tool and Voice-Specific Risks

- Speech recognition errors can turn into unintended actions; consequential tools require confirmation.
- Voice is a weak identity signal, and spoken statements of identity are not authentication.
- Synthetic voices enable impersonation; voice cloning requires consent controls. See [18_Text_to_Speech.md](18_Text_to_Speech.md).
- Recorded or replayed audio may be used to trigger an agent.

## Supply Chain

- Dependencies are justified, pinned, and reviewed per [22_Engineering_Principles.md](22_Engineering_Principles.md).
- Automated vulnerability alerts are enabled for the repository.
- Container images are built from minimal, maintained bases.
- Third-party adapters and tools are treated as untrusted code.

## Future Expansion Points

- A formal threat model.
- A vulnerability disclosure policy before public release.
- Audit logging for sensitive operations.
- Compliance considerations for regulated deployments.

## Related Documents

[10_API_Design.md](10_API_Design.md), [15_RAG.md](15_RAG.md), [17_Tool_Calling.md](17_Tool_Calling.md), [19_Observability.md](19_Observability.md), [20_Deployment.md](20_Deployment.md)
