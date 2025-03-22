from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

class UserRolBase(BaseModel):
    Usuario_ID: int = Field(..., example=1, description="ID del usuario que se asigna al rol")
    Rol_ID: int = Field(..., example=2, description="ID del rol asignado al usuario")
    Estatus: bool = Field(..., example=True, description="Estado de la asignación (activo/inactivo)")
    Fecha_Registro: Optional[datetime] = Field(None, example="2025-03-21T14:30:00", description="Fecha de creación de la asignación")
    Fecha_Actualizacion: Optional[datetime] = Field(None, example="2025-03-28T09:15:00", description="Fecha de última modificación")

class UserRolCreate(UserRolBase):
    """Modelo para crear una asignación de usuario a rol"""
    pass

class UserRolUpdate(UserRolBase):
    """Modelo para actualizar una asignación existente"""
    pass

class UserRol(UserRolBase):
    """Modelo para visualizar una asignación de usuario a rol"""
    Usuario_ID: int = Field(..., example=1)
    Rol_ID: int = Field(..., example=2)

    class Config:
        orm_mode = True
