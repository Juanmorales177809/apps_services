# Guía de Trabajo Práctico Experimental — Laboratorio 3

**Desarrollo de servicios web seguros con JWT, scopes y reglas de autorización utilizando FastAPI y PostgreSQL**

---

| Campo | Valor |
|---|---|
| **Código de guía** | 003 |
| **Laboratorio** | Laboratorio DevOps |
| **Tiempo estimado** | 4 días |
| **Asignatura** | Aplicaciones y Servicios Web |
| **Programa académico** | Tecnología en Desarrollo de Software |
| **Elaborado por** | Juan Carlos Morales Guerra |
| **Versión** | 002 |
| **Fecha** | 27-02-2026 |

---

## 1. Competencias, Contenido Temático e Indicador de Logro

| Competencias | Contenido Temático | Indicador de Logro |
|---|---|---|
| Diseñar y desarrollar servicios web seguros utilizando FastAPI, PostgreSQL, JWT y scopes, aplicando reglas de autorización, validación de datos y control de acceso según roles dentro de una mesa de servicios para laboratorios universitarios. | Autenticación con JWT. Autorización basada en scopes. Roles de usuario y permisos. Protección de endpoints en FastAPI. Persistencia de datos con PostgreSQL y SQLAlchemy. Modelado de usuarios, laboratorios, servicios y tickets. Reglas de negocio para flujo de estados del ticket. Validación de acceso según rol, scope y relación con el ticket. Pruebas de endpoints protegidos en Swagger. Trabajo colaborativo con Git y GitHub. | El estudiante implementa una API segura para la gestión de tickets de servicios en laboratorios, utilizando JWT para autenticación, scopes para autorización y PostgreSQL para persistencia, aplicando reglas de negocio que controlan la creación, asignación, actualización, consulta y finalización de tickets según el rol del usuario. |

---

## 2. Fundamento Teórico

El desarrollo de servicios web modernos requiere mecanismos que permitan identificar a los usuarios y controlar las acciones que pueden realizar dentro del sistema. La **autenticación** permite verificar la identidad de un usuario, mientras que la **autorización** define qué operaciones está permitido ejecutar según sus permisos.

**JSON Web Token (JWT)** es un estándar abierto (RFC 7519) utilizado para transmitir información segura entre cliente y servidor mediante un token firmado. Después de iniciar sesión, el servidor genera un token compuesto por tres partes: encabezado (*header*), carga útil (*payload*) y firma (*signature*), codificadas en Base64URL y separadas por puntos. El cliente envía este token en cada solicitud protegida dentro del encabezado HTTP `Authorization: Bearer <token>`. De esta manera, la API puede reconocer al usuario sin mantener una sesión tradicional en el servidor.

Los **scopes** permiten representar permisos específicos dentro del sistema. A diferencia de un rol general (como `admin` o `tecnico`), un scope describe una acción concreta, por ejemplo `tickets:crear` o `tickets:finalizar`. Esto facilita controlar el acceso a los endpoints de forma más precisa y escalable, ya que un mismo rol puede tener múltiples scopes y un scope puede ser compartido entre roles diferentes.

**FastAPI** implementa autenticación y autorización mediante el sistema de dependencias de Python. La clase `OAuth2PasswordBearer` gestiona la extracción del token del encabezado, mientras que `SecurityScopes` permite declarar qué scopes requiere cada endpoint. Combinado con **SQLAlchemy** como ORM y **PostgreSQL** como motor de base de datos, FastAPI permite construir servicios web con persistencia de datos, validación mediante **Pydantic** y separación clara entre modelos, esquemas y lógica de acceso a datos.

En este taller, estos conceptos se aplican al desarrollo de una **mesa de servicios para laboratorios universitarios**. El sistema controla que un usuario pueda crear un ticket; que el responsable técnico lo reciba y asigne a un auxiliar o técnico especializado; que el técnico asignado atienda la solicitud y actualice el estado; y que finalmente el responsable técnico revise y cierre el caso. Este flujo exige combinar autenticación, autorización y reglas de negocio para garantizar que cada usuario solo pueda realizar las acciones permitidas dentro del proceso.

