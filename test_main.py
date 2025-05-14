from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_welcome():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_tokenize_text():
    response = client.post("/tokenize", json={"text": "hello"})
    assert response.status_code == 200
    assert "checksum" in response.json()
