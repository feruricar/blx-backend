from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.routers import routers_produtos, routers_usuarios

#criar_bd()

app = FastAPI()

#CORS
origins = ["http://localhost",
           "http://localhost:3000"
          ]

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],)

#ROUTERS PRODUTOS USUARIOS
app.include_router(routers_produtos.router)
app.include_router(routers_usuarios.router)