# Separation of Concerns

## Definition
Separate a system into distinct sections where each handles one concern (e.g., UI, business logic, data access).

## Why it matters
- Improves modularity and testability
- Reduces change impact across layers
- Enables parallel team development

## When to apply it
- Web/API apps with presentation, domain, and persistence layers
- Systems integrating external services

## Common pitfalls / violations
- Controllers doing direct SQL and business rules together
- Business logic tied to framework-specific details

## Included examples
- `bad.py`: route handler mixes validation, business logic, and persistence
- `good.py`: handler delegates work to service and repository layers
