# Deploy

Este documento acompaña la práctica final de la clase de Aplicaciones y Servicios Web. El objetivo es desplegar una API desarrollada con FastAPI, una base de datos PostgreSQL y pgAdmin usando Docker Compose en un servidor Linux.

La práctica sigue este flujo:

1. Repasar comandos básicos de Linux.
2. Acceder a un servidor por SSH.
3. Instalar Docker y Docker Compose.
4. Crear la estructura del proyecto.
5. Crear el Dockerfile del backend FastAPI.
6. Crear el archivo docker-compose.yml.
7. Levantar los servicios.
8. Verificar contenedores, puertos y logs.
9. Probar FastAPI, PostgreSQL y pgAdmin.
10. Preparar el repositorio para GitHub.

---

## 1. Comandos básicos de Linux antes de comenzar

Antes de instalar Docker o crear archivos, es importante manejar algunos comandos básicos de terminal.

### Ver la ubicación actual

```bash
pwd
```

Muestra la carpeta donde estamos ubicados.

### Listar archivos y carpetas

```bash
ls
```

Lista el contenido de la carpeta actual.

```bash
ls -la
```

Muestra archivos visibles, ocultos, permisos, propietarios y fechas.

### Cambiar de carpeta

```bash
cd nombre_carpeta
```

Ejemplo:

```bash
cd proyectos
```

Volver a la carpeta anterior:

```bash
cd ..
```

Ir al directorio personal del usuario:

```bash
cd ~
```

### Crear una carpeta

```bash
mkdir nombre_carpeta
```

Ejemplo:

```bash
mkdir clase-despliegue
```

### Crear varias carpetas

```bash
mkdir -p backend/app
```

El parámetro `-p` permite crear carpetas anidadas.

### Crear un archivo con nano

```bash
nano nombre_archivo
```

Ejemplo:

```bash
nano docker-compose.yml
```

Para guardar en nano:

```text
CTRL + O
Enter
CTRL + X
```

### Ver el contenido de un archivo

```bash
cat nombre_archivo
```

Ejemplo:

```bash
cat docker-compose.yml
```

### Copiar archivos

```bash
cp archivo_origen archivo_destino
```

Ejemplo:

```bash
cp .env.example .env
```

### Eliminar archivos

```bash
rm nombre_archivo
```

### Eliminar carpetas

```bash
rm -r nombre_carpeta
```

### Limpiar la terminal

```bash
clear
```

### Ejecutar comandos con permisos de administrador

```bash
sudo comando
```

Ejemplo:

```bash
sudo apt update
```

---

## 2. Acceso al servidor por SSH

Para trabajar en un servidor Linux remoto se usa SSH.

La estructura general del comando es:

```bash
ssh usuario@ip_del_servidor
```

Ejemplo:

```bash
ssh usuario@192.168.1.50
```

Si el servidor usa un puerto diferente al 22:

```bash
ssh usuario@ip_del_servidor -p puerto
```

Ejemplo:

```bash
ssh usuario@192.168.1.50 -p 2222
```

Después de ingresar al servidor, se recomienda verificar:

```bash
pwd
```

```bash
ls -la
```

También es buena práctica actualizar la lista de paquetes:

```bash
sudo apt update
```

---

## 3. Preparar una carpeta de trabajo

Crear una carpeta para la práctica:

```bash
mkdir -p ~/clase-despliegue
```

Entrar a la carpeta:

```bash
cd ~/clase-despliegue
```

Verificar ubicación:

```bash
pwd
```

---

## 4. Instalación de Docker en Ubuntu Server

Primero se actualiza el sistema de paquetes:

```bash
sudo apt update
```

Instalar paquetes necesarios para usar repositorios por HTTPS:

```bash
sudo apt install -y ca-certificates curl gnupg
```

Crear la carpeta para las llaves de paquetes:

```bash
sudo install -m 0755 -d /etc/apt/keyrings
```

Descargar la llave oficial de Docker:

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

Asignar permisos de lectura:

```bash
sudo chmod a+r /etc/apt/keyrings/docker.gpg
```

Agregar el repositorio de Docker:

```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

Actualizar nuevamente los paquetes:

```bash
sudo apt update
```

Instalar Docker Engine, CLI, containerd y Docker Compose como plugin:

```bash
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Verificar Docker:

```bash
docker --version
```

Verificar Docker Compose:

```bash
docker compose version
```

Probar Docker con un contenedor de prueba:

```bash
sudo docker run hello-world
```

---

## 5. Usar Docker sin escribir sudo

Agregar el usuario actual al grupo `docker`:

```bash
sudo usermod -aG docker $USER
```

Aplicar el cambio de grupo en la sesión actual:

```bash
newgrp docker
```

