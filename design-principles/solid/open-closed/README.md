# Open/Closed Principle (OCP)

## Definition
Software entities should be open for extension but closed for modification.

## Why it matters
- New behavior can be added with less regression risk
- Existing tested code remains stable
- Encourages polymorphism and cleaner architecture

## When to apply it
- Conditional-heavy logic based on types or channels
- Plugin-style features and policy rules

## Common pitfalls / violations
- Large `if/elif` chains that must be edited for every new case
- Modifying stable core classes for each variation

## Included examples
- `bad.py`: payment processing depends on a growing conditional chain
- `good.py`: payment methods implement a shared protocol and are extensible
