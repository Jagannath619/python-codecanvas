# 11 - Background Tasks

Background tasks run after returning the response.

## Example

```python
from fastapi import BackgroundTasks, FastAPI

app = FastAPI()

def write_log(message: str):
    with open("log.txt", "a") as file:
        file.write(message + "\n")

@app.post("/send")
def send_email(background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, "Email sent")
    return {"message": "Task scheduled"}
```
