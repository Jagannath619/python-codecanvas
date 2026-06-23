# Fail Fast

## Definition
Detect invalid states and inputs as early as possible and raise clear errors immediately.

## Why it matters
- Bugs surface earlier and closer to root cause
- Prevents cascading failures and corrupted state
- Improves reliability and debuggability

## When to apply it
- Input validation and configuration loading
- Startup checks for required dependencies and settings

## Common pitfalls / violations
- Deferring validation until deep in execution
- Silently ignoring invalid input and continuing

## Included examples
- `bad.py`: invalid config is tolerated until runtime behavior breaks
- `good.py`: config is validated at startup with explicit exceptions
