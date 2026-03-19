# 🚀 Inyección de Dependencias (DI) en FastAPI

## 📌 Descripción

En esta clase se abordó el concepto de **Inyección de Dependencias (Dependency Injection - DI)** en FastAPI, como una técnica clave para construir aplicaciones limpias, reutilizables y mantenibles.

El objetivo es entender cómo FastAPI permite **inyectar recursos automáticamente** en los endpoints, evitando manejar manualmente aspectos como conexiones a base de datos.

---

## ⚠️ Problema inicial

En un enfoque tradicional, cada endpoint maneja directamente la conexión a la base de datos:

```python
@app.get("/laboratorios")
def listar_laboratorios():
    db = session()
    labs = db.query(Laboratorio).all()
    db.close()
    return labs