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
