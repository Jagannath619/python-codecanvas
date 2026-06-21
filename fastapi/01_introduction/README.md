# 01 - Introduction

FastAPI is a modern Python web framework for building APIs quickly.

## Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
```
