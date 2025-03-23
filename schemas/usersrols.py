from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID


class UserRolBase(BaseModel):
    Usuario_ID: UUID = Field(..., example="b5cb2487-e6ac-4419-9916-47a10d4f4103", description="ID del usuario que se asigna al rol")
    Rol_ID: UUID = Field(..., example="d7c2e7f8-5ac4-4d0b-8e3b-fbe2216c4a2c", description="ID del rol asignado al usuario")
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
    Usuario_ID: UUID = Field(..., example="b5cb2487-e6ac-4419-9916-47a10d4f4103")
    Rol_ID: UUID = Field(..., example="d7c2e7f8-5ac4-4d0b-8e3b-fbe2216c4a2c")

    class Config:
        orm_mode = True
