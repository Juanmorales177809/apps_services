from sqlalchemy import Column, Integer, String
from db import Base

class Laboratorio(Base):
    __tablename__ = "laboratorios"
    __table_args__ = {"schema": "Laboratorios"}
    
    
    idLaboratorio = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=True)
    tipo = Column(String(30), nullable=True)
    ubicacion = Column(String(50), nullable=True)

    