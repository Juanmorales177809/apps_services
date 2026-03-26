from models.laboratorios import Laboratorio
from sqlalchemy.orm import Session
from schemas.laboratorios import LaboratorioBase



def get_all(db: Session):
    labs = db.query(Laboratorio).all()
    return labs

def get_by_id(db: Session, id_laboratorio : int):
    laboratorio = db.query(Laboratorio).filter(
        Laboratorio.idLaboratorio == id_laboratorio
    ).first()
    return laboratorio

def create(db: Session, data:LaboratorioBase):
    nuevo_laboratorio = Laboratorio(
        nombre=data.nombre,
        ubicacion=data.ubicacion,
        tipo=data.tipo        
    )
    db.add(nuevo_laboratorio)
    db.commit()
    db.refresh(nuevo_laboratorio)
    return nuevo_laboratorio

def update(db: Session, id_laboratorio, data: Laboratorio):
    laboratorio = db.query(Laboratorio).filter(
        Laboratorio.idLaboratorio == id_laboratorio
    ).first()
    if laboratorio is None:
        return None
    laboratorio.nombre = data.nombre
    laboratorio.ubicacion = data.ubicacion
    laboratorio.tipo = data.tipo
    db.commit()
    db.refresh(laboratorio)
    return laboratorio
