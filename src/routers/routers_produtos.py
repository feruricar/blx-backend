from fastapi import APIRouter,status,Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.schemas.schemas import Produto , Usuario, ProdutoSimples
from src.infra.sqlalchemy.repositorios.repositorio_produto import RepositorioProduto 
from src.infra.sqlalchemy.config.database import get_db, criar_bd


router = APIRouter()

#PRODUTOS
@router.post('/produtos', status_code=status.HTTP_201_CREATED,response_model=Produto)
def criar_produtos(produto:Produto, db: Session = Depends(get_db)):
    RepositorioProduto(db).criar(produto)
    return produto

@router.get('/produtos', status_code=status.HTTP_200_OK, response_model=List[Produto])
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos 

@router.get('/produtos/{id}')
def exibir_produto(id:int, db:Session = Depends(get_db)):
    produto_localizado = RepositorioProduto(db).buscarPorId(id)
    if not produto_localizado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não há um produto com este id = {id}')
    return produto_localizado


@router.put('/produtos/{id}',status_code=status.HTTP_200_OK,response_model=ProdutoSimples)
def atualizar_produtos(id:int, produto:Produto, db: Session = Depends(get_db)):
    RepositorioProduto(db).editar(id,produto)
    produto.id = id
    return produto

@router.delete('/produtos/{id}',status_code=status.HTTP_200_OK)
def remover_produto(id:int, db: Session = Depends(get_db)):
    RepositorioProduto(db).remover(id)
    return