---

## 3. Objetivos

### Objetivo General

Desarrollar una API segura para la gestión de tickets de servicios en laboratorios universitarios, utilizando FastAPI, PostgreSQL, JWT y scopes para controlar la autenticación, autorización y flujo de atención de las solicitudes.

### Objetivos Específicos

- Diseñar el modelo de datos para usuarios, laboratorios, servicios y tickets.
- Implementar autenticación de usuarios mediante JWT.
- Definir roles y scopes para controlar el acceso a los endpoints.
- Proteger rutas de la API según los permisos requeridos.
- Implementar reglas de negocio para la creación, recepción, asignación, atención y finalización de tickets.
- Validar la visibilidad de los tickets según el rol y la relación del usuario con la solicitud.
- Probar los endpoints protegidos mediante Swagger o herramienta equivalente.

---

## 4. Recursos Requeridos

### Equipos

- Computador personal o estación de trabajo por estudiante.

### Herramientas de Software

- Sistema operativo Linux o Windows.
- Python 3.10 o superior.
- FastAPI.
- PostgreSQL.
- SQLAlchemy.
- Uvicorn.
- Git.
- Cuenta en GitHub.
- Editor de código (recomendado: Visual Studio Code).

### Material Bibliográfico y Recursos Digitales

- Documentación oficial de FastAPI: https://fastapi.tiangolo.com
- Documentación oficial de Pydantic: https://docs.pydantic.dev
- Documentación oficial de Python: https://docs.python.org
- Guías básicas de uso de Git y GitHub.
- Repositorio de clase: https://github.com/Juanmorales177809/apps_services.git

---

## 5. Aspectos de Seguridad

La práctica descrita en esta guía corresponde a una actividad de desarrollo de software, por lo cual no se identifican riesgos físicos o químicos asociados al uso de laboratorios experimentales.

Sin embargo, se recomienda tener en cuenta las siguientes consideraciones:

- Mantener una postura adecuada durante el uso prolongado del computador para evitar fatiga o lesiones musculares.
- Evitar la manipulación inadecuada de cables o conexiones eléctricas de los equipos.
- Realizar copias de seguridad periódicas del código desarrollado para evitar pérdida de información.
- **Nunca incluir credenciales sensibles** (contraseñas, cadenas de conexión, claves JWT) directamente en el código fuente. Siempre usar variables de entorno mediante un archivo `.env`.

---

## 6. Procedimiento o Metodología para el Desarrollo

La práctica se desarrollará en equipos de trabajo conformados por dos a tres estudiantes. A continuación se presenta la distribución orientativa del tiempo:

| Actividad | Descripción | Tiempo orientativo |
|---|---|---|
| 1 | Configuración inicial del proyecto | Día 1 — mañana |
| 2 | Comprensión del problema y modelo de datos | Día 1 — tarde |
| 3 | Configuración de la base de datos y modelos | Día 2 |
| 4 | Autenticación con JWT y gestión de usuarios | Día 3 — mañana |
| 5 | Autorización con scopes y reglas de acceso | Día 3 — tarde / Día 4 — mañana |
| 6 | Trabajo colaborativo y entrega | Día 4 — tarde |

---

### Actividad 1: Configuración Inicial del Proyecto

**Tiempo orientativo:** Día 1 — mañana

**Pasos:**

1. Crear repositorio en GitHub con el nombre acordado por el equipo.
2. Clonar el repositorio en el computador local.
3. Crear el entorno virtual de Python:

```bash
python -m venv venv
```

4. Activar el entorno virtual:

```bash
# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

5. Instalar las dependencias del proyecto:

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary \
    python-jose[cryptography] passlib[bcrypt] \
    python-multipart python-dotenv
```

