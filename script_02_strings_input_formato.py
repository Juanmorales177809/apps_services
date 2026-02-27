"""
script_02_strings_input_formato.py

Objetivo:
- Manejo básico de strings (texto)
- Operaciones comunes con strings
- Entrada por teclado con input()
- Formateo de texto (concatenación y f-strings)
"""

# ============================================================
# 1) STRINGS: QUÉ SON Y CÓMO SE USAN
# ============================================================

print("=== 1) STRINGS ===")

texto1 = "Hola"
texto2 = "Python"

print("texto1 =", texto1, "| tipo:", type(texto1))
print("texto2 =", texto2, "| tipo:", type(texto2))

# Concatenación: unir strings con +
# Ojo: + solo funciona si ambos son strings.
saludo = texto1 + " " + texto2
print("Concatenación (+):", saludo)

# Repetición: multiplicar string por un entero
linea = "-" * 30
print("Repetición ('-'*30):", linea)

# Longitud del texto
print("len(texto2) =", len(texto2))


# ============================================================
# 2) ACCESO POR ÍNDICE Y REBANADO (SLICING)
# ============================================================

print("\n=== 2) ÍNDICES Y SLICING ===")

palabra = "programacion"

# Índices: 0 es el primer carácter
print("palabra =", palabra)
print("palabra[0] =", palabra[0])      # primera letra
print("palabra[1] =", palabra[1])
print("palabra[-1] =", palabra[-1])    # última letra

# Slicing: palabra[inicio:fin] (fin NO se incluye)
print("palabra[0:4] =", palabra[0:4])  # 'prog'
print("palabra[4:7] =", palabra[4:7])  # 'ram'
print("palabra[:5] =", palabra[:5])    # desde 0 hasta 5
print("palabra[5:] =", palabra[5:])    # desde 5 hasta el final

# Saltos: palabra[inicio:fin:paso]
print("palabra[0:12:2] =", palabra[0:12:2])  # cada 2 caracteres
print("palabra[::-1] =", palabra[::-1])      # reversa (truco clásico)


# ============================================================
# 3) STRINGS SON INMUTABLES
# ============================================================

print("\n=== 3) INMUTABILIDAD ===")

# No puedes hacer: palabra[0] = 'P'  (eso da error)
# La forma correcta es crear un nuevo string:
nueva_palabra = "P" + palabra[1:]
print("original =", palabra)
print("nueva    =", nueva_palabra)


# ============================================================
# 4) MÉTODOS ÚTILES DE STRINGS
# ============================================================

print("\n=== 4) MÉTODOS ÚTILES ===")

cadena = "  Hola, FastAPI y Pydantic  "
print("cadena original:", repr(cadena))

# strip(): quita espacios al inicio y final
print("strip():", repr(cadena.strip()))

# lower()/upper(): minúsculas / mayúsculas
print("lower():", cadena.lower())
print("upper():", cadena.upper())

# replace(): reemplaza texto
print("replace('FastAPI', 'Python'):", cadena.replace("FastAPI", "Python"))

# startswith()/endswith(): valida inicio/fin
print("startswith('  Hola'):", cadena.startswith("  Hola"))
print("endswith('  '):", cadena.endswith("  "))

# find(): busca y devuelve índice (o -1 si no existe)
print("find('Pydantic'):", cadena.find("Pydantic"))
print("find('Django'):", cadena.find("Django"))

# split(): separa en lista según un separador
csv = "ana,juan,sofia"
lista_nombres = csv.split(",")
print("split(','):", lista_nombres, "| tipo:", type(lista_nombres))

# join(): une lista de strings con separador
unido = " | ".join(lista_nombres)
print("join():", unido)

# count(): cuenta ocurrencias
frase = "hola hola hola"
print("count('hola'):", frase.count("hola"))


# ============================================================
# 5) COMPARACIÓN DE STRINGS (CASO COMÚN)
# ============================================================

print("\n=== 5) COMPARAR STRINGS ===")

usuario = "Admin"
entrada = "admin"

# Si comparas directo, "Admin" != "admin"
print("Comparación directa:", usuario == entrada)

# Lo normal: normalizar con lower()
print("Normalizando lower():", usuario.lower() == entrada.lower())


# ============================================================
# 6) INPUT(): ENTRADA POR TECLADO
# ============================================================

print("\n=== 6) INPUT() ===")

# input() SIEMPRE devuelve str, aunque el usuario escriba números.
nombre_ingresado = input("Escribe tu nombre: ")
print("Ingresaste:", nombre_ingresado, "| tipo:", type(nombre_ingresado))

edad_texto = input("Escribe tu edad (número): ")
print("edad_texto:", edad_texto, "| tipo:", type(edad_texto))

# Para convertir a int/float, toca hacer casting:
# Ojo: si el usuario escribe algo no numérico, esto falla.
edad_int = int(edad_texto)
print("edad_int:", edad_int, "| tipo:", type(edad_int))

# Ejemplo con float
altura_texto = input("Escribe tu estatura (ej: 1.72): ")
altura_float = float(altura_texto)
print("altura_float:", altura_float, "| tipo:", type(altura_float))


# ============================================================
# 7) FORMATEO DE TEXTO (RECOMENDADO: f-strings)
# ============================================================

print("\n=== 7) FORMATEO ===")

# Concatenación (funciona, pero se vuelve fea rápido)
mensaje1 = "Nombre: " + nombre_ingresado + " | Edad: " + str(edad_int)
print("Concatenación:", mensaje1)

# f-strings (recomendado): más limpio
mensaje2 = f"Nombre: {nombre_ingresado} | Edad: {edad_int} | Estatura: {altura_float}"
print("f-string:", mensaje2)

# Formateo numérico: limitar decimales
print(f"Estatura con 2 decimales: {altura_float:.2f}")

# Alineación simple (útil para reportes en consola)
print(f"{'Campo':<10} | {'Valor':<15}")
print(f"{'-'*10} | {'-'*15}")
print(f"{'Nombre':<10} | {nombre_ingresado:<15}")
print(f"{'Edad':<10} | {edad_int:<15}")
print(f"{'Altura':<10} | {altura_float:<15.2f}")


print("\n=== FIN DEL SCRIPT 02 ===")