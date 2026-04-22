# 🔐 Autenticación con JWT en FastAPI
### Módulo: Seguridad y Proyección  
### Curso: Aplicaciones y Servicios Web

Este laboratorio introduce el concepto de autenticación basada en **JSON Web Tokens (JWT)** utilizando **FastAPI**. A lo largo de la clase se explicarán los fundamentos teóricos, la arquitectura del sistema y la implementación práctica, finalizando con la validación del funcionamiento mediante Swagger.

---

## 📚 Contenido de la Clase

1. Introducción a la seguridad en servicios web  
2. Autenticación vs. Autorización  
3. Problemas de las sesiones tradicionales  
4. ¿Qué es un JSON Web Token (JWT)?  
5. Estructura de un JWT  
6. Librerías y herramientas utilizadas  
7. Arquitectura del proyecto  
8. Implementación de la autenticación  
9. Generación y validación del token  
10. Protección de endpoints  
11. Instalación de dependencias  
12. Pruebas en Swagger  

---

## 🔐 1. Introducción a la Seguridad en Servicios Web

Las APIs modernas requieren mecanismos de seguridad que permitan verificar la identidad de los usuarios y proteger la información. La autenticación basada en tokens es una solución eficiente, escalable y ampliamente utilizada en aplicaciones web y móviles.

---

## 👤 2. Autenticación vs. Autorización

| Concepto | Descripción |
|----------|-------------|
| **Autenticación** | Verifica la identidad del usuario. |
| **Autorización** | Determina qué acciones puede realizar el usuario. |

Ejemplo:
- Autenticación: Iniciar sesión con usuario y contraseña.
- Autorización: Permitir acceso solo a usuarios administradores.

---

## 🔑 3. ¿Qué es JWT?

**JWT (JSON Web Token)** es un estándar definido en el **RFC 7519** que permite transmitir información de forma segura entre dos partes.

### Características
- Compacto y eficiente.
- Autocontenido.
- Firmado digitalmente.
- Stateless (sin estado en el servidor).

### Estructura de un JWT
Un token consta de tres partes separadas por puntos:

```
HEADER.PAYLOAD.SIGNATURE
```

#### Header
Contiene el algoritmo de firma.
```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

#### Payload
Contiene la información del usuario.
```json
{
  "sub": "admin",
  "exp": 1776366295
}
```

#### Signature
Garantiza la integridad del token mediante el `SECRET_KEY`.

---

## 🛠️ 4. Librerías y Herramientas

| Librería | Descripción |
|----------|-------------|
| **FastAPI** | Framework para crear APIs modernas en Python. |
| **PyJWT** | Generación y validación de tokens JWT. |
| **pwdlib** | Hash seguro de contraseñas. |
| **SQLAlchemy** | ORM para la gestión de bases de datos. |
| **python-dotenv** | Gestión de variables de entorno. |
| **Uvicorn** | Servidor ASGI para ejecutar la aplicación. |

---

## 🏗️ 5. Arquitectura del Proyecto

```
project/
│── api/
│   └── auth.py
│
│── crud/
│   └── auth.py
│
│── models/
│   └── usuario.py
│
│── schemas/
│   └── auth.py
│
│── security/
│   └── auth.py
│
│── db.py
│── main.py
│── .env
│── requirements.txt
└── README.md
```

### Descripción de Carpetas

| Carpeta | Función |
|---------|---------|
| **api/** | Define los endpoints. |
| **crud/** | Maneja consultas a la base de datos. |
| **models/** | Define las entidades. |
| **schemas/** | Define la validación de datos. |
| **security/** | Implementa la autenticación JWT. |
| **db.py** | Configura la conexión a la base de datos. |

---

## 🔑 6. Variables de Entorno

Crear un archivo `.env` en la raíz del proyecto:

```env
SECRET_KEY=mi_clave_secreta_super_segura
```

Para generar una clave segura:

```python
import secrets
print(secrets.token_hex(32))
```

---

## ⚙️ 7. Instalación de Dependencias

Instalar las librerías necesarias:

```bash
pip install fastapi uvicorn pyjwt pwdlib python-dotenv sqlalchemy
```

Opcionalmente, guardar las dependencias:

```bash
pip freeze > requirements.txt
```

---

## ▶️ 8. Ejecución del Proyecto

Iniciar el servidor:

```bash
uvicorn main:app --reload
```

Acceder a la aplicación:

- API:
  ```
  http://127.0.0.1:8000
  ```

- Documentación Swagger:
  ```
  http://127.0.0.1:8000/docs
  ```

---

## 🧪 9. Pruebas en Swagger

### Paso 1: Iniciar Sesión
Ejecutar el endpoint:

```
POST /auth/login
```

Ejemplo de solicitud:

```json
{
  "username": "admin",
  "password": "123456"
}
```

Respuesta esperada:

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer"
}
```

---

### Paso 2: Autorizar el Token

1. Hacer clic en **Authorize**.
2. Pegar el token en el campo **Value**:

```
Bearer eyJhbGciOiJIUzI1NiIs...
```

3. Presionar **Authorize** y luego **Close**.

---

### Paso 3: Acceder a un Endpoint Protegido

Ejecutar:

```
GET /auth/me
```

Respuesta esperada:

```json
{
  "username": "admin",
  "correo": "admin@correo.com"
}
```

---

## ❌ Errores Comunes

| Error | Causa | Solución |
|------|-------|----------|
| 401 Unauthorized | Token inválido o expirado | Generar uno nuevo |
| Token inválido | SECRET_KEY incorrecta | Verificar `.env` |
| Not authenticated | No se autorizó en Swagger | Usar botón **Authorize** |
| Module not found | Dependencias no instaladas | Ejecutar `pip install` |

---

## 🔄 Flujo de Autenticación

```
Usuario → Login → Validación de Credenciales
        → Generación de JWT
        → Cliente almacena el Token
        → Solicitud con Authorization: Bearer Token
        → Validación del Token
        → Acceso al Recurso Protegido
```

---

## 📖 Referencias

- RFC 7519 – JSON Web Token: https://datatracker.ietf.org/doc/html/rfc7519  
- Documentación FastAPI: https://fastapi.tiangolo.com  
- PyJWT: https://pyjwt.readthedocs.io  
- OWASP Authentication Guide: https://owasp.org  

---

## 👨‍🏫 Autor

**Curso:** Aplicaciones y Servicios Web  
**Módulo:** Seguridad y Proyección  
**Tema:** Autenticación con JWT usando FastAPI  

---

## ✅ Conclusión

En esta práctica se aprendió a:

- Implementar autenticación con JWT.
- Proteger endpoints en FastAPI.
- Utilizar variables de entorno para mayor seguridad.
- Integrar FastAPI con SQLAlchemy.
- Validar el funcionamiento mediante Swagger.

La autenticación basada en JWT es un estándar moderno, escalable y ampliamente utilizado en el desarrollo de servicios web seguros.
