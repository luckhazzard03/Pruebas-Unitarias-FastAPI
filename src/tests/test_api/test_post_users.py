from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_post_users():
    # Parámetros del nuevo usuario
    new_user = {
        "name": "Jaime",
        "email": "jaime@example.com"
    }
    
    # Realiza la solicitud POST al endpoint con los parámetros
    response = client.post("/usuarios", json=new_user)
    # Verifica que el código de estado sea 201, indicando que se creó correctamente
    assert response.status_code == 201 # Creación exitosa
    response_data = response.json()
    assert response_data["message"] == "Usuario creado con éxito"
    assert "user_id" in response_data  # Asegúrate de que el ID esté en la respuesta
    