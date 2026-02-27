"""
script_05_funciones.py

Objetivo:
- Entender qué es una función y por qué se usa
- Parámetros y argumentos
- return (devolver valores)
- Alcance (scope) básico
- Valores por defecto
- *args y **kwargs (sin magia negra, bien explicado)

"""

# ============================================================
# 1) ¿QUÉ ES UNA FUNCIÓN?
# ============================================================
# Una función es un bloque de código reutilizable.
# Sirve para:
# - evitar repetición (copiar/pegar)
# - organizar el programa
# - hacer el código más legible y mantenible


# ============================================================
# 2) FUNCIÓN SIN PARÁMETROS
# ============================================================
def saludo_basico():
    """
    No recibe nada.
    Solo ejecuta una acción.
    """
    print("Hola. Esta es una función sin parámetros.")


print("=== 2) FUNCIÓN SIN PARÁMETROS ===")
saludo_basico()


# ============================================================
# 3) FUNCIÓN CON PARÁMETROS
# ============================================================
def saludar(nombre):
    """
    Recibe un parámetro: nombre (str)
    """
    print(f"Hola {nombre}.")


print("\n=== 3) FUNCIÓN CON PARÁMETROS ===")
saludar("Ana")
saludar("Juan")


# ============================================================
# 4) FUNCIÓN QUE DEVUELVE VALOR (return)
# ============================================================
def sumar(a, b):
    """
    Devuelve la suma de a y b.
    Importante:
    - return termina la función y envía el resultado al que llama.
    """
    return a + b


print("\n=== 4) FUNCIÓN CON RETURN ===")
resultado = sumar(10, 5)
print("sumar(10,5) =", resultado)


# ============================================================
# 5) DIFERENCIA ENTRE print() y return
# ============================================================
def sumar_con_print(a, b):
    """
    Esta función NO devuelve nada útil.
    Solo imprime.
    """
    print("La suma es:", a + b)


print("\n=== 5) print VS return ===")
x = sumar(2, 3)               # x guarda el valor 5
print("x =", x)

y = sumar_con_print(2, 3)     # y será None porque la función no devuelve nada
print("y =", y)


# ============================================================
# 6) PARÁMETROS CON VALOR POR DEFECTO
# ============================================================
def saludar_con_titulo(nombre, titulo="Sr./Sra."):
    """
    titulo tiene un valor por defecto.
    Si no lo mandas, usa "Sr./Sra."
    """
    return f"Hola {titulo} {nombre}."


print("\n=== 6) VALORES POR DEFECTO ===")
print(saludar_con_titulo("Camila"))                 # usa el default
print(saludar_con_titulo("Camila", "Ing."))         # se lo pasamos


# ============================================================
# 7) PARÁMETROS NOMBRADOS (keyword arguments)
# ============================================================
def crear_usuario(nombre, edad, ciudad):
    """
    Recibe 3 datos y devuelve un diccionario.
    """
    return {"nombre": nombre, "edad": edad, "ciudad": ciudad}


print("\n=== 7) ARGUMENTOS NOMBRADOS ===")
u1 = crear_usuario("Juan", 30, "Medellín")
print("u1:", u1)

# Puedes pasar por nombre (sin depender del orden)
u2 = crear_usuario(ciudad="Bogotá", edad=22, nombre="Ana")
print("u2:", u2)


# ============================================================
# 8) SCOPE (ALCANCE) BÁSICO
# ============================================================
# Variables definidas dentro de una función son "locales".
# Variables definidas fuera son "globales".

print("\n=== 8) SCOPE ===")

mensaje = "Estoy afuera (global)"

def mostrar_mensaje():
    mensaje_local = "Estoy adentro (local)"
    print("Dentro:", mensaje_local)
    print("Dentro también puedo leer global:", mensaje)

mostrar_mensaje()
print("Fuera:", mensaje)

# Ojo: si intentas usar mensaje_local fuera, da error:
# print(mensaje_local)  # NameError


# ============================================================
# 9) *args (cantidad variable de argumentos posicionales)
# ============================================================
def sumar_varios(*args):
    """
    args llega como tupla con todos los valores que mandes.
    Ej: sumar_varios(1,2,3) -> args = (1,2,3)
    """
    total = 0
    for n in args:
        total += n
    return total


print("\n=== 9) *args ===")
print("sumar_varios(1,2,3) =", sumar_varios(1, 2, 3))
print("sumar_varios(10,20) =", sumar_varios(10, 20))


# ============================================================
# 10) **kwargs (cantidad variable de argumentos nombrados)
# ============================================================
def imprimir_campos(**kwargs):
    """
    kwargs llega como diccionario con los pares clave=valor.
    Ej: imprimir_campos(nombre='Ana', edad=20)
        kwargs = {'nombre':'Ana', 'edad':20}
    """
    for clave, valor in kwargs.items():
        print(f"{clave} -> {valor}")


print("\n=== 10) **kwargs ===")
imprimir_campos(nombre="Sofía", curso="Web", lenguaje="Python")


# ============================================================
# 11) MINI-EJERCICIO: VALIDAR RANGO CON FUNCIÓN
# ============================================================
def esta_en_rango(valor, minimo, maximo):
    """
    Devuelve True si valor está dentro del rango [minimo, maximo].
    """
    return (valor >= minimo) and (valor <= maximo)


print("\n=== 11) MINI-EJERCICIO ===")
print("5 en [1,10] ->", esta_en_rango(5, 1, 10))
print("20 en [1,10] ->", esta_en_rango(20, 1, 10))


print("\n=== FIN DEL SCRIPT 05 ===")