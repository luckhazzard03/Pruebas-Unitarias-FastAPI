# src/app/main.py

from fastapi import FastAPI
from src.app.routers import users
# Importa la simulación de la base de datos

app = FastAPI()

# Incluir el router del módulo de usuarios
app.include_router(users.router)
