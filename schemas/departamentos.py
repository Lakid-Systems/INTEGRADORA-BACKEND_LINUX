from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class DepartamentoBase(BaseModel):
    nombre: str
    area_medica_id: Optional[int] = None
    departamento_superior_id: Optional[int] = None
    responsable_id: Optional[int] = None
    estatus: Optional[bool] = True
    fecha_registro: Optional[datetime] = None
    fecha_actualizacion: Optional[datetime] = None

class DepartamentoCreate(DepartamentoBase):
    pass  # Se usa la misma estructura de DepartamentoBase

class DepartamentoUpdate(BaseModel):
    nombre: Optional[str] = None
    area_medica_id: Optional[int] = None
    departamento_superior_id: Optional[int] = None
    responsable_id: Optional[int] = None
    estatus: Optional[bool] = None
    fecha_actualizacion: Optional[datetime] = None

class Departamento(DepartamentoBase):
    id: int

    class Config:
        orm_mode = True
