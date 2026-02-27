from fastapi import FastAPI
from pydantic import BaseModel

class Person(BaseModel):
    name : str
    last_name: str
    age : int

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hola mundo "}

@app.post("/personal")
def crear(usuario : Person):
    print(usuario)
    return True