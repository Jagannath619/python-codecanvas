# Encapsulation

## Definition
Bundle data and behavior together while controlling direct access to internal state.

## Why it matters
- Protects invariants and prevents invalid state
- Makes APIs clearer and safer to use
- Enables internal changes without breaking callers

## When to apply it
- Domain entities with business constraints
- Objects requiring controlled updates

## Common pitfalls / violations
- Exposing mutable state publicly
- Allowing bypass of validation rules

## Included examples
- `bad.py`: bank account balance is directly mutable and can go negative
- `good.py`: account state is protected and updated through validated methods
