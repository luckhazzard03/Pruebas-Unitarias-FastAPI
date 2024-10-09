from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_update_users():
    # Crear un usuario para luego actualizarlo
    client.post("/usuarios/", json={"name": "Juan", "email": "juan@example.com"})

    # Actualizar los datos del usuario
    updated_user = {
        "name": "Juan Actualizado",
        "email": "juan.actualizado@example.com"
    }

    # Actualiza el usuario con ID 1
    response = client.put("/usuarios/1", json=updated_user)

    # Verificar que el código de estado sea 200
    assert response.status_code == 200
    assert response.json() == {"message": "Usuario actualizado con éxito", "user_id": 1}
    
def test_update_user_not_found():
    # Datos del usuario que intentamos actualizar, pero el ID no existe
    updated_user = {
        "name": "No Existo",
        "email": "noexisto@example.com"
    }
    
    # Realiza la solicitud PUT a un ID que no existe
    response = client.put("/usuarios/999", json=updated_user)  # ID que no existe
    
    # Verifica que el código de estado sea 404 (no encontrado)
    assert response.status_code == 404  
    # Verifica que la respuesta contenga el mensaje de error esperado
    assert response.json() == {"detail": "Usuario no encontrado"}  