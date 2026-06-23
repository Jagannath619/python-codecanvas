# Single Responsibility Principle (SRP)

## Definition
A class or module should have one reason to change, meaning it should focus on a single responsibility.

## Why it matters
- Improves readability and maintainability
- Reduces coupling between unrelated concerns
- Makes testing smaller and faster

## When to apply it
- Classes that handle both business logic and I/O
- Services that mix validation, persistence, and notifications

## Common pitfalls / violations
- “God classes” doing validation, storage, and reporting
- Utility classes that silently become dumping grounds

## Included examples
- `bad.py`: `OrderProcessor` mixes validation, persistence, and email sending
- `good.py`: responsibilities split into validator, repository, and notifier
