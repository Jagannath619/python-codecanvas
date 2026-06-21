# 06 - Response Models

Response models control the output format.

## Example

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ItemOut(BaseModel):
    name: str

@app.get("/item", response_model=ItemOut)
def get_item():
    return {"name": "Pen", "price": 10}
```
