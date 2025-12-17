# Product Context

## Why this project exists
Cline's Memory Bank exists to solve the problem of reconstructing project context after a full memory reset between sessions. It centralizes essential project knowledge so work can continue predictably.

## Problems it solves
- Loss of session-specific memory between restarts
- Fragmented documentation scattered across files and comments
- Onboarding friction for returning engineers

## How it should work
- Files live in `memory-bank/` at repository root.
- Every session begins by reading all memory bank files in this prescribed order: `projectbrief.md`, `productContext.md`, `systemPatterns.md`, `techContext.md`, `activeContext.md`, `progress.md`.

## User Experience Goals
- Clear, short documents that can be skimmed quickly
- Explicit "what's next" in `activeContext.md` and `progress.md`
- Easy to update during work and after major decisions

## Target Users
- Primary developer (Cline)
- New contributors needing fast context
- Automation that rehydrates context for tools/agents