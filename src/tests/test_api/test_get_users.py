# src/app/tests/test_api/test_users.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_users():
    # Crear un usuario para obtenerlo
    client.post("/usuarios/", json={"name": "Juan", "email": "juan@example.com"})
    
    # Obtener el usuario creado
    response = client.get("/usuarios/1")
    
    # Verificar que el código de estado sea 200
    assert response.status_code == 200
    assert response.json() == {"name": "Juan", "email": "juan@example.com"}
    
def test_get_users_not_found():
    response = client.get("/usuarios/999") # ID que no existe
    assert response.status_code == 404 
    assert response.json() == {"detail": "Usuario no encontrado"}