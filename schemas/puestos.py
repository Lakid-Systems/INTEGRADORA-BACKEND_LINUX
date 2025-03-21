from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class TurnoEnum(str, Enum):
    Mañana = "Mañana"
    Tarde = "Tarde"
    Noche = "Noche"

class PuestoBase(BaseModel):
    Nombre: str
    Descripcion: Optional[str] = None
    Salario: Optional[float] = None
    Turno: Optional[TurnoEnum] = None
    Creado: datetime
    Modificado: Optional[datetime] = None

class PuestoCreate(PuestoBase):
    pass

class PuestoUpdate(PuestoBase):
    pass

class Puesto(PuestoBase):
    PuestoID: int

    class Config:
        orm_mode = True
