
from sqlalchemy.orm import Session
from sqlalchemy import update,delete,select
from src.schemas import schemas 
from src.infra.sqlalchemy.models import models
from typing import List


class RepositorioPedido():

    def __init__(self, session:Session)->None:
        self.session = session

    def gravar_pedido(self, pedido:schemas.Pedido)->models.Pedido:
        db_pedido = models.Pedido(quantidade = pedido.quantidade,
                                   local_entrega = pedido.local_entrega,
                                   tipo_entrega  = pedido.tipo_entrega,
                                   observacao   = pedido.observacao,
                                   usuario_id = pedido.usuario_id,
                                   produto_id = pedido.produto_id)
        self.session.add(db_pedido)
        self.session.commit()
        self.session.refresh(db_pedido)
        return db_pedido

    def buscarPorId(self,id:int)->models.Pedido:
        consulta = select(models.Pedido).where(models.Pedido.id == id)
        pedido = self.session.execute(consulta).scalars().first()
        return pedido

    def listar_pedidos(self)->List[models.Pedido]:
        pedidos = self.session.query(models.Pedido).all()
        return pedidos

    def listar_meus_pedidos_por_usuario_id(self,usuario_id:int)->List[models.Pedido]:
        consulta = select(models.Pedido).where(models.Pedido.usuario_id == usuario_id)
        pedidos = self.session.execute(consulta).scalars().all()
        return pedidos
    
    
    def listar_minhas_vendas_usuario_id(self,usuario_id:int)->List[models.Pedido]:
        consulta = select(models.Pedido).join_from(models.Pedido, models.Produto).where(models.Produto.usuario_id == usuario_id)
        pedidos = self.session.execute(consulta).scalars().all()
        return pedidos
 
    def editar(self,id: int,pedido : schemas.Pedido)->models.Pedido:
        update_stmt = update(models.Pedido).where(models.Pedido.id == id).values(
            quantidade = pedido.quantidade,
            local_entrega = pedido.local_entrega,
            tipo_entrega  = pedido.tipo_entrega,
            observacao   = pedido.observacao,
            usuario_id = pedido.usuario_id,
            produto_id = pedido.produto_id,
            usuario = pedido.usuario,
            produto = pedido.produto)
        pedido_update = self.session.execute(update_stmt)
        self.session.commit()
        
    
    def remover(self, id: int):
        delete_stmt = delete(models.Pedido).where(models.Pedido.id == id)
        self.session.execute(delete_stmt)
        self.session.commit()

