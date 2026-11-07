# 24 Learning Journal

> Status: Draft. Introduced in Phase 0.

## Purpose

This document defines how learning is recorded during the project: the daily entry format, how resources and notes are kept, and how problems solved are documented. It supports the public learning goal of VoiceOS.

## Goals

- Make learning visible and reviewable.
- Keep entries short enough to sustain the habit.
- Turn solved problems into reusable knowledge.

## Table of Contents

- [How to Use This Journal](#how-to-use-this-journal)
- [Daily Entry Format](#daily-entry-format)
- [Problems Solved Format](#problems-solved-format)
- [Resources](#resources)
- [Notes Conventions](#notes-conventions)
- [Weekly Review](#weekly-review)
- [Future Expansion Points](#future-expansion-points)
- [Related Documents](#related-documents)

## How to Use This Journal

Entries are added when learning happens, not in advance, and are written in reverse chronological order below the sections of this document once the first entry exists. The journal records what was learned and why it mattered, not a log of every command. Where an entry produces a decision, it links to the ADR. Where entries grow long, they may move to a dedicated folder, a decision recorded in Phase 1.

## Daily Entry Format

```markdown
### YYYY-MM-DD

**Focus:** the topic or task of the day.

**What I learned:**
- Concrete points, in my own words.

**What I built or changed:**
- Links to commits or documents.

**What confused me:**
- Open questions to resolve later.

**Next:**
- The next step.
```

## Problems Solved Format

```markdown
### Problem title

**Symptom:** what was observed.
**Cause:** the root cause, once known.
**Fix:** what resolved it.
**Lesson:** what to remember or check next time.
**Related:** document, ADR, or commit.
```

Problems solved are recorded when the cause was not obvious. A problem that took time to diagnose is worth recording even if the fix was small.

## Resources

Reference material for the topics of this project. Entries are added with a note on why each was useful.

| Topic | Resource |
| --- | --- |
| Backend framework | FastAPI official documentation |
| Workflow orchestration | LangGraph official documentation |
| Browser real-time media | MDN WebRTC API documentation |
| WebRTC connectivity | RFC 8445 (ICE), RFC 8489 (STUN), RFC 8656 (TURN) |
| WebRTC overview | RFC 8825 |
| Audio codec | RFC 6716 (Opus) |
| Asynchronous Python | Python standard library asyncio documentation |
| Vector search | FAISS project documentation |
| Tool protocol | Model Context Protocol specification |
| Recording decisions | Architecture Decision Record literature and templates |

Resource entries should be verified against current versions, since documentation changes.

## Notes Conventions

- Write for a reader a year from now.
- Separate facts from opinions and from guesses.
- Cite the source of any non-obvious claim.
- Prefer a short diagram or example over a long paragraph.
- Link concepts to the documents in this directory instead of restating them.

## Weekly Review

Once a week, read the week's entries and write a short summary:

- What was learned that changes how the system should be built.
- Which open questions remain.
- Whether any documents are now out of date and need updating.
- What to focus on next week.

## Future Expansion Points

- A published index of entries by topic.
- Conversion of selected entries into public write-ups.
- A glossary built from recurring terms.

## Related Documents

[01_Project_Vision.md](01_Project_Vision.md), [23_Architecture_Decisions.md](23_Architecture_Decisions.md), [25_Interview_Notes.md](25_Interview_Notes.md)
