from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud.usuarios import get_all, get_by_id
from db import get_db
from schemas.usuarios import UsuarioResponse
from security.auth import get_current_user


router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"],
    dependencies=[Depends(get_current_user)],
)


@router.get("/", response_model=list[UsuarioResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    return get_all(db)


@router.get("/{id_usuario}", response_model=UsuarioResponse)
def usuario_id(id_usuario: int, db: Session = Depends(get_db)):
    usuario = get_by_id(db, id_usuario)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario
