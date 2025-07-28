from fastapi import FastAPI
from typing import Optional

app = FastAPI()
@app.get("/hello")
def hello(name: Optional[str] = None):
    if name:
        return {"message": f"Hello {name}"}
    return {"message": "Hello"}


@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Cześć, {name}!"}
@app.get("/greet/{name}")
def greet_get(name: str):
    return {"message": f"Cześć, {name}!"}


