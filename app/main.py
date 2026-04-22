from fastapi import FastAPI
from api.auth import router as router_auth
from api.laboratorios import router as router_laboratorios
from api.usuarios import router as router_usuarios


app = FastAPI(
    title="API para servicios web",
    version="0.1",
    description="API desarrollada para el curso de Aplicaciones y servicios"
)

app.include_router(router_auth)
app.include_router(router_laboratorios)
app.include_router(router_usuarios)

@app.get("/")
def root():
    return {"Message": "Status OK"}