> **Nota:** Las dependencias `python-jose[cryptography]`, `passlib[bcrypt]`, `python-multipart` y `python-dotenv` son obligatorias para implementar JWT y autenticación segura. Sin ellas no es posible completar las Actividades 4 y 5.

6. Crear el archivo `requirements.txt`:

```bash
pip freeze > requirements.txt
```

7. Crear el archivo `.gitignore` con el siguiente contenido mínimo:

```
venv/
__pycache__/
*.pyc
.env
```

8. Crear el archivo `.env` para almacenar las variables de entorno sensibles:

```
DATABASE_URL=postgresql://usuario:contraseña@host:5432/nombre_db
SECRET_KEY=una_clave_secreta_larga_y_aleatoria
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

> **Importante:** El archivo `.env` **nunca debe subirse al repositorio**. Verificar que esté incluido en el `.gitignore`.

9. Crear la estructura de carpetas del proyecto:

```
nombre_proyecto/
├── app/
│   ├── __init__.py
│   ├── main.py          ← Punto de entrada de la aplicación
│   ├── db.py            ← Configuración de la conexión a PostgreSQL
│   ├── models.py        ← Modelos SQLAlchemy (tablas)
│   ├── schemas.py       ← Esquemas Pydantic (validación)
│   ├── crud.py          ← Lógica de acceso a la base de datos
│   ├── auth.py          ← Lógica de JWT y autenticación
│   └── routers/
│       ├── __init__.py
│       ├── usuarios.py
│       ├── laboratorios.py
│       ├── servicios.py
│       └── tickets.py
├── .env
├── .gitignore
└── requirements.txt
```

---

### Actividad 2: Comprensión del Problema y del Modelo de Datos

**Tiempo orientativo:** Día 1 — tarde

#### A. Planteamiento del Problema

La universidad requiere una API para gestionar solicitudes de servicios en laboratorios. Una persona podrá crear un ticket seleccionando el laboratorio y el tipo de servicio requerido. El responsable técnico del laboratorio deberá recibir la solicitud, asignarla a un auxiliar o técnico especializado, revisar el avance y finalizar el ticket cuando el servicio haya sido atendido.

El sistema debe controlar el acceso mediante autenticación con JWT y autorización basada en scopes, de modo que cada usuario solo pueda ejecutar las acciones permitidas según su rol.

#### B. Roles del Sistema

| Rol | Descripción |
|---|---|
| `solicitante` | Crea tickets y consulta sus propias solicitudes. |
| `responsable_tecnico` | Recibe, asigna y finaliza tickets del laboratorio que gestiona. |
| `auxiliar` | Atiende tickets asignados a él; actualiza el estado a `en_proceso` y `en_revision`. |
| `tecnico_especializado` | Igual que auxiliar; atiende tickets de mayor complejidad técnica. |
| `admin` | Acceso total al sistema. Puede ver y gestionar cualquier recurso. |

#### C. Scopes del Sistema

Los scopes representan los permisos concretos que se incluyen en el token JWT. Cada rol recibe un conjunto predefinido de scopes al iniciar sesión.

| Scope | Descripción | Roles que lo poseen |
|---|---|---|
| `tickets:crear` | Crear nuevos tickets | solicitante, admin |
| `tickets:ver_propios` | Ver los tickets propios (como solicitante o asignado) | solicitante, auxiliar, tecnico_especializado, admin |
| `tickets:recibir` | Cambiar estado de `solicitado` a `recibido` | responsable_tecnico, admin |
| `tickets:asignar` | Asignar ticket a un auxiliar o técnico | responsable_tecnico, admin |
| `tickets:atender` | Cambiar estado a `en_proceso` o `en_revision` | auxiliar, tecnico_especializado, admin |
| `tickets:finalizar` | Cambiar estado a `terminado` | responsable_tecnico, admin |
| `tickets:ver_todos` | Ver todos los tickets del sistema | admin |
| `usuarios:gestionar` | Crear, listar y consultar usuarios | admin |

> **Importante:** Al generar el token JWT, el servidor debe incluir en el campo `scopes` del payload la lista de scopes correspondientes al rol del usuario autenticado.

#### D. Flujo de Estados del Ticket

El estado del ticket sigue un flujo estrictamente controlado. Solo se permiten las transiciones indicadas en la tabla:

| Estado actual | Estado siguiente | Quién puede hacer la transición | Scope requerido |
|---|---|---|---|
| `solicitado` | `recibido` | responsable_tecnico, admin | `tickets:recibir` |
| `recibido` | `asignado` | responsable_tecnico, admin | `tickets:asignar` |
| `asignado` | `en_proceso` | auxiliar o tecnico_especializado **asignado al ticket**, admin | `tickets:atender` |
| `en_proceso` | `en_revision` | auxiliar o tecnico_especializado **asignado al ticket**, admin | `tickets:atender` |
| `en_revision` | `terminado` | responsable_tecnico, admin | `tickets:finalizar` |

Cualquier intento de transición fuera de esta tabla debe ser rechazado con error `HTTP 422` o `HTTP 403` según corresponda.

#### E. Modelo de Datos

El sistema se desarrollará a partir de cuatro tablas principales.

##### Tabla `usuarios`

Almacena la información de las personas que interactúan con el sistema.

| Campo | Tipo | Descripción |
|---|---|---|
| `id_usuario` | Integer (PK) | Identificador único |
| `nombre` | String | Nombre completo |
| `correo` | String (unique) | Correo electrónico — usado para iniciar sesión |
| `password_hash` | String | Contraseña almacenada como hash bcrypt |
| `rol` | String | Uno de: solicitante, responsable_tecnico, auxiliar, tecnico_especializado, admin |
| `activo` | Boolean | Indica si el usuario puede iniciar sesión |

##### Tabla `laboratorios`

| Campo | Tipo | Descripción |
|---|---|---|
| `id_laboratorio` | Integer (PK) | Identificador único |
| `nombre` | String | Nombre del laboratorio |
| `ubicacion` | String | Ubicación física |
| `activo` | Boolean | Indica si está operativo |

##### Tabla `servicios`

| Campo | Tipo | Descripción |
|---|---|---|
| `id_servicio` | Integer (PK) | Identificador único |
| `nombre` | String | Nombre del servicio |
| `descripcion` | String | Descripción del tipo de soporte |
| `activo` | Boolean | Indica si está disponible |

##### Tabla `tickets`

| Campo | Tipo | Descripción |
|---|---|---|
| `id_ticket` | Integer (PK) | Identificador único |
| `id_solicitante` | FK → usuarios | Quien crea el ticket |
| `id_laboratorio` | FK → laboratorios | Laboratorio donde se requiere el servicio |
| `id_servicio` | FK → servicios | Tipo de servicio solicitado |
| `id_responsable` | FK → usuarios (nullable) | Responsable técnico que gestiona el ticket |
| `id_asignado` | FK → usuarios (nullable) | Auxiliar o técnico asignado para ejecutar |
| `titulo` | String | Título breve de la solicitud |
| `descripcion` | String | Descripción detallada del problema |
| `estado` | String | Estado actual (ver flujo de estados) |
| `prioridad` | String | baja / media / alta |
| `observacion_responsable` | String (nullable) | Comentario del responsable técnico |
| `observacion_tecnico` | String (nullable) | Comentario del técnico asignado |
| `fecha_creacion` | DateTime | Timestamp de creación |
| `fecha_actualizacion` | DateTime | Timestamp de última modificación |
| `fecha_finalizacion` | DateTime (nullable) | Timestamp de cierre |

**Relaciones principales:**

- `usuarios` 1:N `tickets` (como solicitante)
- `usuarios` 1:N `tickets` (como responsable)
- `usuarios` 1:N `tickets` (como asignado)
- `laboratorios` 1:N `tickets`
- `servicios` 1:N `tickets`

---

### Actividad 3: Configuración de la Base de Datos y Modelos

**Tiempo orientativo:** Día 2

**Propósito:** Configurar la conexión con PostgreSQL y desarrollar la estructura base de la API mediante modelos SQLAlchemy, esquemas Pydantic y endpoints iniciales.

**Descripción:** El equipo deberá crear las tablas del sistema dentro del schema de PostgreSQL asignado por el docente, configurar la conexión desde FastAPI y desarrollar los componentes iniciales para gestionar usuarios, laboratorios, servicios y tickets.

> **Nota:** No deben crearse tablas en el schema `public` ni en otro que no haya sido asignado.

**Acciones a realizar:**

1. Configurar la conexión a PostgreSQL en el archivo `app/db.py` usando la variable `DATABASE_URL` definida en el `.env`.
2. Crear los modelos SQLAlchemy para las cuatro tablas en `app/models.py`.
3. Definir claves primarias, claves foráneas y relaciones entre las tablas.
4. Crear los esquemas Pydantic en `app/schemas.py` para validar datos de entrada y salida.
5. Implementar la lógica CRUD en `app/crud.py`.
6. Implementar endpoints base en los archivos de `app/routers/`.
7. Registrar los routers en `app/main.py`.
8. Verificar el funcionamiento desde Swagger (`http://localhost:8000/docs`).

