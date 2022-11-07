
from sqlalchemy import select, update,delete
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class RepositorioUsuario():

    def __init__(self, session: Session):
        self.session = session

    def criar(self,usuario: schemas.Usuario):
        db_usuario = models.Usuario(nome  = usuario.nome,
                                    senha = usuario.senha,
                                    telefone = usuario.telefone)
        self.session.add(db_usuario)
        self.session.commit()
        self.session.refresh(db_usuario)
        return db_usuario

    def listar(self):
        #usuarios = self.session.query(models.Usuario).all()
        stmt = select(models.Usuario)
        usuarios = self.session.execute(stmt).scalars().all()
        return usuarios

    def editar(self,usuario : schemas.Usuario):
        update_stmt = update(models.Usuario).where(models.Usuario.id == usuario.id).values(
            nome  = usuario.nome,
            senha = usuario.senha,
            telefone = usuario.telefone)
        usuario_update = self.db.execute(update_stmt)
        self.db.commit()
        return usuario_update

    def remover(self, id: int):
        delete_stmt = delete(models.Usuario).where(models.Usuario.id == id)
        self.db.execute(delete_stmt)
        self.db.commit()