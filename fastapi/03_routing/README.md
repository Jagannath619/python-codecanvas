# 03 - Routing

Routes define API endpoints.

## Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items")
def get_items():
    return [{"id": 1, "name": "Book"}]
```