**Referencia de implementación — `app/db.py`:**

```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

**Endpoints mínimos de esta actividad:**

```
POST   /usuarios/
GET    /usuarios/
GET    /usuarios/{id_usuario}

POST   /laboratorios/
GET    /laboratorios/
GET    /laboratorios/{id_laboratorio}

POST   /servicios/
GET    /servicios/
GET    /servicios/{id_servicio}

POST   /tickets/
GET    /tickets/
GET    /tickets/{id_ticket}
PATCH  /tickets/{id_ticket}/estado
```

> En esta actividad los endpoints **no requieren autenticación todavía**. La protección se agrega en la Actividad 4.

---

### Actividad 4: Autenticación con JWT y Gestión de Usuarios

**Tiempo orientativo:** Día 3 — mañana

**Propósito:** Implementar el inicio de sesión de usuarios y la generación de tokens JWT para proteger el acceso a la API.

**Descripción:** Los usuarios registrados deberán iniciar sesión con su correo y contraseña. Si las credenciales son válidas, la API genera un token JWT que el cliente envía en las solicitudes protegidas.

**Acciones a realizar:**

1. Implementar el hashing seguro de contraseñas con `passlib` en `app/auth.py`.
2. Implementar el endpoint de inicio de sesión `POST /auth/token`.
3. Validar las credenciales del usuario contra la base de datos.
4. Generar un token JWT que incluya como mínimo en el payload:
   - `sub`: correo del usuario
   - `id_usuario`: identificador
   - `rol`: rol del usuario
   - `scopes`: lista de scopes correspondientes al rol (ver tabla de scopes en Actividad 2)
   - `exp`: tiempo de expiración
5. Crear una dependencia `get_current_user` que valide el token en cada solicitud protegida.
6. Proteger al menos un endpoint usando `Depends(get_current_user)`.

**Referencia de implementación — `app/auth.py`:**

```python
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.db import get_db
from app import models
import os

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

