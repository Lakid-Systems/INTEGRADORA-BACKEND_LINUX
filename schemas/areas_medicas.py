from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID


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
    ID: UUID = Field(..., example="9b4e1bc0-8129-4cf5-9e7c-1c802e60decd")

    class Config:
        from_attributes = True
