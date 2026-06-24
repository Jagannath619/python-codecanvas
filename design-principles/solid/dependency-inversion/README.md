# Dependency Inversion Principle (DIP)

## Definition
High-level modules should depend on abstractions, not concrete implementations.

## Why it matters
- Improves testability and flexibility
- Reduces hard coupling to infrastructure details
- Makes swapping implementations easier

## When to apply it
- Services that rely on storage, messaging, or external APIs
- Code needing dependency injection and mocking

## Common pitfalls / violations
- Creating concrete dependencies directly in business logic
- No abstraction boundary for external systems

## Included examples
- `bad.py`: notification service directly constructs an SMTP client
- `good.py`: notification service depends on a notifier abstraction
