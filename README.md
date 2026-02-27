# Clase 03 – Pydantic, Dataclasses y Primer Repositorio en GitHub

En esta clase abordamos dos herramientas fundamentales para modelado de datos en Python: **Pydantic** y **dataclasses**, y además realizamos el flujo profesional completo para crear un repositorio en GitHub usando autenticación SSH.

---

# 🎯 Objetivos de la Clase

Al finalizar esta clase el estudiante debe ser capaz de:

- Entender qué es Pydantic y para qué se usa.
- Comprender cómo funciona el tipado en Python.
- Comparar Pydantic con dataclasses.
- Crear modelos de datos correctamente tipados.
- Crear un repositorio en GitHub.
- Configurar autenticación SSH.
- Realizar el primer push a GitHub de forma profesional.

---

# 1️⃣ ¿Qué es Pydantic?

**Pydantic** es una biblioteca de Python para validación y modelado de datos usando type hints.

Permite:

- Validar datos automáticamente.
- Convertir tipos automáticamente.
- Documentar entradas y salidas.
- Generar esquemas JSON.
- Integrarse perfectamente con FastAPI.

Es ampliamente usada en:
- APIs modernas
- Microservicios
- Sistemas distribuidos
- Machine Learning
- Arquitecturas backend escalables

---

# 2️⃣ Características Generales de Pydantic

- Basado en type hints nativos de Python.
- Validación automática de tipos.
- Conversión automática (ej: `"25"` → `int`).
- Errores estructurados y claros.
- Compatible con JSON.
- Integración directa con FastAPI.
- Alto rendimiento.

Ejemplo básico:

```python
from pydantic import BaseModel

class Usuario(BaseModel):
    nombre: str
    edad: int

u = Usuario(nombre="Ana", edad="25")
print(u.edad)  # 25 (convertido automáticamente a int)
```

---

# 3️⃣ ¿Qué son las Dataclasses?

Las **dataclasses** son una herramienta estándar de Python (desde 3.7) que simplifica la creación de clases usadas principalmente para almacenar datos.

Ejemplo:

```python
from dataclasses import dataclass

@dataclass
class Usuario:
    nombre: str
    edad: int
```

Genera automáticamente:
- __init__
- __repr__
- __eq__

---

# 4️⃣ Pydantic vs Dataclasses

| Característica | Dataclass | Pydantic |
|---------------|-----------|----------|
| Tipado | Sí | Sí |
| Validación automática | No | Sí |
| Conversión automática de tipos | No | Sí |
| Errores estructurados | No | Sí |
| Integración con FastAPI | No directa | Sí |
| Uso recomendado | Modelos simples internos | APIs y validación externa |

### Conclusión

- **Dataclass** → ideal para modelos internos simples.
- **Pydantic** → ideal para APIs, validación y entrada de datos externos.

En este curso usaremos ambos para entender diferencias, pero FastAPI utiliza Pydantic como estándar.

---

# 5️⃣ Crear un Repositorio en GitHub

## 🔹 Paso 1 – Crear repositorio en GitHub

1. Ir a https://github.com
2. Crear nuevo repositorio
3. NO marcar "Add README"
4. Crear repositorio

---

# 6️⃣ Configurar Clave SSH (Profesional)

## 🔹 ¿Por qué usar SSH?

- Evita escribir usuario y contraseña en cada push.
- Es más seguro.
- Es el estándar en entornos profesionales.
- Permite automatización (CI/CD).
- GitHub ya no recomienda autenticación por contraseña.

---

## 🔹 Generar clave SSH

En Git Bash:

```bash
ssh-keygen -t ed25519 -C "tu_correo@ejemplo.com"
```

Presionar ENTER en todas las opciones.

Se crea en:

```
~/.ssh/id_ed25519
~/.ssh/id_ed25519.pub
```

---

## 🔹 Copiar clave pública

```bash
cat ~/.ssh/id_ed25519.pub
```

Copiar el contenido completo.

---

## 🔹 Agregar clave a GitHub

1. Ir a GitHub → Settings
2. SSH and GPG keys
3. New SSH key
4. Pegar la clave pública
5. Guardar

---

## 🔹 Probar conexión

```bash
ssh -T git@github.com
```

Si funciona, verás:

```
Hi usuario! You've successfully authenticated.
```

---

# 7️⃣ Conectar Proyecto Local con GitHub

En el proyecto local:

```bash
git init
git add .
git commit -m "primer commit"
```

Agregar remoto:

```bash
git remote add origin git@github.com:USUARIO/NOMBRE_REPO.git
```

Subir al repositorio:

```bash
git branch -M main
git push -u origin main
```

---

# 📌 Flujo Profesional Final

1. Crear entorno virtual.
2. Desarrollar código.
3. Usar tipado correctamente.
4. Crear modelos con dataclass o Pydantic.
5. Versionar con Git.
6. Subir a GitHub usando SSH.
7. Trabajar por ramas.

---
