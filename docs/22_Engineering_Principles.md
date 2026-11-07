# 22 Engineering Principles

> Status: Draft. Introduced in Phase 0. Rules here are proposed standards; tooling choices are made in Phase 1.

## Purpose

This document defines the rules by which VoiceOS is built: architecture rules, coding standards, documentation rules, dependency rules, and testing philosophy.

## Goals

- Make quality expectations explicit and checkable.
- Keep the codebase consistent as contributors are added.
- Guard against overengineering and premature optimization.

## Table of Contents

- [Guiding Principles](#guiding-principles)
- [Architecture Rules](#architecture-rules)
- [Coding Standards](#coding-standards)
- [Documentation Rules](#documentation-rules)
- [Dependency Rules](#dependency-rules)
- [Testing Philosophy](#testing-philosophy)
- [Change Process](#change-process)
- [Future Expansion Points](#future-expansion-points)
- [Related Documents](#related-documents)

## Guiding Principles

- **Simplicity first.** The simplest design that meets the requirement is preferred.
- **No speculative abstraction.** An abstraction is introduced when a real second use or a real replacement need exists. Provider interfaces are the deliberate exception, because replacement is a stated requirement.
- **Design for scale, build for need.** Boundaries are drawn so scaling is possible; scaling infrastructure is built when required.
- **Measure before optimizing.** Performance work follows evidence from [19_Observability.md](19_Observability.md).
- **Explain decisions.** Significant choices are recorded with their reasoning.

## Architecture Rules

1. Dependencies point inward; the domain depends on nothing outside itself.
2. Business logic never imports a provider SDK or framework type.
3. External capabilities are reached only through contracts owned by inner layers.
4. Concrete implementations are assembled at the composition root.
5. A module has one reason to change.
6. State belongs to sessions or storage, not module globals.
7. Blocking work does not run on the event loop.

These rules follow the SOLID principles and clean architecture; they are enforced by review and, where practical, by automated import checks.

## Coding Standards

- Type annotations on public interfaces, and static type checking in continuous integration.
- Names express intent and avoid unexplained abbreviations.
- Named constants replace magic numbers, with the reason for the value recorded.
- Functions and modules are small enough to describe in one sentence.
- Comments explain reasons and constraints, not the obvious.
- Errors are handled deliberately: no silently swallowed exceptions, and failures carry context.
- Formatting and linting are automated, so review focuses on design.

## Documentation Rules

- Every folder contains a README stating its purpose.
- Every public module and contract is documented.
- An architectural change updates the affected documents in the same change.
- A significant decision gets an ADR, see [23_Architecture_Decisions.md](23_Architecture_Decisions.md).
- A topic is explained in one place and linked elsewhere.
- Documents state their status, and describe intended behavior as intended, never as implemented when it is not.

## Dependency Rules

- A new dependency requires a stated reason, a license check, and consideration of the alternative of not adding it.
- Dependencies are pinned for reproducibility.
- Popularity alone is not a reason to adopt a framework.
- Dependencies are kept at the edges. Core layers stay free of third-party types where practical.
- Unmaintained or poorly licensed dependencies are replaced or removed.

## Testing Philosophy

- Tests give confidence to change the system; they are not a coverage target.
- Most tests are fast and isolated, using fake providers. The default test run needs no network or credentials.
- Contract tests verify that each adapter honors the contract it implements, so replacing a provider is verified, not assumed.
- Integration tests verify that real components work together, including real provider calls, and run separately from the default pipeline.
- Pipeline behavior that is hard to test, such as interruption and cancellation, is tested deliberately with controlled inputs.
- Security-relevant behavior, including prompt injection resistance, has tests.
- Quality of model-dependent behavior is measured with evaluation sets rather than exact output assertions.
- A bug fix includes a test that would have caught the bug.

## Change Process

- Changes are small, focused, and reviewed.
- Major architectural changes are proposed through an ADR and approved before implementation.
- A change is complete when its code, tests, and documentation are complete.

## Future Expansion Points

- Concrete tooling choices for linting, typing, and import enforcement.
- Contribution and code review guidelines.
- Performance testing and load testing approach.
- Release and versioning policy.

## Related Documents

[06_Project_Structure.md](06_Project_Structure.md), [09_Low_Level_Design.md](09_Low_Level_Design.md), [23_Architecture_Decisions.md](23_Architecture_Decisions.md)
