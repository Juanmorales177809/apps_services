from pydantic import BaseModel, Field

class LaboratorioBase(BaseModel):
    nombre : str = Field(..., max_length=50)
    tipo : str = Field(..., max_length=30)
    ubicacion : str = Field(..., max_length=50)