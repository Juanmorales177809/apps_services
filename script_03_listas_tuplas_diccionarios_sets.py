"""
script_03_listas_tuplas_diccionarios_sets.py

Objetivo:
- Profundizar en listas (lo más usado en Python)
- Recorrer estructuras
- Ordenar datos
- Copias y errores comunes
- Listas anidadas
- Repaso práctico de tuplas, diccionarios y sets
"""

# ============================================================
# 1) LISTAS (LIST) - PROFUNDIZANDO
# ============================================================

print("=== 1) LISTAS ===")

numeros = [5, 2, 9, 1, 5, 6]
print("Lista original:", numeros)

# Acceso por índice
print("Primer elemento:", numeros[0])
print("Último elemento:", numeros[-1])

# Modificar elemento
numeros[1] = 200
print("Modificando índice 1 ->", numeros)

# Longitud
print("Cantidad de elementos (len):", len(numeros))

# ============================================================
# 2) RECORRER LISTAS
# ============================================================

print("\n=== 2) RECORRER LISTAS ===")

print("Recorrido simple:")
for n in numeros:
    print("Elemento:", n)

print("\nRecorrido con índice (range + len):")
for i in range(len(numeros)):
    print("Índice:", i, "| Valor:", numeros[i])

print("\nRecorrido con enumerate (mejor práctica):")
for indice, valor in enumerate(numeros):
    print("Índice:", indice, "| Valor:", valor)


# ============================================================
# 3) MÉTODOS IMPORTANTES DE LISTA
# ============================================================

print("\n=== 3) MÉTODOS DE LISTA ===")

datos = [10, 30, 20, 40]
print("datos:", datos)

datos.append(50)
print("append(50):", datos)

datos.extend([60, 70])
print("extend([60,70]):", datos)

datos.insert(1, 999)
print("insert(1, 999):", datos)

datos.remove(999)
print("remove(999):", datos)

ultimo = datos.pop()
print("pop():", ultimo, "| lista quedó:", datos)

print("index(20):", datos.index(20))
print("count(10):", datos.count(10))


# ============================================================
# 4) ORDENAR LISTAS
# ============================================================

print("\n=== 4) ORDENAR LISTAS ===")

lista = [4, 2, 8, 1]
print("Original:", lista)

lista.sort()
print("sort() ascendente:", lista)

lista.sort(reverse=True)
print("sort(reverse=True):", lista)

# sorted() crea una nueva lista
otra = [7, 3, 9]
ordenada = sorted(otra)
print("otra:", otra)
print("sorted(otra):", ordenada)


# ============================================================
# 5) SLICING EN LISTAS
# ============================================================

print("\n=== 5) SLICING EN LISTAS ===")

valores = [0, 1, 2, 3, 4, 5]
print("valores:", valores)
print("valores[1:4]:", valores[1:4])
print("valores[:3]:", valores[:3])
print("valores[3:]:", valores[3:])
print("valores[::-1]:", valores[::-1])  # reversa


# ============================================================
# 6) COPIAS DE LISTAS (ERROR CLÁSICO)
# ============================================================

print("\n=== 6) COPIAS DE LISTAS ===")

lista_original = [1, 2, 3]
lista_copia_mala = lista_original   # referencia, NO copia real

lista_copia_mala[0] = 999

print("lista_original:", lista_original)
print("lista_copia_mala:", lista_copia_mala)
print("Ambas cambiaron porque apuntan al mismo objeto.")

# Copia correcta
lista_original = [1, 2, 3]
lista_copia_buena = lista_original.copy()

lista_copia_buena[0] = 999

print("lista_original:", lista_original)
print("lista_copia_buena:", lista_copia_buena)


# ============================================================
# 7) LISTAS ANIDADAS (MATRICES BÁSICAS)
# ============================================================

print("\n=== 7) LISTAS ANIDADAS ===")

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("matriz:", matriz)
print("Elemento fila 1 columna 2:", matriz[1][2])

print("Recorriendo matriz:")
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()


# ============================================================
# 8) TUPLAS (RECORDATORIO)
# ============================================================

print("\n=== 8) TUPLAS ===")

coordenadas = (10, 20)
print("coordenadas:", coordenadas)
print("coordenadas[0]:", coordenadas[0])

# Desempaquetado
x, y = coordenadas
print("x =", x, "| y =", y)


# ============================================================
# 9) DICCIONARIOS (DICT)
# ============================================================

print("\n=== 9) DICCIONARIOS ===")

persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Medellín"
}

print("persona:", persona)
print("persona['nombre']:", persona["nombre"])

# Recorrer claves
for clave in persona:
    print("Clave:", clave)

# Recorrer clave-valor
for clave, valor in persona.items():
    print("Clave:", clave, "| Valor:", valor)

# Métodos útiles
print("Keys:", list(persona.keys()))
print("Values:", list(persona.values()))

# Acceso seguro
print("get('correo'):", persona.get("correo"))


# ============================================================
# 10) SETS (CONJUNTOS)
# ============================================================

print("\n=== 10) SETS ===")

a = {1, 2, 3}
b = {3, 4, 5}

print("a:", a)
print("b:", b)

print("Unión (a | b):", a | b)
print("Intersección (a & b):", a & b)
print("Diferencia (a - b):", a - b)

print("=== FIN DEL SCRIPT 03 ===")