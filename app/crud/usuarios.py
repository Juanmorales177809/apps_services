from sqlalchemy.orm import Session

from models.usuarios import Usuario
from schemas.usuarios import UsuarioCreate
from security.auth import hash_password


def get_all(db: Session):
    usuarios = db.query(Usuario).all()
    return usuarios


def get_by_id(db: Session, id_usuario: int):
    usuario = db.query(Usuario).filter(
        Usuario.id_usuario == id_usuario
    ).first()
    return usuario


def get_by_email(db: Session, correo: str):
    return db.query(Usuario).filter(Usuario.correo == correo).first()


def get_by_username(db: Session, username: str):
    return db.query(Usuario).filter(Usuario.username == username).first()


def create(db: Session, data: UsuarioCreate):
    nuevo_usuario = Usuario(
        nombre=data.nombre,
        apellido=data.apellido,
        correo=data.correo,
        username=data.username,
        hashed_password=hash_password(data.password),
        rol=data.rol,
        activo=data.activo,
    )

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario
