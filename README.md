# Clase 02 – FastAPI: Primer Servicio Web (Hello World)

En esta clase iniciamos el desarrollo de servicios web usando **FastAPI**.

El objetivo es comprender qué es un framework web moderno, por qué se utiliza en este curso y cómo crear nuestro primer servicio HTTP funcional.

---

## ¿Qué es FastAPI?

FastAPI es un framework moderno para construir APIs con Python.

Se caracteriza por:

- Alto rendimiento (basado en Starlette y Pydantic)
- Uso de tipado (type hints) nativo de Python
- Validación automática de datos
- Documentación automática (Swagger y ReDoc)
- Diseño limpio y fácil de escalar

Es ampliamente utilizado en:

- Backend de aplicaciones web
- Microservicios
- APIs para Machine Learning
- Sistemas distribuidos

---

## ¿Por qué FastAPI en este curso?

Este curso no busca solo “hacer backend”, sino aprender arquitectura limpia y buenas prácticas desde el inicio.

FastAPI es ideal porque:

- Obliga a usar tipado (documentación clara)
- Genera documentación automática
- Es simple para empezar
- Escala bien para proyectos reales
- Se integra fácilmente con bases de datos y microservicios

Además, en cursos posteriores lo usaremos junto con:
- Pydantic
- Docker
- Bases de datos
- Arquitectura modular

---

## Recursos Oficiales

Documentación oficial:

https://fastapi.tiangolo.com/

Video recomendado (introducción práctica):

https://www.youtube.com/watch?v=mpR8ngthqiE

---

## Objetivo de la Clase

Al finalizar esta clase el estudiante debe poder:

- Instalar FastAPI
- Crear un proyecto básico
- Levantar un servidor local
- Crear un endpoint tipo "Hello World"
- Acceder a la documentación automática
- Entender el flujo básico HTTP



# 1️⃣ Entorno Virtual (venv)

Trabajar con entorno virtual es obligatorio en proyectos profesionales.  
Permite aislar dependencias por proyecto.

---

## 🔹 Crear entorno virtual

Desde la carpeta del proyecto:

```bash
python -m venv venv
```

Esto crea una carpeta llamada `venv` con el entorno aislado.

---

## 🔹 Activar entorno virtual

### En Git Bash (recomendado en Windows)

```bash
source venv/Scripts/activate
```

### En CMD (Windows)

```bash
venv\Scripts\activate
```

### En Linux / Mac

```bash
source venv/bin/activate
```

Cuando el entorno está activo, verás algo como:

```
(venv)
```

al inicio de la línea de comandos.

---

## 🔹 Desactivar entorno virtual

```bash
deactivate
```

---

## 🔹 ¿Por qué usar Git Bash?

Se recomienda usar **Git Bash** en Windows porque:

- Usa comandos estilo Linux
- Evita inconsistencias entre CMD y PowerShell
- Es el entorno más común en proyectos reales
- Facilita trabajo futuro con Docker y servidores Linux

---

# 2️⃣ Instalación de FastAPI

Con el entorno virtual activado:

```bash
pip install fastapi uvicorn
```

- `fastapi` → framework web
- `uvicorn` → servidor ASGI para ejecutar la aplicación

---

# 3️⃣ Primer Servicio – main.py

Crear archivo `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root() -> dict:
    return {"message": "Hello World"}
```

---

## 🔍 Explicación del Código

### `from fastapi import FastAPI`

Importa la clase principal del framework.

---

### `app = FastAPI()`

Crea la aplicación web.

Esta instancia es el núcleo del servicio.

---

### `@app.get("/")`

Decorador que indica:

- Método HTTP: GET
- Ruta: `/`
- Cuando alguien visite esa ruta, se ejecuta la función debajo.

---

### `def root() -> dict:`

Función que maneja la petición.

- `root` → nombre de la función (puede ser cualquier nombre).
- `-> dict` → tipado del retorno (documentación).
- Devuelve un diccionario.
- FastAPI lo convierte automáticamente a JSON.

---

### `return {"message": "Hello World"}`

Respuesta en formato JSON:

```json
{
  "message": "Hello World"
}
```

---

# 4️⃣ Levantar el Servidor

Desde la consola (con entorno virtual activo):

```bash
uvicorn main:app --reload
```

---

## 🔍 Explicación del comando

- `main` → nombre del archivo (main.py)
- `app` → instancia de FastAPI
- `--reload` → reinicia automáticamente al guardar cambios

---

# 5️⃣ Probar el Servicio

Abrir navegador:

```
http://127.0.0.1:8000/
```

Documentación automática:

```
http://127.0.0.1:8000/docs
```

Documentación alternativa:

```
http://127.0.0.1:8000/redoc
```

---

# 🎯 Resultado de la Clase

Al finalizar esta práctica debes:

- Crear y activar un entorno virtual
- Instalar dependencias
- Crear un archivo main.py
- Definir un endpoint básico
- Levantar un servidor web
- Acceder a la documentación automática

---

En la siguiente clase agregaremos:

- Parámetros en rutas
- Query parameters
- Validación con tipado
- Introducción a Pydantic