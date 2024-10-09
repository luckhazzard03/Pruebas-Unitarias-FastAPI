my_fastapi_project/
│
├── src/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py          # Archivo principal que arranca la API
│   │   ├── database.py      # Archivo donde se simula la base de datos
│   │   ├── endpoints/       # Carpeta para los endpoints
│   │   │   ├── __init__.py
│   │   │   └── usuarios.py   # Aquí están tus endpoints CRUD para usuarios
│   │   │
│   │   └── tests/           # Carpeta para las pruebas
│   │       ├── __init__.py
│   │       └── test_api/
│   │           ├── __init__.py
│   │           └── test_usuarios.py
│   │
│   └── requirements.txt
│
└── README.md


Ejecutar tus pruebas con pytest:

 pytest

Activar el entorno virtual 
~/Desktop/Ejercicios endpoints FASTAPI

 uvicorn src.app.main:app --reload


DOCKER
Construir la imagen de Docker de nuevo

 docker-compose build --no-cache

Iniciar el contenedor
 
 docker-compose up