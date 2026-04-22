from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud.usuarios import create, get_all, get_by_email, get_by_id, get_by_username
from db import get_db
from schemas.usuarios import UsuarioCreate, UsuarioResponse
from security.auth import require_scopes


router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"],
)


@router.get(
    "/",
    response_model=list[UsuarioResponse],
    dependencies=[Depends(require_scopes("usuarios:read"))],
)
def listar_usuarios(db: Session = Depends(get_db)):
    return get_all(db)


@router.post(
    "/",
    response_model=UsuarioResponse,
    dependencies=[Depends(require_scopes("usuarios:create"))],
)
def crear_usuario(data: UsuarioCreate, db: Session = Depends(get_db)):
    if get_by_username(db, data.username) is not None:
        raise HTTPException(status_code=400, detail="Username ya registrado")

    if get_by_email(db, data.correo) is not None:
        raise HTTPException(status_code=400, detail="Correo ya registrado")

    return create(db, data)


@router.get(
    "/{id_usuario}",
    response_model=UsuarioResponse,
    dependencies=[Depends(require_scopes("usuarios:read"))],
)
def usuario_id(id_usuario: int, db: Session = Depends(get_db)):
    usuario = get_by_id(db, id_usuario)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario
