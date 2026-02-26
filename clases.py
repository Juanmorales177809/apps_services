# from pydantic import BaseModel


# class Persona(BaseModel):
#     nombre : str
#     apellido: str
#     edad: int
    
# juan = Persona(nombre="Juan", apellido="Morales", edad=30)
# print(juan)


from dataclasses import dataclass

@dataclass
class Persona:
    nombre : str
    apellido: str
    edad: int

juan = Persona(nombre="Juan", apellido="Morales", edad=30)   
print(juan)




# class Persona:
#     def __init__(self, nombre, apellido, edad):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
    
#     def representar(self):
#         return f"nombre = {self.nombre}, apellido = {self.apellido}, edad={self.edad}"
# carlos = Persona("Carlos", "Guerra", 30)
# print(carlos.representar())