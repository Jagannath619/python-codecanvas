# DRY (Don't Repeat Yourself)

## Definition
Avoid duplicating logic; every piece of knowledge should have a single, authoritative representation.

## Why it matters
- Fewer bugs caused by inconsistent updates
- Easier maintenance and refactoring
- Better readability and reuse

## When to apply it
- Repeated business calculations
- Duplicate validation, formatting, or mapping logic

## Common pitfalls / violations
- Copy-pasting logic across modules
- Premature abstraction for things that are not truly repeated

## Included examples
- `bad.py`: duplicate discount calculations across checkout paths
- `good.py`: shared discount utility reused by all checkout flows
