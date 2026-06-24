# Composition over Inheritance

## Definition
Prefer composing objects with capabilities over deep inheritance hierarchies.

## Why it matters
- More flexible behavior combinations
- Avoids fragile base-class coupling
- Easier testing and runtime swapping of behavior

## When to apply it
- Feature sets that vary by capability
- Systems requiring dynamic behavior changes

## Common pitfalls / violations
- Deep class trees for orthogonal behaviors
- Subclass explosion for every feature combination

## Included examples
- `bad.py`: inheritance hierarchy grows for each notification combination
- `good.py`: notifier behavior composed from reusable sender components
