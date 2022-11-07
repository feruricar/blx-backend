from fastapi import FastAPI , Depends, status
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from src.infra.sqlalchemy.models.models import Usuario
from src.schemas.schemas import Produto , Usuario, ProdutoSimples
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.infra.sqlalchemy.repositorios.repositorio_produto import RepositorioProduto 
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario 


criar_bd()

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

#PRODUTOS
@app.post('/produtos', status_code=status.HTTP_201_CREATED,response_model=Produto)
def criar_produtos(produto:Produto, db: Session = Depends(get_db)):
    RepositorioProduto(db).criar(produto)
    return produto

@app.get('/produtos', status_code=status.HTTP_200_OK, response_model=List[Produto])
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos 

@app.put('/produtos/{id}',status_code=status.HTTP_200_OK,response_model=ProdutoSimples)
def atualizar_produtos(id:int, produto:Produto, db: Session = Depends(get_db)):
    RepositorioProduto(db).editar(id,produto)
    produto.id = id
    return produto

@app.delete('/produtos/{id}',status_code=status.HTTP_200_OK)
def remover_produto(id:int, db: Session = Depends(get_db)):
    RepositorioProduto(db).remover(id)
    return

#USUARIOS
@app.post('/signup',status_code=status.HTTP_201_CREATED,response_model=Usuario)
def Signup(usuario:Usuario, session: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado

@app.get('/usuarios', status_code=status.HTTP_200_OK, response_model=List[Usuario])
def listar_usuarios(session: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(session).listar()
    return usuarios 

