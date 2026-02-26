
class Persona:
    estatura = 1.68
    def __init__(self,nombre:str, edad: int):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        print(f"Mi nombre es {self.nombre} y mi edad es {self.edad} ")

def caminar(persona : Persona) :
    print(Persona.estatura)
    persona.saludar()       
juan = Persona("Juan", 30)
caminar(juan)