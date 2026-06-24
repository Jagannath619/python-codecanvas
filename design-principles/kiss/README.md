# KISS (Keep It Simple, Stupid)

## Definition
Prefer the simplest solution that correctly solves the current problem.

## Why it matters
- Simple code is easier to understand and debug
- Reduces maintenance cost and onboarding time
- Lowers risk of hidden edge-case bugs

## When to apply it
- Feature implementation with straightforward requirements
- Refactoring over-engineered helper utilities

## Common pitfalls / violations
- Using advanced abstractions without need
- Building generic frameworks for one narrow use case

## Included examples
- `bad.py`: over-engineered parser using unnecessary classes
- `good.py`: direct and readable parser function
