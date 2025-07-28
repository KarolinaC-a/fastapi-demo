from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_hello_standard():
    response = client.get("/hello?name=Karolina")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Karolina"}

def test_hello_empty_name():
    response = client.get("/hello?name=")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello "}
def test_hello_name():
    response = client.get("/hello?name=Jan")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Jan"}
def test_hello_empty_name():
    response = client.get("/hello?name=")
    assert response.status_code == 200
    print(response.json())
    assert response.json()["message"].startswith("Hello")

def test_hello_polish_name():
    response = client.get("/hello?name=Łukasz")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Łukasz"}
def test_hello_missing_name():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello"}
def test_wrong_path():
    response = client.get("/hejo")
    assert response.status_code == 404