SCOPES_POR_ROL = {
    "solicitante":         ["tickets:crear", "tickets:ver_propios"],
    "responsable_tecnico": ["tickets:recibir", "tickets:asignar", "tickets:finalizar", "tickets:ver_propios"],
    "auxiliar":            ["tickets:atender", "tickets:ver_propios"],
    "tecnico_especializado": ["tickets:atender", "tickets:ver_propios"],
    "admin":               ["tickets:crear", "tickets:ver_propios", "tickets:recibir",
                            "tickets:asignar", "tickets:atender", "tickets:finalizar",
                            "tickets:ver_todos", "usuarios:gestionar"],
}

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudo validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        correo: str = payload.get("sub")
        if correo is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    usuario = db.query(models.Usuario).filter(models.Usuario.correo == correo).first()
    if usuario is None or not usuario.activo:
        raise credentials_exception
    return usuario
```

**Referencia de implementación — endpoint de login:**

```python
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.db import get_db
from app import models, auth

router = APIRouter(prefix="/auth", tags=["Autenticación"])

@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.correo == form_data.username).first()
    if not usuario or not auth.verify_password(form_data.password, usuario.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales incorrectas")
    scopes = auth.SCOPES_POR_ROL.get(usuario.rol, [])
    token = auth.create_access_token({
        "sub": usuario.correo,
        "id_usuario": usuario.id_usuario,
        "rol": usuario.rol,
        "scopes": scopes,
    })
    return {"access_token": token, "token_type": "bearer"}
```

**Probar desde Swagger el flujo completo:**

1. `POST /usuarios/` — crear un usuario con contraseña en texto plano (el sistema debe almacenarla como hash).
2. `POST /auth/token` — iniciar sesión con correo y contraseña.
3. Copiar el `access_token` de la respuesta.
4. Hacer clic en el botón **Authorize** en Swagger e ingresar `Bearer <token>`.
5. Consultar un endpoint protegido y verificar que responde con los datos del usuario autenticado.

**Producto esperado:** El sistema permite autenticar usuarios mediante correo y contraseña, genera un token JWT válido con los scopes del rol, y protege endpoints que solo puedan ser accedidos por usuarios autenticados.

---

### Actividad 5: Autorización con Scopes y Reglas de Acceso

**Tiempo orientativo:** Día 3 — tarde / Día 4 — mañana

**Propósito:** Proteger los endpoints según los scopes requeridos y aplicar reglas de negocio adicionales basadas en la relación del usuario con el ticket.

**Descripción:** No basta con que el usuario esté autenticado. Cada endpoint debe validar que el token incluya el scope requerido **y** que se cumpla la regla de negocio correspondiente (por ejemplo, que solo el técnico asignado pueda actualizar su propio ticket).

#### A. Implementar la dependencia con verificación de scopes

```python
from fastapi.security import SecurityScopes
from fastapi import Security

def get_current_user_with_scope(
    security_scopes: SecurityScopes,
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):
    if security_scopes.scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
    else:
        authenticate_value = "Bearer"

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudo validar las credenciales",
        headers={"WWW-Authenticate": authenticate_value},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        correo: str = payload.get("sub")
        token_scopes: list = payload.get("scopes", [])
        if correo is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    for scope in security_scopes.scopes:
        if scope not in token_scopes:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Permisos insuficientes. Se requiere el scope: {scope}",
                headers={"WWW-Authenticate": authenticate_value},
            )

    usuario = db.query(models.Usuario).filter(models.Usuario.correo == correo).first()
    if usuario is None or not usuario.activo:
        raise credentials_exception
    return usuario
