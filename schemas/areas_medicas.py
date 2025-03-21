from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class AreaMedicaBase(BaseModel):
    Nombre: str
    Descripcion: Optional[str] = None
    Estatus: Optional[bool] = True  
    Fecha_Registro: Optional[datetime] = None
    Fecha_Actualizacion: Optional[datetime] = None

class AreaMedicaCreate(AreaMedicaBase):
    pass

class AreaMedicaUpdate(BaseModel):
    Nombre: Optional[str] = None
    Descripcion: Optional[str] = None
    Estatus: Optional[bool] = None  
    Fecha_Actualizacion: Optional[datetime] = None

class AreaMedica(AreaMedicaBase):
    ID: str  

    class Config:
        from_attributes = True
