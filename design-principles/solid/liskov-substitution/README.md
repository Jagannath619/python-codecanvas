# Liskov Substitution Principle (LSP)

## Definition
Subtypes should be replaceable for their base types without breaking expected behavior.

## Why it matters
- Preserves correctness in polymorphic code
- Prevents surprising runtime errors
- Makes abstractions trustworthy

## When to apply it
- Inheritance hierarchies and polymorphic APIs
- Libraries exposing common base classes/interfaces

## Common pitfalls / violations
- Subclasses narrowing valid inputs unexpectedly
- Subclasses throwing unsupported-operation errors

## Included examples
- `bad.py`: `Penguin` breaks behavior expected from `Bird`
- `good.py`: behavior contracts are split into fitting abstractions
