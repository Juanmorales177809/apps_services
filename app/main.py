from fastapi import FastAPI, Depends
from db import engine, Base, session, get_db
from schemas.laboratorios import LaboratorioBase
from models.laboratorios import Laboratorio
from sqlalchemy.orm import Session
from crud.laboratorios import *



app = FastAPI(
    title="API para servicios web",
    version="0.1",
    description="API desarrollada para el curso de Aplicaciones y servicios"
)

@app.get("/")
def root():
    return {"Message": "Hola a todos"}

@app.get("/laboratorios")
def listar_laboratorios(db : Session = Depends(get_db)):
    return get_all(db)

@app.get("/laboratorio/{id_laboratorio}")
def laboratorio_id(id_laboratorio : int, db : Session = Depends(get_db)):
    return get_by_id(db, id_laboratorio)
