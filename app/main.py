from fastapi import FastAPI
from db import engine, Base, session
from schemas.laboratorios import LaboratorioBase
from models.laboratorios import Laboratorio

app = FastAPI(
    title="API para servicios web",
    version="0.1",
    description="API desarrollada para el curso de Aplicaciones y servicios"
)

@app.get("/")
def root():
    return {"Message": "Hola a todos"}

@app.get("/laboratorios", response_model=list[LaboratorioBase])
def listar_laboratorios():
    db = session()
    labs = db.query(Laboratorio).all()
    db.close()
    return labs