

from email.mime import base
from sqlalchemy import Column, Integer, String, Float, Boolean
from src.infra.sqlalchemy.config.database import Base

class Produto(Base):

    __tablename__= 'Produto'

    id = Column(Integer, primary_key=True, index=True) 
    nome = Column(String)
    detalhes = Column(String)
    preco = Column(Float)
    disponivel = Column(Boolean)