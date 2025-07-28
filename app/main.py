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
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Witaj w FastAPI!"}
from fastapi.responses import FileResponse

@app.get("/")
def serve_frontend():
    return FileResponse("app/static/index.html")
from fastapi.responses import FileResponse

@app.get("/")
def read_index():
    return FileResponse("app/static/index.html")



