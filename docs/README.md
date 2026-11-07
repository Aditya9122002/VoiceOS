# VoiceOS Documentation

This directory contains the engineering documentation for VoiceOS. The project follows a documentation-first approach: architecture is described and reviewed here before it is implemented.

All documents are in draft status during Phase 0. Statements about the system describe intended design, not implemented behavior. Where a decision has not been made, the document says so and points to the Architecture Decision Records in [23_Architecture_Decisions.md](23_Architecture_Decisions.md).

## Reading Order

| Group | Documents |
| --- | --- |
| Context | 01 Project Vision, 02 Problem Statement, 03 Goals and Scope, 04 Product Roadmap |
| Foundations | 05 Tech Stack, 06 Project Structure |
| Architecture | 07 System Architecture, 08 High Level Design, 09 Low Level Design, 10 API Design, 11 Data Flow |
| Subsystems | 12 WebRTC, 13 Speech to Text, 14 LLM, 15 RAG, 16 Memory, 17 Tool Calling, 18 Text to Speech |
| Operations | 19 Observability, 20 Deployment, 21 Security |
| Process | 22 Engineering Principles, 23 Architecture Decisions |
| Journey | 24 Learning Journal, 25 Interview Notes, 26 Future Roadmap |

## Document Conventions

- Every document contains Purpose, Goals, Table of Contents, body sections, Future Expansion Points, and Related Documents.
- A topic is explained in one document and linked from the others, not repeated.
- Diagrams use Mermaid so they are versioned with the text.
- Changes to architecture update the affected documents and add or amend an ADR in the same change.