Probar nuevamente:

```bash
docker run hello-world
```

---

## 6. Crear la estructura del proyecto

Desde la carpeta de trabajo:

```bash
cd ~/clase-despliegue
```

Crear la estructura:

```bash
mkdir -p backend/app
```

Verificar:

```bash
ls -la
```

La estructura esperada será:

```text
clase-despliegue/
├── backend/
│   ├── app/
│   │   └── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── docker-compose.yml
├── .env.example
├── .gitignore
└── README.md
```

---

## 7. Crear la aplicación FastAPI

Crear el archivo principal:

```bash
nano backend/app/main.py
```

Pegar el siguiente contenido:

```python
from fastapi import FastAPI
import os

app = FastAPI(
    title="API desplegada con Docker Compose",
    version="1.0.0"
)

@app.get("/")
def inicio():
    return {
        "mensaje": "API funcionando correctamente",
        "servicio": "FastAPI",
        "estado": "activo"
    }

@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }

@app.get("/config")
def mostrar_configuracion():
    return {
        "database_url": os.getenv("DATABASE_URL", "No configurada")
    }
```

Guardar el archivo con:

```text
CTRL + O
Enter
CTRL + X
```

---

## 8. Crear el archivo requirements.txt

Crear el archivo:

```bash
nano backend/requirements.txt
```

Agregar:

```text
fastapi
uvicorn[standard]
sqlalchemy
psycopg2-binary
python-dotenv
```

Guardar y salir.

---

## 9. Crear el Dockerfile para FastAPI

Crear el archivo:

```bash
nano backend/Dockerfile
```

Agregar el siguiente contenido:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Guardar y salir.

### Explicación del Dockerfile

`FROM python:3.12-slim` define la imagen base.

`WORKDIR /app` define la carpeta de trabajo dentro del contenedor.

`COPY requirements.txt .` copia el archivo de dependencias.

`RUN pip install --no-cache-dir -r requirements.txt` instala las dependencias.

`COPY . .` copia el código del backend dentro del contenedor.

`CMD [...]` ejecuta la API usando Uvicorn.

El parámetro `--host 0.0.0.0` permite que la API sea accesible desde fuera del contenedor.

---

## 10. Crear el archivo docker-compose.yml

Crear el archivo en la raíz del proyecto:

```bash
nano docker-compose.yml
```

Agregar el siguiente contenido:

```yaml
services:
  db:
    image: postgres:16
    container_name: clase_postgres
    restart: always
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: appdb
    ports:
      - "5433:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - app_network

  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: clase_fastapi
    restart: always
    depends_on:
      - db
    environment:
      DATABASE_URL: postgresql://postgres:postgres@db:5432/appdb
    ports:
      - "8000:8000"
    networks:
      - app_network

  pgadmin:
    image: dpage/pgadmin4:latest
    container_name: clase_pgadmin
    restart: always
    depends_on:
      - db
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@admin.com
      PGADMIN_DEFAULT_PASSWORD: admin
    ports:
      - "5050:80"
    volumes:
      - pgadmin_data:/var/lib/pgadmin
    networks:
      - app_network

volumes:
  postgres_data:
  pgadmin_data:

networks:
  app_network:
    driver: bridge
```

Guardar y salir.

---

## 11. Explicación del docker-compose.yml

### Servicio db

`image: postgres:16` crea un contenedor usando PostgreSQL 16.

`container_name: clase_postgres` define un nombre claro para el contenedor.

`POSTGRES_USER`, `POSTGRES_PASSWORD` y `POSTGRES_DB` definen el usuario, la contraseña y la base de datos inicial.

```yaml
ports:
  - "5433:5432"
```

El puerto interno de PostgreSQL es `5432`. En la máquina se publica como `5433`.

```yaml
volumes:
  - postgres_data:/var/lib/postgresql/data
```

Guarda los datos de PostgreSQL en un volumen persistente.

### Servicio backend

```yaml
build:
  context: ./backend
  dockerfile: Dockerfile
```

Construye la imagen del backend usando el Dockerfile ubicado en la carpeta `backend`.

```yaml
depends_on:
  - db
```

Indica que el backend depende del servicio `db`.

```yaml
DATABASE_URL: postgresql://postgres:postgres@db:5432/appdb
```

Define la URL de conexión a la base de datos.

El host es `db`, no `localhost`.

Dentro de Docker Compose, los servicios se comunican usando el nombre del servicio. Por eso el backend se conecta a PostgreSQL usando:

```text
db:5432
```

### Servicio pgAdmin

`image: dpage/pgadmin4:latest` crea un contenedor con pgAdmin.

```yaml
ports:
  - "5050:80"
```

Permite acceder a pgAdmin desde el navegador usando el puerto `5050`.

