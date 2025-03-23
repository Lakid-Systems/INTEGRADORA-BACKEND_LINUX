from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class DepartamentoBase(BaseModel):
    nombre: str
    area_medica_id: Optional[UUID] = None
    departamento_superior_id: Optional[UUID] = None
    responsable_id: Optional[UUID] = None
    estatus: Optional[bool] = True
    fecha_registro: Optional[datetime] = None
    fecha_actualizacion: Optional[datetime] = None

class DepartamentoCreate(DepartamentoBase):
    pass  # Se usa la misma estructura de DepartamentoBase

class DepartamentoUpdate(BaseModel):
    nombre: Optional[str] = None
    area_medica_id: Optional[UUID] = None
    departamento_superior_id: Optional[UUID] = None
    responsable_id: Optional[UUID] = None
    estatus: Optional[bool] = None
    fecha_actualizacion: Optional[datetime] = None

class Departamento(DepartamentoBase):
    id: UUID

    class Config:
        orm_mode = True
