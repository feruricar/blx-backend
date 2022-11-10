from fastapi import APIRouter,status,Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.schemas.schemas import Pedido
from src.infra.sqlalchemy.repositorios.repositorio_pedido import RepositorioPedido
from src.infra.sqlalchemy.config.database import get_db, criar_bd


router = APIRouter()

#PEDIDOS
@router.post('/pedidos', status_code=status.HTTP_201_CREATED,response_model=Pedido)
def fazer_pedido(pedido:Pedido, session: Session = Depends(get_db)):
    pedido_criado = RepositorioPedido(session).gravar_pedido(pedido)
    return pedido_criado

@router.get('/pedidos/{id}',response_model=Pedido)
def exibir_pedido(id:int, session:Session = Depends(get_db)):
    try:
        pedido_localizado = RepositorioPedido(session).buscarPorId(id)
        return pedido_localizado
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não há um pedido com este id = {id}')

@router.get('/pedidos/{usuario_id}/compras', status_code=status.HTTP_200_OK)
def listar_pedidos(usuario_id:int, session: Session = Depends(get_db)):
    pedidos = RepositorioPedido(session).listar_meus_pedidos_por_usuario_id(usuario_id)
    return pedidos

@router.get('/pedidos/{usuario_id}/vendas', status_code=status.HTTP_200_OK)
def listar_vendas(usuario_id:int, session: Session = Depends(get_db)):
    pedidos = RepositorioPedido(session).listar_minhas_vendas_usuario_id(usuario_id)
    return pedidos




@router.put('/pedidos/{id}',status_code=status.HTTP_200_OK,response_model=Pedido)
def atualizar_pedidos(id:int, pedido:Pedido, session: Session = Depends(get_db)):
    RepositorioPedido(session).editar(id,pedido)
    pedido.id = id
    return pedido

@router.delete('/pedidos/{id}',status_code=status.HTTP_200_OK)
def remover_pedido(id:int, session: Session = Depends(get_db)):
    RepositorioPedido(session).remover(id)
    return