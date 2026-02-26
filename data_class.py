from dataclasses import dataclass, asdict, field


@dataclass(frozen=True)

class Persona:
    nombre : str
    edad : int
    estatura : float
    password : str = field(repr=False)
    

juan = Persona("Juan", 30, 1.68, "abcd1234*")
print(juan)
juan.edad = 31

# class Persona_sin_data:
#     def __init__(self, nombre : str, edad : int, estatura : float):
#         self.nombre = nombre
#         self.edad = edad
#         self.estatura = estatura
#     def __repr__(self):
#         return f"Persona_sin_data(nombre='{self.nombre}' edad={self.edad} estatura={self.estatura})"
# carlos = Persona_sin_data("Carlos", 30, 1.68)
# print(carlos)