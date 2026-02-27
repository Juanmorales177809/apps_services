"""
script_01_tipos_operadores_estructuras.py

Objetivo:
- Ver tipos de datos en Python
- Usar operadores principales
- Conocer estructuras de datos: list, tuple, dict, set

"""

# ============================================================
# 1) TIPOS DE DATOS BÁSICOS
# ============================================================

print("=== 1) TIPOS DE DATOS ===")

# Enteros (int)
edad = 30
print("edad =", edad, "| tipo:", type(edad))

# Decimales (float)
estatura = 1.72
print("estatura =", estatura, "| tipo:", type(estatura))

# Texto (str)
nombre = "Juan"
print("nombre =", nombre, "| tipo:", type(nombre))

# Booleanos (bool): True / False
es_docente = True
print("es_docente =", es_docente, "| tipo:", type(es_docente))

# None: significa "no hay valor"
dato_vacio = None
print("dato_vacio =", dato_vacio, "| tipo:", type(dato_vacio))

# Conversión de tipos (casting)
print("\n--- Conversión de tipos ---")
numero_texto = "25"
numero_int = int(numero_texto)     # "25" -> 25
numero_float = float(numero_texto) # "25" -> 25.0
print("numero_texto =", numero_texto, "| tipo:", type(numero_texto))
print("int(numero_texto) =", numero_int, "| tipo:", type(numero_int))
print("float(numero_texto) =", numero_float, "| tipo:", type(numero_float))

# Cuidado: si el texto no es numérico, int(...) falla
# int("hola")  # Esto lanzaría error


# ============================================================
# 2) OPERADORES
# ============================================================

print("\n=== 2) OPERADORES ===")

a = 10
b = 3

# 2.1 Operadores aritméticos
print("\n--- Aritméticos ---")
print("a =", a, "b =", b)
print("a + b =", a + b)   # suma
print("a - b =", a - b)   # resta
print("a * b =", a * b)   # multiplicación
print("a / b =", a / b)   # división (siempre float)
print("a // b =", a // b) # división entera (parte entera)
print("a % b =", a % b)   # módulo (residuo)
print("a ** b =", a ** b) # potencia

# 2.2 Operadores de comparación (devuelven bool)
print("\n--- Comparación ---")
print("a == b:", a == b)  # igual
print("a != b:", a != b)  # diferente
print("a > b:", a > b)
print("a >= b:", a >= b)
print("a < b:", a < b)
print("a <= b:", a <= b)

# 2.3 Operadores lógicos (and, or, not)
print("\n--- Lógicos ---")
cond1 = (a > b)     # True
cond2 = (b == 0)    # False
print("cond1 =", cond1)
print("cond2 =", cond2)
print("cond1 and cond2 =", cond1 and cond2)  # True si ambas son True
print("cond1 or cond2  =", cond1 or cond2)   # True si al menos una es True
print("not cond1       =", not cond1)        # invierte True <-> False

# 2.4 Operadores de asignación (actualizan variables)
print("\n--- Asignación compuesta ---")
x = 5
print("x inicial =", x)
x += 2   # x = x + 2
print("x += 2 ->", x)
x *= 3   # x = x * 3
print("x *= 3 ->", x)
x -= 4   # x = x - 4
print("x -= 4 ->", x)

# 2.5 Operadores de pertenencia (in / not in)
print("\n--- Pertenencia (in) ---")
texto = "python"
print("'py' in texto:", "py" in texto)
print("'java' in texto:", "java" in texto)

# 2.6 Operadores de identidad (is / is not)
# Se usan para comparar identidad (si es el mismo objeto en memoria).
# Para comparar valores, casi siempre usa ==.
print("\n--- Identidad (is) ---")
n1 = None
print("n1 is None:", n1 is None)


# ============================================================
# 3) ESTRUCTURAS DE DATOS (ARREGLOS EN PYTHON)
# ============================================================

print("\n=== 3) ESTRUCTURAS DE DATOS ===")

# 3.1 LISTA (list): ordenada y mutable (se puede cambiar)
print("\n--- LIST (lista) ---")
numeros = [10, 20, 30]
print("numeros =", numeros, "| tipo:", type(numeros))
print("primer elemento numeros[0] =", numeros[0])
print("último elemento numeros[-1] =", numeros[-1])

# Modificar un elemento
numeros[1] = 200
print("modificando numeros[1]=200 ->", numeros)

# Agregar elementos
numeros.append(40)         # agrega al final
print("append(40) ->", numeros)

numeros.insert(1, 15)      # inserta en la posición 1
print("insert(1, 15) ->", numeros)

# Eliminar elementos
numeros.remove(15)         # elimina el valor 15 (primera ocurrencia)
print("remove(15) ->", numeros)

ultimo = numeros.pop()     # elimina y devuelve el último
print("pop() devolvió:", ultimo, "| lista quedó:", numeros)

# Longitud de una lista
print("len(numeros) =", len(numeros))

# 3.2 TUPLA (tuple): ordenada e inmutable (no se puede cambiar)
print("\n--- TUPLE (tupla) ---")
coordenadas = (5, 8)
print("coordenadas =", coordenadas, "| tipo:", type(coordenadas))
print("coordenadas[0] =", coordenadas[0])
# coordenadas[0] = 99  # ERROR: no se puede modificar una tupla

# 3.3 DICCIONARIO (dict): clave -> valor
print("\n--- DICT (diccionario) ---")
persona = {"nombre": "Juan", "edad": 30, "ciudad": "Medellín"}
print("persona =", persona, "| tipo:", type(persona))
print("persona['nombre'] =", persona["nombre"])

# Modificar / agregar
persona["edad"] = 31
persona["correo"] = "juan@ejemplo.com"
print("modificando y agregando ->", persona)

# Consultar claves/valores
print("claves:", list(persona.keys()))
print("valores:", list(persona.values()))

# 3.4 SET (conjunto): sin duplicados, sin orden garantizado
print("\n--- SET (conjunto) ---")
ids = {1, 2, 2, 3, 3, 3}
print("ids =", ids, "| tipo:", type(ids))  # repetidos se eliminan

ids.add(10)
print("add(10) ->", ids)

ids.discard(2)  # elimina 2 si existe; si no existe, no falla
print("discard(2) ->", ids)

# Pertenencia en set (rápido)
print("10 in ids:", 10 in ids)
print("999 in ids:", 999 in ids)


print("\n=== FIN DEL SCRIPT 01 ===")