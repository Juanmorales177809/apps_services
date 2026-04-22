from sqlalchemy import Boolean, Column, DateTime, Integer, String, text
from db import Base


class Usuario(Base):
    __tablename__ = "usuarios"
    __table_args__ = {"schema": "Laboratorios"}

    id_usuario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    correo = Column(String(150), nullable=False, unique=True)
    username = Column(String(50), nullable=False, unique=True)
    hashed_password = Column(String(255), nullable=False)
    rol = Column(String(50), nullable=False, server_default=text("'usuario'"))
    activo = Column(Boolean, nullable=False, server_default=text("true"))
    fecha_creacion = Column(
        DateTime,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    )
    fecha_actualizacion = Column(DateTime, nullable=True)
