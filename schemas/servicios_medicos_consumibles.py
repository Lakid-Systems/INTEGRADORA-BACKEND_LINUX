from typing import Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime

class ServiciosMedicosConsumiblesBase(BaseModel):
    id_servicio: int
    id_consumible: int
    cantidad_usada: int
    fecha_uso: Optional[datetime] = None
    observaciones: Optional[str] = None

class ServiciosMedicosConsumiblesCreate(ServiciosMedicosConsumiblesBase):
    pass

class ServiciosMedicosConsumiblesUpdate(BaseModel):
    cantidad_usada: Optional[int] = None
    fecha_uso: Optional[datetime] = None
    observaciones: Optional[str] = None

class ServiciosMedicosConsumibles(ServiciosMedicosConsumiblesBase):
    id: int

    model_config = ConfigDict(from_attributes=True) 
