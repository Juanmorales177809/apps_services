# Curso: Aplicaciones y Servicios Web (Python + FastAPI)

Este repositorio contiene **todo el material del curso**:
- Código desarrollado en clase
- Ejercicios y talleres
- Tareas y guías
- Recursos de apoyo (cuando aplique)

## Cómo se organiza el repositorio

- La rama **`main`** funciona como punto de entrada: aquí están las instrucciones, el índice del curso y enlaces a las ramas.
- Cada clase tendrá su **propia rama**, con el código y material correspondiente.

## Ramas del curso (ruta por clases)

> Nota: si en una clase no alcanzamos a terminar un tema, se continúa en la siguiente rama.

| Clase | Tema | Rama |
|------:|------|------|
| 01 | Python básico (repaso rápido) | `clase-01-python-basico` |
| 02 | FastAPI: primer proyecto y Hello World | `clase-02-fastapi-hello-world` |
| 03 | Modelos de datos: Pydantic y dataclasses | `clase-03-modelos-pydantic-y-dataclasses` |

## Cómo cambiarte a la rama de una clase

```bash
git fetch --all
git switch clase-03-modelos-pydantic-y-dataclasses