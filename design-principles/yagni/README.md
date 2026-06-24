# YAGNI (You Aren't Gonna Need It)

## Definition
Do not build features until they are actually required.

## Why it matters
- Prevents wasted effort on speculative work
- Keeps codebase lean and focused
- Avoids maintaining unused complexity

## When to apply it
- During initial implementation and MVP phases
- When tempted to support hypothetical future use cases

## Common pitfalls / violations
- Adding plugin systems or abstraction layers before demand
- Shipping unused configuration options and flags

## Included examples
- `bad.py`: overbuilt report generator with unused exporter modes
- `good.py`: implements only current CSV requirement cleanly
