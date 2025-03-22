from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

class AreaMedicaBase(BaseModel):
    Nombre: str
    Descripcion: Optional[str] = None
    Estatus: Optional[bool] = True  
    Fecha_Registro: Optional[datetime] = Field(None, description="(Opcional) Se genera automáticamente.")
    Fecha_Actualizacion: Optional[datetime] = Field(None, description="(Opcional) Se actualiza automáticamente.")

class AreaMedicaCreate(AreaMedicaBase):
    pass

class AreaMedicaUpdate(BaseModel):
    Nombre: Optional[str] = None
    Descripcion: Optional[str] = None
    Estatus: Optional[bool] = None  
    Fecha_Actualizacion: Optional[datetime] = Field(None, description="(Opcional) Se actualiza automáticamente si no se envía.")

class AreaMedica(AreaMedicaBase):
    ID: str

    class Config:
        from_attributes = True
