"""
script_04_condicionales_ciclos_control_flujo.py

Objetivo:
- Entender condicionales (if / elif / else)
- Trabajar con ciclos (for / while)
- Usar break, continue y pass
- Resolver mini-problemas prácticos
"""

# ============================================================
# 1) CONDICIONALES (if / elif / else)
# ============================================================

print("=== 1) CONDICIONALES ===")

numero = int(input("Ingrese un número entero: "))

if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")


# Validación con múltiples condiciones
edad = int(input("\nIngrese su edad: "))

if edad >= 18 and edad <= 65:
    print("Está en edad laboral.")
elif edad < 18:
    print("Es menor de edad.")
else:
    print("Es adulto mayor.")


# ============================================================
# 2) CICLO FOR
# ============================================================

print("\n=== 2) CICLO FOR ===")

print("\nFor con range(5):")
for i in range(5):
    print("i =", i)

print("\nFor con rango específico range(1,6):")
for i in range(1, 6):
    print(i)

print("\nFor con salto range(0,10,2):")
for i in range(0, 10, 2):
    print(i)

# Recorrer lista
numeros = [10, 20, 30, 40]

print("\nRecorriendo lista:")
for n in numeros:
    print(n)


# ============================================================
# 3) CICLO WHILE
# ============================================================

print("\n=== 3) CICLO WHILE ===")

contador = 0

while contador < 5:
    print("contador =", contador)
    contador += 1

# Ejemplo práctico: pedir contraseña hasta que sea correcta
print("\nSimulación de validación de contraseña:")
clave_correcta = "python123"
clave_ingresada = ""

while clave_ingresada != clave_correcta:
    clave_ingresada = input("Ingrese la contraseña: ")

print("Acceso concedido.")


# ============================================================
# 4) CONTROL DE FLUJO: break / continue / pass
# ============================================================

print("\n=== 4) CONTROL DE FLUJO ===")

print("\nEjemplo break:")
for i in range(10):
    if i == 5:
        break
    print(i)

print("\nEjemplo continue:")
for i in range(5):
    if i == 2:
        continue
    print(i)

print("\nEjemplo pass:")
for i in range(3):
    if i == 1:
        pass  # no hace nada
    print(i)


# ============================================================
# 5) MINI PROBLEMA 1: SUMA ACUMULADA
# ============================================================

print("\n=== 5) MINI PROBLEMA: SUMA ACUMULADA ===")

suma = 0

for i in range(1, 6):
    suma += i

print("Suma de 1 a 5 =", suma)


# ============================================================
# 6) MINI PROBLEMA 2: TABLA DE MULTIPLICAR
# ============================================================

print("\n=== 6) MINI PROBLEMA: TABLA DE MULTIPLICAR ===")

numero_tabla = int(input("Ingrese número para tabla: "))

for i in range(1, 11):
    print(f"{numero_tabla} x {i} = {numero_tabla * i}")


# ============================================================
# 7) MINI PROBLEMA 3: CONTAR PARES E IMPARES
# ============================================================

print("\n=== 7) MINI PROBLEMA: PARES E IMPARES ===")

pares = 0
impares = 0

for i in range(1, 11):
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Cantidad de pares del 1 al 10:", pares)
print("Cantidad de impares del 1 al 10:", impares)


print("\n=== FIN DEL SCRIPT 04 ===")