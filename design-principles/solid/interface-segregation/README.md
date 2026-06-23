# Interface Segregation Principle (ISP)

## Definition
Clients should not be forced to depend on methods they do not use.

## Why it matters
- Smaller interfaces reduce implementation burden
- Avoids unused methods and dummy implementations
- Increases modularity and testability

## When to apply it
- Broad interfaces used by many different clients
- Teams building separate services with different capabilities

## Common pitfalls / violations
- Fat interfaces mixing unrelated actions
- Implementers raising `NotImplementedError` for irrelevant methods

## Included examples
- `bad.py`: one large worker interface forces unsupported behavior
- `good.py`: small focused interfaces fit each worker role
