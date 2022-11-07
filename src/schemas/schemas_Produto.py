
from msilib.schema import Class
from pydantic import BaseModel
from typing import Optional,List


class Usuario(BaseModel):
    
    id: Optional[int] = None
    nome: str
    senha: str
    telefone: str
    #produtos: List[Produto]=[]
    #minhas_vendas: List[Pedido]
    #meus_pedidos: List[Pedido]

    class Config:
       orm_mode = True
class Produto(BaseModel):
    id: Optional[int] = None
    #usuario: Usuario
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False
    usuario_id : int
    usuario: Optional[Usuario]

    class Config:
        orm_mode = True

class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    senha: str
    telefone: str
    produtos: List[Produto]=[]
    #minhas_vendas: List[Pedido]
    #meus_pedidos: List[Pedido]

    class Config:
       orm_mode = True

class Pedido(BaseModel):
    id: Optional[str]= None
   # usuario: Usuario
    produto: Produto
    quantidade: int
    entrega: bool= True
    endereco: str
    observacoes: Optional[str] = 'Sem Observações'







