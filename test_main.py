from fastapi.testclient import TestClient
from app.main import app   # uwaga na import!

client = TestClient(app)

def test_greet():
    response = client.get("/greet/Karolina")
    assert response.status_code == 200
    assert response.json() == {"message": "Cześć, Karolina!"}

