# 09 - Authentication

Authentication protects your API endpoints.

## Example

```python
from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/profile")
def profile(x_token: str = Header()):
    return {"token": x_token}
```
