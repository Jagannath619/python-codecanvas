# 12 - Testing

Use TestClient to test FastAPI applications.

## Example

```python
from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()
client = TestClient(app)

@app.get("/")
def read_root():
    return {"message": "ok"}

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
```
