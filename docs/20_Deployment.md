# 20 Deployment

> Status: Draft. Introduced in Phase 0. Implementation is Phase 7; this document records considerations so that earlier phases do not foreclose them.

## Purpose

This document describes how VoiceOS is intended to be packaged, built, delivered, and operated: containers, CI/CD, production concerns, scaling, cloud hosting, and reverse proxying.

## Goals

- Ensure earlier design decisions remain deployable.
- Identify the infrastructure concerns specific to real-time voice.
- Define the direction without prescribing a platform.

## Table of Contents

- [Principles](#principles)
- [Docker](#docker)
- [CI/CD](#cicd)
- [Production](#production)
- [Scaling](#scaling)
- [Cloud](#cloud)
- [Reverse Proxy](#reverse-proxy)
- [Environments and Configuration](#environments-and-configuration)
- [Operational Concerns](#operational-concerns)
- [Future Expansion Points](#future-expansion-points)
- [Related Documents](#related-documents)

## Principles

- Deployment is reproducible: the same inputs produce the same deployable artifact.
- Configuration is separated from code and supplied through the environment.
- The simplest deployment that meets requirements is preferred; complexity is added when a need is demonstrated.

## Docker

Containers package the backend and frontend with their dependencies for reproducible environments. Considerations specific to VoiceOS:

- Local speech models increase image size and resource needs, and may benefit from separate handling of model files.
- Real-time media needs network configuration beyond ordinary HTTP services, covered under Reverse Proxy and in [12_WebRTC.md](12_WebRTC.md).
- Images run as non-root users and contain no secrets.

## CI/CD

GitHub Actions is the intended automation. Pipelines are kept simple and portable.

- **Continuous integration:** linting, type checking, and tests run on every change. Tests use fake providers and need no network or credentials. See [22_Engineering_Principles.md](22_Engineering_Principles.md).
- **Build:** produce versioned container images.
- **Delivery:** deployments are triggered from approved changes and are reversible.
- Credentials for any live-provider checks are held as protected secrets, and such checks are separate from the default pipeline.

## Production

Production readiness requires, at minimum: health and readiness reporting, structured logs and metrics per [19_Observability.md](19_Observability.md), configuration validation at startup, graceful shutdown that lets active sessions end cleanly, and the security measures in [21_Security.md](21_Security.md).

## Scaling

Voice sessions are long-lived and stateful, which differs from stateless request and response services.

- **Vertical first:** a single instance serves the early deployment.
- **Horizontal:** multiple instances require that each session is handled consistently by one instance for its duration, or that session state is shared. Shared state may call for a coordination store such as Redis, and a shared database in place of SQLite. Both require ADRs.
- **Capacity:** the limiting resources are concurrent sessions, local inference compute where used, and provider rate limits.
- **Separation:** compute-heavy parts, such as local speech recognition, can move to separate services through the provider boundary.

## Cloud

VoiceOS does not depend on a particular cloud provider. Cloud-specific choices are isolated in deployment definitions. Region selection matters for latency, since distance to users and to providers adds to every turn.

## Reverse Proxy

A reverse proxy terminates TLS and routes HTTP and WebSocket traffic. Considerations:

- WebSocket connections need long idle and total timeouts and correct upgrade handling.
- Request size and rate limits protect the backend.
- WebRTC media does not pass through an HTTP reverse proxy; it needs its own reachable network ports, and potentially a TURN server, which has distinct infrastructure and bandwidth requirements.
- Security headers and restrictions on allowed origins are applied here and in the application.

## Environments and Configuration

Development, test, and production differ only by configuration. Secrets are provided by the environment or a secret manager and are never committed. Configuration is validated at startup so that misconfiguration fails fast.

## Operational Concerns

- Backups and retention for persisted data.
- Upgrade procedure, including database migration.
- Rollback procedure.
- Incident response and runbooks.

## Future Expansion Points

- Deployment guides for specific platforms.
- Infrastructure definitions.
- Autoscaling policy based on measured session capacity.
- Multi-region operation.

## Related Documents

[05_Tech_Stack.md](05_Tech_Stack.md), [12_WebRTC.md](12_WebRTC.md), [19_Observability.md](19_Observability.md), [21_Security.md](21_Security.md)
