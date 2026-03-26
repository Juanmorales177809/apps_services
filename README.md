# 🧪 Clase: Construcción de API con FastAPI (Routers + CRUD + HTTP Status)

## 🎯 Objetivo de la clase

En esta sesión aprenderás a:

- Organizar una API usando **routers**
- Implementar un **CRUD completo** (GET, POST, PUT, DELETE)
- Entender el flujo de una petición en FastAPI
- Manejar correctamente **códigos de estado HTTP**
- Aplicar buenas prácticas de arquitectura básica

---

## 🧱 Estructura del proyecto

```text
proyecto/
│
├── main.py
├── db.py
├── api/
│   └── laboratorios.py
├── crud/
│   └── laboratorios.py
├── models/
│   └── laboratorios.py
└── schemas/
    └── laboratorios.py
```

---

## 🔄 Flujo de una petición en FastAPI

```text
Cliente → Router → (Validación + Dependencias) → Endpoint → CRUD → Base de datos → Respuesta
```

### Componentes clave:

- **Router**: define las rutas
- **Pydantic**: valida los datos de entrada
- **Depends**: inyección de dependencias (ej: DB)
- **CRUD**: lógica de acceso a datos
- **ORM (SQLAlchemy)**: interacción con la base de datos

---

## 🧩 Routers en FastAPI

Un router permite organizar la API por módulos.

### Ejemplo:

```python
router = APIRouter(
    prefix="/laboratorios",
    tags=["Laboratorios"]
)
```

### Beneficios:

- Organización modular
- Escalabilidad
- Código más limpio
- Mejor documentación en Swagger

---

## 🗂️ CRUD de Laboratorios

### 🔍 GET - Listar

```python
def get_all(db: Session):
    return db.query(Laboratorio).all()
```

---

### 🔎 GET - Por ID

```python
def get_by_id(db: Session, id_laboratorio: int):
    return db.query(Laboratorio).filter(
        Laboratorio.idLaboratorio == id_laboratorio
    ).first()
```

---

### ➕ POST - Crear

```python
def create(db: Session, data: LaboratorioBase):
    nuevo_laboratorio = Laboratorio(
        nombre=data.nombre,
        ubicacion=data.ubicacion,
        tipo=data.tipo
    )
    db.add(nuevo_laboratorio)
    db.commit()
    db.refresh(nuevo_laboratorio)
    return nuevo_laboratorio
```

---

### ✏️ PUT - Actualizar

```python
def update(db: Session, id_laboratorio: int, data: LaboratorioBase):
    laboratorio = db.query(Laboratorio).filter(
        Laboratorio.idLaboratorio == id_laboratorio
    ).first()

    if laboratorio is None:
        return None

    laboratorio.nombre = data.nombre
    laboratorio.ubicacion = data.ubicacion
    laboratorio.tipo = data.tipo

    db.commit()
    db.refresh(laboratorio)
    return laboratorio
```

---

### ❌ DELETE - Eliminar

```python
def delete(db: Session, id_laboratorio: int):
    laboratorio = db.query(Laboratorio).filter(
        Laboratorio.idLaboratorio == id_laboratorio
    ).first()

    if laboratorio is None:
        return None

    db.delete(laboratorio)
    db.commit()

    return laboratorio
```

---

## 🌐 Endpoints

```python
@router.get("/")
def listar_laboratorios(...)

@router.get("/{id_laboratorio}")
def laboratorio_id(...)

@router.post("/")
def crear_laboratorio(...)

@router.put("/{id_laboratorio}")
def actualizar_laboratorio(...)

@router.delete("/{id_laboratorio}")
def eliminar_laboratorio(...)
```

---

## 📦 Schema (Pydantic)

```python
from pydantic import BaseModel

class LaboratorioBase(BaseModel):
    nombre: str
    ubicacion: str
    tipo: str
```

---

## 📡 Códigos de estado HTTP

| Código | Significado | Ejemplo |
|--------|------------|--------|
| 200 | OK | GET exitoso |
| 201 | Created | POST exitoso |
| 400 | Bad Request | Datos inválidos |
| 404 | Not Found | ID no existe |
| 422 | Unprocessable Entity | Error de validación |
| 500 | Server Error | Error interno |