```

#### B. Proteger endpoints con scopes específicos

```python
from fastapi import Security
from app.auth import get_current_user_with_scope

@router.patch("/{id_ticket}/estado")
def actualizar_estado(
    id_ticket: int,
    nuevo_estado: str,
    db: Session = Depends(get_db),
    usuario_actual = Security(get_current_user_with_scope, scopes=["tickets:atender"]),
):
    ticket = db.query(models.Ticket).filter(models.Ticket.id_ticket == id_ticket).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket no encontrado")

    # Regla de negocio: solo el técnico asignado puede cambiar estado a en_proceso o en_revision
    if nuevo_estado in ["en_proceso", "en_revision"]:
        if ticket.id_asignado != usuario_actual.id_usuario:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Solo el técnico asignado puede actualizar este ticket"
            )

    # Validar transición permitida
    transiciones_validas = {
        "asignado": "en_proceso",
        "en_proceso": "en_revision",
    }
    if transiciones_validas.get(ticket.estado) != nuevo_estado:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Transición de estado no permitida: {ticket.estado} → {nuevo_estado}"
        )

    ticket.estado = nuevo_estado
    db.commit()
    db.refresh(ticket)
    return ticket
```

> **Criterio clave:** No basta con que el endpoint funcione. Deben demostrarse dos cosas:
> 1. Que el usuario **sin scope** recibe error `403`.
> 2. Que el usuario **con scope** también debe cumplir la regla de negocio. Ejemplo: un responsable puede finalizar tickets, pero no puede pasar directamente de `solicitado` a `terminado`.

#### C. Evidencias de Funcionamiento Requeridas

El equipo debe realizar las siguientes pruebas con usuarios de diferentes roles y registrar los resultados en el README del repositorio:

| # | Usuario | Acción | Resultado esperado |
|---|---|---|---|
| 1 | solicitante | Crear ticket | Permitido (200) |
| 2 | solicitante | Asignar ticket | Denegado (403) |
| 3 | responsable_tecnico | Recibir ticket (`solicitado` → `recibido`) | Permitido |
| 4 | responsable_tecnico | Asignar ticket (`recibido` → `asignado`) | Permitido |
| 5 | auxiliar | Cambiar ticket a `en_proceso` | Permitido **solo si está asignado a él** |
| 6 | auxiliar | Finalizar ticket como `terminado` | Denegado (403) |
| 7 | tecnico_especializado | Cambiar ticket a `en_revision` | Permitido **solo si está asignado a él** |
| 8 | responsable_tecnico | Finalizar ticket (`en_revision` → `terminado`) | Permitido |
| 9 | solicitante | Ver tickets de otros usuarios | Denegado (403) |
| 10 | admin | Ver todos los tickets | Permitido |

---

### Actividad 6: Trabajo Colaborativo

**Tiempo orientativo:** Día 4 — tarde

El equipo deberá evidenciar el trabajo colaborativo mediante el uso de Git y GitHub.

**Requisitos mínimos de colaboración:**

- Cada integrante debe tener al menos **5 commits** con mensajes descriptivos en inglés o español (ejemplo: `feat: agregar endpoint de login`, `fix: corregir validación de estado en tickets`).
- Se recomienda usar ramas por funcionalidad y merge a `main` mediante Pull Requests.
- El `README.md` del repositorio debe incluir la descripción de aportes de cada integrante.

---

## 7. Resultado Esperado del Taller

Al finalizar el taller, cada equipo deberá entregar una API funcional desarrollada con FastAPI y PostgreSQL para gestionar tickets de servicios en laboratorios universitarios.

La API debe:

- Implementar autenticación mediante JWT con hashing bcrypt de contraseñas.
- Generar tokens con los scopes del rol del usuario autenticado.
- Proteger endpoints según los scopes definidos en la tabla de la Actividad 2.
- Controlar el flujo de estados del ticket según la tabla de transiciones de la Actividad 2.
- Permitir crear usuarios, laboratorios, servicios y tickets.
- Asignar tickets a auxiliares o técnicos especializados.
- Finalizar tickets únicamente por parte del responsable técnico o administrador.
- Rechazar con `HTTP 403` cualquier acción para la que el usuario no tenga scope.
- Rechazar con `HTTP 422` o `HTTP 403` transiciones de estado no permitidas.

La entrega debe incluir el código fuente en el repositorio, la base de datos configurada en el schema asignado, los modelos SQLAlchemy, los esquemas Pydantic, los endpoints funcionales y las evidencias de prueba en Swagger o herramienta equivalente.

---

## 8. Parámetros para Elaboración del Informe

El informe del taller deberá presentarse en formato **README.md** dentro del repositorio del proyecto en GitHub. No se aceptarán informes en formatos externos (PDF, Word, etc.).

### Contenido del README.md

#### 1. Información General

- Nombre del proyecto
- Integrantes del equipo
- Asignatura
- Fecha

#### 2. Descripción del Sistema

- Descripción general del sistema desarrollado.
- Entidades implementadas: Usuarios, Laboratorios, Servicios y Tickets.
- Descripción de la arquitectura utilizada (`models`, `schemas`, `crud`, `auth`, `routers`, `db`).

#### 3. Configuración del Entorno

- Creación del entorno virtual.
- Activación del entorno.
- Instalación de dependencias.
- Uso del archivo `requirements.txt`.
- Configuración del archivo `.env` (sin incluir valores reales).

#### 4. Configuración de la Base de Datos

- Descripción de la conexión a PostgreSQL.
- Uso del archivo `db.py`.
- Schema asignado (sin incluir credenciales sensibles).

#### 5. Endpoints Implementados

Listado completo de endpoints con método HTTP, ruta, descripción, scope requerido y rol(es) autorizados.

#### 6. Evidencias de Funcionamiento

**Autenticación con JWT:**
- Login exitoso con token generado.
- Uso del botón Authorize en Swagger con Bearer Token.
- Consulta de endpoint protegido con token válido.
- Intento de acceso sin token recibiendo `401`.

**Autorización con scopes:**
- Usuario con scope ejecutando acción permitida (captura + respuesta HTTP).
- Usuario sin scope recibiendo error `403` (captura + respuesta HTTP).
- Ejemplo de endpoint protegido por scope con el código correspondiente.

**Reglas de negocio del ticket:**
- Ticket creado en estado `solicitado`.
- Responsable técnico recibe el ticket (`solicitado` → `recibido`).
- Responsable técnico asigna el ticket a un auxiliar.
- Auxiliar o técnico cambia estado a `en_proceso`.
- Auxiliar o técnico cambia estado a `en_revision`.
- Responsable técnico finaliza el ticket (`en_revision` → `terminado`).

**Evidencia de restricciones:**
- Solicitante intentando asignar un ticket → error.
- Auxiliar intentando finalizar un ticket → error.
- Usuario intentando modificar un ticket no asignado a él → error.
- Responsable intentando finalizar un ticket que no está en `en_revision` → error.

#### 7. Control de Versiones

- Enlace al repositorio en GitHub.
- Evidencia de commits realizados por cada integrante (captura o listado).
- Descripción breve del aporte de cada miembro.

#### 8. Conclusiones

- Principales aprendizajes.
- Dificultades encontradas.
- Soluciones aplicadas.

> **Nota:** El README debe permitir que cualquier persona pueda clonar el repositorio y ejecutar el proyecto sin necesidad de información adicional fuera del archivo.

### Requisitos del Repositorio

El repositorio debe:

- Contener el código fuente completo organizado según la arquitectura propuesta.
- Incluir el archivo `README.md` correctamente estructurado.
- Incluir el archivo `requirements.txt`.
- Incluir el archivo `.gitignore` (con `.env` excluido).
- **No incluir** el archivo `.env` con credenciales reales.

---

## 9. Disposición de Residuos

La actividad descrita en esta guía no genera residuos físicos o químicos. En consecuencia, no se requiere un procedimiento específico de disposición de residuos para esta práctica.

---

## 10. Bibliografía

- FastAPI. (2024). *FastAPI Documentation*. https://fastapi.tiangolo.com
- FastAPI. (2024). *OAuth2 with scopes*. https://fastapi.tiangolo.com/advanced/security/oauth2-scopes/
- Pydantic. (2024). *Pydantic Documentation*. https://docs.pydantic.dev
- Python Software Foundation. (2024). *Python Documentation*. https://docs.python.org
- python-jose. (2024). *Python JOSE Documentation*. https://python-jose.readthedocs.io
- passlib. (2024). *Passlib Documentation*. https://passlib.readthedocs.io
- Chacon, S., & Straub, B. (2014). *Pro Git*. Apress.
- Fielding, R. (2000). *Architectural Styles and the Design of Network-based Software Architectures*. University of California, Irvine.

