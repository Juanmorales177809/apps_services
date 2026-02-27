"""
script_modelos_basicos.py

Objetivo:
Comparar tres formas básicas de crear un modelo de datos:

1) POO puro
2) Dataclass
3) Pydantic

"""

from dataclasses import dataclass
from pydantic import BaseModel


print("====================================================")
print("1) MODELO CON POO PURO")
print("====================================================")


class UsuarioPOO:
    """
    Modelo simple con POO tradicional.
    No valida tipos automáticamente.
    """

    nombre: str
    edad: int

    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre = nombre
        self.edad = edad


# Creamos usuario con edad como string
u1 = UsuarioPOO("Ana", "25")  # Python NO valida tipo aquí
print("UsuarioPOO edad:", u1.edad, "| tipo:", type(u1.edad))


print("\n====================================================")
print("2) MODELO CON DATACLASS")
print("====================================================")


@dataclass
class UsuarioDataclass:
    """
    Modelo usando @dataclass.
    Tampoco valida tipos automáticamente.
    """

    nombre: str
    edad: int


# Igual que POO, no hay validación automática
u2 = UsuarioDataclass("Ana", "25")
print("UsuarioDataclass edad:", u2.edad, "| tipo:", type(u2.edad))


print("\n====================================================")
print("3) MODELO CON PYDANTIC")
print("====================================================")


class UsuarioPydantic(BaseModel):
    """
    Modelo con Pydantic.
    Valida y convierte tipos automáticamente.
    """

    nombre: str
    edad: int


# Pydantic convierte automáticamente "25" a int
u3 = UsuarioPydantic(nombre="Ana", edad="25")
print("UsuarioPydantic edad:", u3.edad, "| tipo:", type(u3.edad))


print("\nIntentando pasar un valor inválido:")

try:
    UsuarioPydantic(nombre="Ana", edad="abc")
except Exception as e:
    print("Error Pydantic:")
    print(e)


print("\n====================================================")
print("CONCLUSIÓN")
print("====================================================")
print("POO puro -> No valida tipos.")
print("Dataclass -> No valida tipos.")
print("Pydantic -> Valida y convierte automáticamente.")