"""
script_06_poo_tipado.py

Objetivo:
- Introducción a Programación Orientada a Objetos (POO) en Python
- Clases, objetos, atributos y métodos
- Constructor __init__
- Tipado (type hints) en atributos, parámetros y retornos
- Encapsulamiento básico (convención con _ y properties)
- Métodos de clase y métodos estáticos
- Composición (objetos dentro de objetos)

Notas importantes:
- El tipado en Python es para documentación y herramientas (linters/IDE),
  no obliga en tiempo de ejecución (a menos que uses validadores externos).
- La POO sirve para modelar "cosas" con estado (datos) + comportamiento (métodos).
"""

from __future__ import annotations  # permite referenciar clases aún no definidas en type hints


# ============================================================
# 1) CLASE BÁSICA: Usuario
# ============================================================

class Usuario:
    """
    Representa un usuario del sistema.

    Atributos:
        nombre (str): Nombre del usuario.
        correo (str): Correo electrónico.
        activo (bool): Estado del usuario.

    Métodos:
        desactivar() -> None
        activar() -> None
        resumen() -> str
    """

    # Tipado de atributos de instancia (se asignan en __init__)
    nombre: str
    correo: str
    activo: bool

    def __init__(self, nombre: str, correo: str, activo: bool = True) -> None:
        self.nombre = nombre
        self.correo = correo
        self.activo = activo

    def desactivar(self) -> None:
        self.activo = False

    def activar(self) -> None:
        self.activo = True

    def resumen(self) -> str:
        estado: str = "activo" if self.activo else "inactivo"
        return f"Usuario(nombre={self.nombre}, correo={self.correo}, estado={estado})"


print("=== 1) CLASE BÁSICA ===")
u1: Usuario = Usuario("Ana", "ana@ejemplo.com")
print(u1.resumen())
u1.desactivar()
print(u1.resumen())


# ============================================================
# 2) MÉTODOS QUE DEVUELVEN VALORES TIPADOS
# ============================================================

class Calculadora:
    """
    Ejemplo simple de clase con métodos que devuelven tipos específicos.
    """

    def sumar(self, a: int, b: int) -> int:
        return a + b

    def dividir(self, a: float, b: float) -> float:
        # Validación mínima: evitar división por cero
        if b == 0:
            raise ValueError("No se puede dividir por cero.")
        return a / b


print("\n=== 2) MÉTODOS CON TIPADO DE RETORNO ===")
calc: Calculadora = Calculadora()
print("sumar(2,3) ->", calc.sumar(2, 3))
print("dividir(10,4) ->", calc.dividir(10, 4))


# ============================================================
# 3) ENCAPSULAMIENTO BÁSICO (convención + property)
# ============================================================
# Python no tiene "private" real como Java, pero se usa convención:
# - _saldo: "uso interno"
# Y si quieres control, usas @property para leer/validar.

class CuentaBancaria:
    """
    Modelo de una cuenta bancaria con encapsulamiento básico.

    Atributos:
        titular (str): Nombre del titular.
        _saldo (float): Saldo interno (no se recomienda acceder directo).

    Propiedades:
        saldo -> float (solo lectura)
    Métodos:
        depositar(monto: float) -> None
        retirar(monto: float) -> bool
    """

    titular: str
    _saldo: float

    def __init__(self, titular: str, saldo_inicial: float = 0.0) -> None:
        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo.")
        self.titular = titular
        self._saldo = saldo_inicial

    @property
    def saldo(self) -> float:
        """
        Permite leer el saldo como atributo:
        cuenta.saldo
        """
        return self._saldo

    def depositar(self, monto: float) -> None:
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser mayor que 0.")
        self._saldo += monto

    def retirar(self, monto: float) -> bool:
        """
        Intenta retirar un monto.
        Retorna:
            True si se pudo retirar
            False si no hay saldo suficiente
        """
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser mayor que 0.")
        if monto > self._saldo:
            return False
        self._saldo -= monto
        return True


