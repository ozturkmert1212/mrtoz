# Project Brief

## Project Name
Cline's Memory Bank

## Purpose
Provide a reliable, versioned, and minimal "memory bank" for projects so that sessions with no persistence can rehydrate project context fully from a small set of Markdown files.

## Core Requirements
- Memory bank MUST contain the six core files described in the specification.
- Files are authoritative: every session MUST read all files before any work.
- Files should be human-readable, machine-parsable, and easy to update.

## Goals
- Make onboarding and context-reload trivial after a memory reset.
- Encourage precise documentation of architecture, tech choices, and active work.

## Scope
- Create and maintain `memory-bank/` containing: `projectbrief.md`, `productContext.md`, `activeContext.md`, `systemPatterns.md`, `techContext.md`, `progress.md`.

## Owner
Cline (project lead)

## Notes
This file is the source of truth for project purpose and scope and should be updated when project goals change.