"""
script_serializacion_deserializacion.py

Objetivo:
Mostrar cómo convertir datos entre estructuras de Python y JSON.

Conceptos clave:
- Serialización: convertir un objeto Python → JSON
- Deserialización: convertir JSON → objeto Python

Esto es fundamental para APIs web porque:
- El servidor trabaja con objetos Python
- El cliente envía y recibe datos en JSON
"""

import json
from dataclasses import dataclass
from pydantic import BaseModel


print("=================================================")
print("1) SERIALIZACIÓN Y DESERIALIZACIÓN BÁSICA CON JSON")
print("=================================================")

# Diccionario Python
persona = {
    "nombre": "Juan",
    "edad": 30
}

print("Objeto Python:", persona)

# SERIALIZACIÓN → Python → JSON
persona_json = json.dumps(persona)

print("JSON:", persona_json)
print("Tipo:", type(persona_json))

# DESERIALIZACIÓN → JSON → Python
persona_dict = json.loads(persona_json)

print("Objeto nuevamente:", persona_dict)
print("Tipo:", type(persona_dict))


print("\n=================================================")
print("2) SERIALIZACIÓN CON POO TRADICIONAL")
print("=================================================")


class PersonaPOO:
    """
    Con POO puro debemos crear manualmente
    funciones de serialización.
    """

    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre = nombre
        self.edad = edad

    def to_dict(self) -> dict:
        return {
            "nombre": self.nombre,
            "edad": self.edad
        }


persona_poo = PersonaPOO("Ana", 25)

# Convertimos a diccionario
persona_dict = persona_poo.to_dict()

# Convertimos a JSON
persona_json = json.dumps(persona_dict)

print("Objeto:", persona_poo.__dict__)
print("JSON:", persona_json)


print("\n=================================================")
print("3) SERIALIZACIÓN CON DATACLASS")
print("=================================================")


@dataclass
class PersonaDataclass:
    nombre: str
    edad: int


persona_dc = PersonaDataclass("Luis", 40)

# Dataclass necesita conversión a dict
from dataclasses import asdict

persona_dict = asdict(persona_dc)
persona_json = json.dumps(persona_dict)

print("Objeto:", persona_dc)
print("Dict:", persona_dict)
print("JSON:", persona_json)


print("\n=================================================")
print("4) SERIALIZACIÓN CON PYDANTIC")
print("=================================================")


class PersonaPydantic(BaseModel):
    nombre: str
    edad: int


persona_py = PersonaPydantic(nombre="Carlos", edad=35)

# Convertir a dict
persona_dict = persona_py.model_dump()

# Convertir a JSON
persona_json = persona_py.model_dump_json()

print("Objeto:", persona_py)
print("Dict:", persona_dict)
print("JSON:", persona_json)


print("\n=================================================")
print("5) DESERIALIZACIÓN CON PYDANTIC")
print("=================================================")

json_data = '{"nombre": "Laura", "edad": "28"}'

# Pydantic convierte JSON → objeto
persona = PersonaPydantic.model_validate_json(json_data)

print("Objeto creado desde JSON:", persona)
print("Edad:", persona.edad)
print("Tipo edad:", type(persona.edad))


print("\n=================================================")
print("RESUMEN")
print("=================================================")
print("POO puro -> serialización manual.")
print("Dataclass -> usar asdict().")
print("Pydantic -> incluye serialización y deserialización.")