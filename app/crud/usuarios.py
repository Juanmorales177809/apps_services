from sqlalchemy.orm import Session

from models.usuarios import Usuario


def get_all(db: Session):
    usuarios = db.query(Usuario).all()
    return usuarios


def get_by_id(db: Session, id_usuario: int):
    usuario = db.query(Usuario).filter(
        Usuario.id_usuario == id_usuario
    ).first()
    return usuario
