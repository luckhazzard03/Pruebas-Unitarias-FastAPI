from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_post_users():
    response = client.get("/usuarios")
    assert response.status_code == 200
    assert response.json() == [
        {"name": "Juan", "email": "juan@example.com"},
        {"name": "Ana", "email": "ana@example.com"},
    ]