# 07 - Dependency Injection

Dependencies help reuse logic like authentication or database access.

## Example

```python
from fastapi import Depends, FastAPI

app = FastAPI()

def common_parameters(q: str | None = None):
    return {"q": q}

@app.get("/search")
def search(params = Depends(common_parameters)):
    return params
```
