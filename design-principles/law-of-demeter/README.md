# Law of Demeter (Principle of Least Knowledge)

## Definition
A unit should only talk to its immediate collaborators, not navigate deep object chains.

## Why it matters
- Reduces coupling to internal object structure
- Improves encapsulation boundaries
- Makes refactoring safer

## When to apply it
- Rich domain models with nested objects
- Service code that accesses deep chains like `a.b.c.d`

## Common pitfalls / violations
- Train-wreck calls (`obj.a().b().c()`)
- Reaching through objects to use details they should hide

## Included examples
- `bad.py`: checkout service drills through customer internals
- `good.py`: customer exposes intent-level method for delivery city
