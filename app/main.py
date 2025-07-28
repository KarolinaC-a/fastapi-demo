from fastapi import FastAPI

app = FastAPI()
@app.get("/hello")
def hello():
    return {"message": "Hello from FastAPI!"}
@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Cześć, {name}!"}
@app.get("/greet/{name}")
def greet_get(name: str):
    return {"message": f"Cześć, {name}!"}


