import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import users_db  # Asegúrate de que la base de datos simulada esté disponible

client = TestClient(app)

@pytest.fixture(scope="function")
def clean_db():
    # Limpiar la base de datos simulada antes de cada prueba
    users_db.clear()
    yield
    # Limpiar la base de datos simulada después de cada prueba
    users_db.clear()

def test_get_all_users(clean_db):  # Usamos 'clean_db' como argumento
    # Crear dos usuarios antes de la prueba
    client.post("/usuarios/", json={"name": "Juan", "email": "juan@example.com"})
    client.post("/usuarios/", json={"name": "Ana", "email": "ana@example.com"})

    # Realizar la solicitud para obtener todos los usuarios
    response = client.get("/usuarios/")
    
    # Verificar que la solicitud fue exitosa
    assert response.status_code == 200

    # Verificar que los datos obtenidos son los esperados (independientemente del orden)
    expected_users = [
        {"name": "Juan", "email": "juan@example.com"},
        {"name": "Ana", "email": "ana@example.com"},
    ]

    # Ordenar ambos resultados por el campo 'name' para evitar problemas de orden
    assert sorted(response.json(), key=lambda x: x["name"]) == sorted(expected_users, key=lambda x: x["name"])
