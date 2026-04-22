from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class UsuarioCreate(BaseModel):
    nombre: str = Field(..., max_length=100)
    apellido: str = Field(..., max_length=100)
    correo: str = Field(..., max_length=150)
    username: str = Field(..., max_length=50)
    password: str = Field(..., min_length=6, max_length=128)
    rol: str = Field(default="usuario", max_length=50)
    activo: bool = True


class UsuarioResponse(BaseModel):
    id_usuario: int
    nombre: str = Field(..., max_length=100)
    apellido: str = Field(..., max_length=100)
    correo: str = Field(..., max_length=150)
    username: str = Field(..., max_length=50)
    rol: str = Field(default="usuario", max_length=50)
    activo: bool = True
    fecha_creacion: datetime
    fecha_actualizacion: datetime | None = None

    model_config = ConfigDict(from_attributes=True)