print("\n=== 3) ENCAPSULAMIENTO CON property ===")
cuenta: CuentaBancaria = CuentaBancaria("Juan", 100.0)
print("Saldo:", cuenta.saldo)
cuenta.depositar(50.0)
print("Saldo:", cuenta.saldo)
ok: bool = cuenta.retirar(200.0)
print("¿Pudo retirar 200? ->", ok, "| saldo:", cuenta.saldo)
ok = cuenta.retirar(80.0)
print("¿Pudo retirar 80? ->", ok, "| saldo:", cuenta.saldo)


# ============================================================
# 4) HERENCIA (reutilizar y especializar)
# ============================================================

class Empleado:
    """
    Clase base para empleados.
    """

    nombre: str
    salario_base: float

    def __init__(self, nombre: str, salario_base: float) -> None:
        self.nombre = nombre
        self.salario_base = salario_base

    def calcular_salario(self) -> float:
        """
        Por defecto, salario = salario_base
        """
        return self.salario_base

    def info(self) -> str:
        return f"Empleado(nombre={self.nombre}, salario={self.calcular_salario():.2f})"


class EmpleadoConBono(Empleado):
    """
    Hereda de Empleado y agrega un bono fijo.
    """

    bono: float

    def __init__(self, nombre: str, salario_base: float, bono: float) -> None:
        super().__init__(nombre, salario_base)
        self.bono = bono

    def calcular_salario(self) -> float:
        return self.salario_base + self.bono


print("\n=== 4) HERENCIA ===")
e1: Empleado = Empleado("Ana", 3000.0)
e2: EmpleadoConBono = EmpleadoConBono("Juan", 3000.0, 500.0)
print(e1.info())
print(e2.info())


# ============================================================
# 5) MÉTODOS DE CLASE Y MÉTODOS ESTÁTICOS
# ============================================================

class Persona:
    """
    Ejemplo de:
    - @classmethod: trabaja con la clase (cls)
    - @staticmethod: utilidad relacionada, pero no usa self ni cls
    """

    nombre: str
    edad: int

    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def desde_texto(cls, linea: str) -> Persona:
        """
        Crea una Persona a partir de un texto tipo: "Nombre,Edad"
        Retorna:
            Persona
        """
        partes: list[str] = linea.split(",")
        nombre: str = partes[0].strip()
        edad: int = int(partes[1].strip())
        return cls(nombre, edad)

    @staticmethod
    def es_mayor_de_edad(edad: int) -> bool:
        return edad >= 18


print("\n=== 5) classmethod y staticmethod ===")
p1: Persona = Persona.desde_texto("Sofía, 19")
print("p1:", p1.nombre, p1.edad)
print("¿Sofía es mayor de edad? ->", Persona.es_mayor_de_edad(p1.edad))


# ============================================================
# 6) COMPOSICIÓN (objetos dentro de objetos)
# ============================================================

class Producto:
    """
    Producto con nombre y precio.
    """
    nombre: str
    precio: float

    def __init__(self, nombre: str, precio: float) -> None:
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.nombre = nombre
        self.precio = precio


class Carrito:
    """
    Carrito que contiene productos (composición).
    """
    items: list[Producto]

    def __init__(self) -> None:
        self.items = []

    def agregar(self, producto: Producto) -> None:
        self.items.append(producto)

    def total(self) -> float:
        total: float = 0.0
        for p in self.items:
            total += p.precio
        return total

    def resumen(self) -> str:
        nombres: list[str] = [p.nombre for p in self.items]
        return f"Carrito(items={nombres}, total={self.total():.2f})"


print("\n=== 6) COMPOSICIÓN ===")
carrito: Carrito = Carrito()
carrito.agregar(Producto("Teclado", 120.0))
carrito.agregar(Producto("Mouse", 50.0))
print(carrito.resumen())


print("\n=== FIN DEL SCRIPT 06 ===")