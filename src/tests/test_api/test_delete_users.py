from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_delete_users():
    # Crear un usuario para eliminar
    response = client.post("/usuarios/", json={"name": "Juan", "email": "juan@example.com"})
    user_id = response.json()["user_id"]  # Obtener el ID del nuevo usuario

    # Realizar la eliminación
    response = client.delete(f"/usuarios/{user_id}")
    
    # Verificar que el código de estado sea 200
    assert response.status_code == 200
    assert response.json() == {"message": "Usuario eliminado con éxito", "user_id": user_id}
 
