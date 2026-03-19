# Inyección de Dependencias (DI) en FastAPI

## Descripción

En esta clase se abordó el concepto de **Inyección de Dependencias (Dependency Injection - DI)** en FastAPI, como una técnica clave para construir aplicaciones limpias, reutilizables y mantenibles.

El objetivo es entender cómo FastAPI permite **inyectar recursos automáticamente** en los endpoints, evitando manejar manualmente aspectos como conexiones a base de datos.

---

## Problema inicial

En un enfoque tradicional, cada endpoint maneja directamente la conexión a la base de datos:

```python
@app.get("/laboratorios")
def listar_laboratorios():
    db = session()
    labs = db.query(Laboratorio).all()
    db.close()
    return labs

## Problemas

- Código repetido en múltiples endpoints  
- Riesgo de olvidar cerrar la conexión  
- Mezcla de lógica de negocio con infraestructura  

El endpoint hace más de lo que debería.

---

## ¿Qué es Inyección de Dependencias?

Una dependencia es cualquier recurso o lógica que una función necesita para ejecutarse.

### Ejemplos

- Conexión a base de datos  
- Usuario autenticado  
- Configuración  
- Validaciones  

### Idea clave

No crees lo que necesitas, recíbelo.

FastAPI se encarga de proporcionar automáticamente esas dependencias.

## Flujo completo de ejecución

1. FastAPI detecta `Depends(get_db)`  
2. Ejecuta `get_db()`  
3. Llega a `yield db`  
4. Inyecta `db` en el endpoint  
5. Ejecuta el endpoint  
6. Finaliza el endpoint  
7. Ejecuta `db.close()`  

---

## Antes vs Después

### Sin DI

```python
def listar_laboratorios():
    db = session()
    labs = db.query(Laboratorio).all()
    db.close()
    return labs

### Con DI

```python
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


## Beneficios de usar DI

- Código más limpio  
- Reutilización de lógica  
- Menos errores (manejo automático)  
- Separación de responsabilidades  
- Mejor mantenimiento  

---

## Otros usos de DI

FastAPI utiliza DI para:

- Autenticación (JWT, OAuth2)  
- Validación de permisos  
- Configuración global  
- Servicios reutilizables  

---

## Conclusión

La Inyección de Dependencias permite que los endpoints se enfoquen únicamente en la lógica de negocio, delegando la gestión de recursos a FastAPI.

El endpoint se enfoca en el negocio, FastAPI maneja la infraestructura.