```yaml
volumes:
  - pgadmin_data:/var/lib/pgadmin
```

Permite conservar la configuración de pgAdmin.

---

## 12. Crear archivo .env.example

Aunque en esta práctica las variables están dentro del `docker-compose.yml`, es conveniente mostrar cómo se documentan.

Crear archivo:

```bash
nano .env.example
```

Agregar:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=appdb
DATABASE_URL=postgresql://postgres:postgres@db:5432/appdb
PGADMIN_DEFAULT_EMAIL=admin@admin.com
PGADMIN_DEFAULT_PASSWORD=admin
```

Guardar y salir.

---

## 13. Crear archivo .gitignore

Crear archivo:

```bash
nano .gitignore
```

Agregar:

```gitignore
.env
__pycache__/
*.pyc
venv/
.env.local
.DS_Store
```

Guardar y salir.

---

## 14. Levantar los servicios

Desde la raíz del proyecto:

```bash
cd ~/clase-despliegue
```

Levantar todos los servicios:

```bash
docker compose up -d --build
```

Explicación:

`docker compose` ejecuta Docker Compose.

`up` levanta los servicios definidos.

`-d` ejecuta los contenedores en segundo plano.

`--build` reconstruye la imagen del backend si hubo cambios en el Dockerfile o en el código.

---

## 15. Verificar contenedores

Ver contenedores activos:

```bash
docker ps
```

Se deberían ver tres contenedores:

```text
clase_postgres
clase_fastapi
clase_pgadmin
```

Ver todos los contenedores, incluso detenidos:

```bash
docker ps -a
```

---

## 16. Verificar logs

Ver logs generales del proyecto:

```bash
docker compose logs
```

Ver logs del backend:

```bash
docker compose logs backend
```

Ver logs de PostgreSQL:

```bash
docker compose logs db
```

Ver logs de pgAdmin:

```bash
docker compose logs pgadmin
```

Seguir los logs en tiempo real:

```bash
docker compose logs -f
```

O solo los logs del backend en tiempo real:

```bash
docker compose logs -f backend
```

---

## 17. Probar la API FastAPI

En el navegador:

```text
http://IP_DEL_SERVIDOR:8000
```

Si se está trabajando en la misma máquina:

```text
http://localhost:8000
```

Documentación Swagger:

```text
http://IP_DEL_SERVIDOR:8000/docs
```

Endpoint de verificación:

```text
http://IP_DEL_SERVIDOR:8000/health
```

Endpoint de configuración:

```text
http://IP_DEL_SERVIDOR:8000/config
```

---

## 18. Probar pgAdmin

Abrir en el navegador:

```text
http://IP_DEL_SERVIDOR:5050
```

Si se está trabajando en la misma máquina:

```text
http://localhost:5050
```

Ingresar con los datos definidos en el `docker-compose.yml`:

```text
Email: admin@admin.com
Password: admin
```

---

## 19. Registrar PostgreSQL en pgAdmin

Dentro de pgAdmin, crear un nuevo servidor.

### General

```text
Name: clase_postgres
```

### Connection

```text
Host name/address: db
Port: 5432
Maintenance database: appdb
Username: postgres
Password: postgres
```

El host debe ser:

```text
db
```

No se usa `localhost` porque pgAdmin está dentro de otro contenedor. En la red de Docker Compose, PostgreSQL se encuentra usando el nombre del servicio `db`.

---

## 20. Verificar puertos publicados

Ver los contenedores y sus puertos:

```bash
docker ps
```

También se puede usar:

```bash
docker compose ps
```

Los puertos esperados son:

```text
FastAPI: 8000:8000
PostgreSQL: 5433:5432
pgAdmin: 5050:80
```

Interpretación:

`8000:8000` significa puerto externo 8000 y puerto interno 8000.

`5433:5432` significa puerto externo 5433 y puerto interno 5432.

`5050:80` significa puerto externo 5050 y puerto interno 80.

---

## 21. Entrar a un contenedor

Entrar al contenedor del backend:

```bash
docker exec -it clase_fastapi bash
```

Salir del contenedor:

```bash
exit
```

Entrar al contenedor de PostgreSQL:

```bash
docker exec -it clase_postgres bash
```

Entrar a PostgreSQL desde el contenedor:

```bash
psql -U postgres -d appdb
```

Listar bases de datos:

```sql
\l
```

Listar tablas:

```sql
\dt
```

Salir de PostgreSQL:

```sql
\q
```

Salir del contenedor:

```bash
exit
```

---

## 22. Reiniciar servicios

Reiniciar todos los servicios:

```bash
docker compose restart
```

Reiniciar solo el backend:

```bash
docker compose restart backend
```

---

## 23. Apagar los servicios

Detener los servicios sin eliminar volúmenes:

```bash
docker compose down
```

Esto elimina los contenedores, pero conserva los datos de PostgreSQL y pgAdmin en los volúmenes.

---

## 24. Apagar y borrar datos persistentes

```bash
docker compose down -v
```

El parámetro `-v` elimina también los volúmenes.

Al usar este comando, se eliminan los datos guardados en PostgreSQL y la configuración de pgAdmin.

---

## 25. Reconstruir después de cambios

Si se modifica el código del backend o el Dockerfile:

```bash
docker compose up -d --build
```

Si el problema persiste, se puede bajar todo y volver a levantar:

```bash
docker compose down
docker compose up -d --build
```

---

## 26. Errores frecuentes

### Error: el backend no conecta con PostgreSQL

Revisar la variable:

```text
DATABASE_URL=postgresql://postgres:postgres@db:5432/appdb
```

El host debe ser:

```text
db
```

No debe ser:

```text
localhost
```

Dentro de un contenedor, `localhost` apunta al mismo contenedor, no a otro servicio.

### Error: el puerto ya está ocupado

Ejemplo:

```text
Bind for 0.0.0.0:8000 failed: port is already allocated
```

Solución: cambiar el puerto externo.

Ejemplo:

```yaml
ports:
  - "8001:8000"
