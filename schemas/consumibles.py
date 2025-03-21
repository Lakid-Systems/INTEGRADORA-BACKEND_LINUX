from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class ConsumibleBase(BaseModel):
    nombre: str
    descripcion: str
    tipo: str
    departamento: str
    cantidad_existencia: int
    detalle: Optional[str] = None
    estatus: Optional[bool] = None
    observaciones: Optional[str] = None
    espacio_medico: Optional[str] = None
    fecha_registro: Optional[datetime] = None  #
    fecha_actualizacion: Optional[datetime] = None 

class ConsumibleCreate(ConsumibleBase):
    pass

class ConsumibleUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    tipo: Optional[str] = None
    departamento: Optional[str] = None
    cantidad_existencia: Optional[int] = None
    detalle: Optional[str] = None
    estatus: Optional[bool] = None
    observaciones: Optional[str] = None
    espacio_medico: Optional[str] = None
    fecha_actualizacion: Optional[datetime] = None  

class Consumible(ConsumibleBase):
    id: int

    class Config:
        orm_mode = True
