from pydantic import BaseModel, constr, Field
from typing import Optional
import datetime

class ServiciosMedicosEspaciosBase(BaseModel):
    fk_servicio: int
    fk_espacio: int
    observaciones: Optional[constr(max_length=255)] = None
    estatus_aprobacion: Optional[constr(max_length=20)] = "Pendiente"
    estatus: Optional[constr(max_length=20)] = "Activo"
    fecha_inicio: Optional[datetime.datetime] = None
    fecha_termino: Optional[datetime.datetime] = None

class ServiciosMedicosEspaciosCreate(ServiciosMedicosEspaciosBase):
    pass

class ServiciosMedicosEspaciosUpdate(BaseModel):
    observaciones: Optional[constr(max_length=255)] = None
    estatus_aprobacion: Optional[constr(max_length=20)] = None
    estatus: Optional[constr(max_length=20)] = None
    fecha_inicio: Optional[datetime.datetime] = None
    fecha_termino: Optional[datetime.datetime] = None
    fecha_ultima_actualizacion: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)

class ServiciosMedicosEspacios(ServiciosMedicosEspaciosBase):
    id: int
    fecha_registro: Optional[datetime.datetime] = None
    fecha_ultima_actualizacion: Optional[datetime.datetime] = None

    class Config:
        from_attributes = True
