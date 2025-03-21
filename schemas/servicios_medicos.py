from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class ServiceMBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    observaciones: Optional[str] = None
    fecha_registro: Optional[datetime] = None
    fecha_actualizacion: Optional[datetime] = None

class ServiceMCreate(ServiceMBase):
    pass

class ServiceMUpdate(BaseModel):  
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    observaciones: Optional[str] = None
    fecha_actualizacion: Optional[datetime] = None

class Service(ServiceMBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
