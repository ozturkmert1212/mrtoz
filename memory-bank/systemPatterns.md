# System Patterns

## Architecture Overview
- Keep the system modular and documented: clearly define components and responsibilities.
- Favor small, independently testable modules.

## Key Technical Decisions
- Decision logs live in `systemPatterns.md` when they affect architecture or major components.
- Use explicit patterns (e.g., hexagonal architecture, event-driven components) when applied.

## Design Patterns in Use
- Dependency inversion for core services
- Clear separation of configuration vs. behaviour
- Explicit error-handling boundaries

## Component Relationships
- Document integration points, APIs, and data contracts here.

## Critical Implementation Paths
- Note any areas that are fragile or require careful sequencing (migrations, deployment steps, stateful upgrades).