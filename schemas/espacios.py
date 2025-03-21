from pydantic import BaseModel, constr, Field
from typing import Optional
import datetime

class EspacioBase(BaseModel):
    tipo: constr(max_length=50)
    nombre: constr(max_length=100)
    departamento_id: Optional[int] = None
    estatus: constr(max_length=20)
    capacidad: Optional[int] = None
    espacio_superior_id: Optional[int] = None

class EspacioCreate(EspacioBase):
    pass

class EspacioUpdate(BaseModel):
    tipo: Optional[constr(max_length=50)] = None
    nombre: Optional[constr(max_length=100)] = None
    departamento_id: Optional[int] = None
    estatus: Optional[constr(max_length=20)] = None
    capacidad: Optional[int] = None
    espacio_superior_id: Optional[int] = None
    fecha_actualizacion: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)

class Espacio(EspacioBase):
    id: int
    fecha_registro: Optional[datetime.datetime] = None
    fecha_actualizacion: Optional[datetime.datetime] = None

    class Config:
        from_attributes = True
