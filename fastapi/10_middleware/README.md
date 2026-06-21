# 10 - Middleware

Middleware runs before and after each request.

## Example

```python
from fastapi import FastAPI, Request

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    response = await call_next(request)
    return response
```