```

Luego la API se consulta por:

```text
http://IP_DEL_SERVIDOR:8001
```

### Error: el contenedor se detiene

Revisar logs:

```bash
docker compose logs backend
```

O:

```bash
docker compose logs db
```

### Error: pgAdmin no conecta con PostgreSQL

Revisar que en pgAdmin se use:

```text
Host name/address: db
Port: 5432
```

---

## 27. Comandos principales de Docker para la práctica

Ver versión de Docker:

```bash
docker --version
```

Ver versión de Docker Compose:

```bash
docker compose version
```

Levantar servicios:

```bash
docker compose up -d --build
```

Ver contenedores activos:

```bash
docker ps
```

Ver servicios del Compose:

```bash
docker compose ps
```

Ver logs:

```bash
docker compose logs
```

Ver logs en tiempo real:

```bash
docker compose logs -f
```

Reiniciar servicios:

```bash
docker compose restart
```

Apagar servicios:

```bash
docker compose down
```

Apagar y borrar volúmenes:

```bash
docker compose down -v
```

Eliminar imágenes sin uso:

```bash
docker image prune
```

Eliminar contenedores detenidos:

```bash
docker container prune
```

Ver redes:

```bash
docker network ls
```

Ver volúmenes:

```bash
docker volume ls
```

---

## 28. Preparar el repositorio en GitHub

Inicializar Git:

```bash
git init
```

Agregar archivos:

```bash
git add .
```

Crear commit:

```bash
git commit -m "Despliegue inicial con FastAPI PostgreSQL y pgAdmin"
```

Configurar rama principal:

```bash
git branch -M main
```

Agregar repositorio remoto:

```bash
git remote add origin URL_DEL_REPOSITORIO
```

Subir al repositorio:

```bash
git push -u origin main
```

---

## 29. Flujo completo de la práctica

La práctica completa puede resumirse así:

```text
1. Entrar al servidor por SSH.
2. Repasar comandos básicos de Linux.
3. Instalar Docker y Docker Compose.
4. Crear la estructura del proyecto.
5. Crear main.py de FastAPI.
6. Crear requirements.txt.
7. Crear Dockerfile del backend.
8. Crear docker-compose.yml.
9. Levantar servicios con docker compose up -d --build.
10. Verificar contenedores con docker ps.
11. Revisar logs con docker compose logs.
12. Probar FastAPI en el navegador.
13. Probar pgAdmin.
14. Registrar PostgreSQL en pgAdmin usando el host db.
15. Subir el proyecto a GitHub.
```

---

## 30. Resultado esperado

Al finalizar, el proyecto debe tener tres servicios funcionando:

```text
FastAPI      http://IP_DEL_SERVIDOR:8000
Swagger      http://IP_DEL_SERVIDOR:8000/docs
pgAdmin      http://IP_DEL_SERVIDOR:5050
PostgreSQL   db:5432 dentro de Docker
PostgreSQL   IP_DEL_SERVIDOR:5433 desde fuera del contenedor
```

La estructura final del proyecto debe quedar así:

```text
clase-despliegue/
├── backend/
│   ├── app/
│   │   └── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── docker-compose.yml
├── .env.example
├── .gitignore
└── README.md
```

El punto clave de la clase es entender que Docker Compose permite levantar varios servicios conectados con una sola configuración. La API, la base de datos y pgAdmin no son elementos aislados: forman parte de una misma arquitectura desplegada.
