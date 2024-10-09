# src/app/routers/users.py
from fastapi import APIRouter, HTTPException
from src.app.database import users_db  # Importa la simulación de la base de datos
from pydantic import BaseModel

router = APIRouter()



# Definir el modelo User
class User(BaseModel):
    name: str
    email: str

# Obtener todos los usuarios (GET)
@router.get("/usuarios/")
def get_all_users():
    # Manejo de la excepción si la base de datos está vacía
    if not users_db:  # Si el diccionario está vacío
        raise HTTPException(status_code=404, detail="No hay usuarios disponibles")
    
    return list(users_db.values())  # Devuelve una lista de todos los usuarios

# Obtener un usuario por ID (GET)
@router.get("/usuarios/{user_id}")
def get_users(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return users_db[user_id]


#cear usuario metodo(POST)
@router.post("/usuarios/", status_code=201)
#define el metodo y se instancia la clase User
def post_users(user: User):
    #Asigna un nuevo ID AL USUARIO
    new_id = max(users_db.keys()) +  1 if users_db else 1
    
    #Añadir el nuevo usuario a la base de datos simulada
    users_db[new_id] =  user.model_dump() #Convertimos  el modelo en un diccionario 
    
    #Devolver el nuevo usuario
    return {"message": "Usuario creado con éxito", "user_id": new_id}  # Respuesta esperada 


#Se Define la funcion para actualizar los usuarios
@router.put("/usuarios/{user_id}")
def put_users(user_id: int, user: User):
    if user_id not in users_db:
        raise HTTPException(status_code=404,  detail="Usuario no encontrado")
    
    users_db[user_id] = user.model_dump()
    return {"message": "Usuario actualizado con éxito", "user_id": user_id}
    
  
  
#Metodo DELETE   
@router.delete("/usuarios/{user_id}")
def delete_users(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    del users_db[user_id] #Elimina el usuario por ID
    return{"message": "Usuario eliminado con éxito", "user_id": user_id}
    