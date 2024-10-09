# src/app/tests/test_api/test_usuarios.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_user():
    response = client.get("/usuarios/1")
    assert response.status_code == 200
    assert response.json() == {"name": "Juan", "email": "juan@example.com" }
    
def test_get_user_2():
    response = client.get("/usuarios/2")
    assert response.status_code == 200
    assert response.json() == {"name": "Ana", "email": "ana@example.com"}
    
# def test_get_user_3():
#     response = client.get("/usuarios/3")
#     assert response.status_code == 200
#     assert response.json() == {"name": "Carlos", "email": "Carl@example.com"}
    
def test_get_user_not_found():
    response = client.get("/usuarios/999") # ID que no existe
    assert response.status_code == 404 
    assert response.json() == {"detail": "Usuario no encontrado"}