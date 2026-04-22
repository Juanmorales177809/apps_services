# Clase: Autorización y Scopes con JWT

## 📌 Descripción
Esta clase introduce el concepto de **autorización** en aplicaciones web utilizando **JWT (JSON Web Token)**. Se diferencia claramente entre autenticación y autorización, y se implementa control de acceso basado en **scopes (permisos)**.

---

## 🎯 Objetivos de aprendizaje
Al finalizar la clase, el estudiante podrá:

- Diferenciar autenticación vs autorización
- Entender la estructura de un JWT
- Identificar el rol del payload en la gestión de permisos
- Implementar control de acceso usando scopes
- Validar tokens en el backend

---

## 🧠 Conceptos clave

### 🔐 Autenticación
Verifica la identidad del usuario.

### 🛂 Autorización
Define qué acciones puede realizar el usuario.

### 🎟️ JWT (JSON Web Token)
Token que transporta información del usuario y permisos.

### 🎯 Scopes
Permisos específicos dentro del token.

Ejemplo:
```json
{
  "sub": "juan",
  "scopes": ["read", "write"]
}
```

---

## 🧩 Flujo del sistema

1. Usuario hace login
2. Backend valida credenciales
3. Backend genera JWT con scopes
4. Cliente guarda el token
5. Cliente envía el token en cada request
6. Backend valida:
   - Firma
   - Expiración
   - Scopes
7. Acceso permitido o denegado

---

## ⚙️ Implementación en FastAPI

### Dependencias
```bash
pip install fastapi uvicorn python-jose passlib[bcrypt]
```

---

### Ejemplo básico de scopes

```python
from fastapi import FastAPI, Security, HTTPException
from fastapi.security import OAuth2PasswordBearer, SecurityScopes

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login",
    scopes={
        "read": "Leer datos",
        "write": "Escribir datos",
        "admin": "Acceso total"
    }
)


def get_current_user(security_scopes: SecurityScopes, token: str = Security(oauth2_scheme)):
    payload = {"scopes": ["read"]}  # Simulación

    for scope in security_scopes.scopes:
        if scope not in payload["scopes"]:
            raise HTTPException(status_code=403, detail="No autorizado")

    return payload


@app.get("/read")
def read_data(user=Security(get_current_user, scopes=["read"])):
    return {"msg": "Lectura permitida"}
```

---

## 🧪 Actividad práctica

### Objetivo
Implementar control de acceso con scopes.

### Tareas

1. Crear endpoint `/read` → requiere `read`
2. Crear endpoint `/write` → requiere `write`
3. Crear endpoint `/admin` → requiere `admin`
4. Modificar el token para incluir scopes
5. Validar scopes en backend

---

## ⚠️ Buenas prácticas

- Validar siempre el token en backend
- Usar expiración corta
- No almacenar información sensible en el payload
- Asignar permisos mínimos necesarios

---

## ❌ Errores comunes

- No validar firma
- Ignorar expiración
- No validar scopes

---

## 💥 Mensaje clave

> El backend es quien decide el acceso, no el cliente.
>
> Los permisos viajan en el token y controlan lo que el usuario puede hacer.

---

## 🚀 Conclusión

JWT permite implementar autenticación sin estado y autorización basada en permisos de forma escalable y eficiente.

---

## 📚 Recomendaciones

- Revisar documentación de FastAPI Security
- Explorar OAuth2
- Implementar roles + scopes en proyectos reales

---

## 🧑‍💻 Autor
Clase de Aplicaciones y Servicios Web
