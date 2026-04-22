from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from crud.laboratorios import get_all, get_by_id, create, update
from schemas.laboratorios import LaboratorioBase
from security.auth import require_scopes


router = APIRouter(
    prefix="/laboratorios",
    tags=["Laboratorios"],
)

@router.get("/", dependencies=[Depends(require_scopes("laboratorios:read"))])
def listar_laboratorios(db : Session = Depends(get_db)):
    return get_all(db)

@router.get(
    "/{id_laboratorio}",
    dependencies=[Depends(require_scopes("laboratorios:read"))],
)
def laboratorio_id(id_laboratorio : int, db : Session = Depends(get_db)):
    return get_by_id(db, id_laboratorio)

@router.post("/", dependencies=[Depends(require_scopes("laboratorios:create"))])
def crear_laboratorio(data: LaboratorioBase, db: Session=Depends(get_db)):
    return create(db, data)

@router.put(
    "/{id_laboratorio}",
    dependencies=[Depends(require_scopes("laboratorios:update"))],
)
def actualizar_laboratorio(id_laboratorio: int,data: LaboratorioBase,db: Session = Depends(get_db)):
    laboratorio_actualizado = update(db, id_laboratorio, data)
    if laboratorio_actualizado is None:
        raise HTTPException(status_code=404, detail="Laboratorio no encontrado")
    return laboratorio_actualizado
