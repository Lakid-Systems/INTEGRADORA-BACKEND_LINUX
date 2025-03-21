from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserBase(BaseModel):
    Persona_ID: int
    Nombre_Usuario: str
    Correo_Electronico: EmailStr
    Contrasena: str
    Numero_Telefonico_Movil: Optional[str] = None
    Estatus: str = "Activo"
    Fecha_Registro: Optional[datetime] = None  # ✅ Ahora es opcional para que se genere automáticamente
    Fecha_Actualizacion: Optional[datetime] = None  # ✅ Se actualizará automáticamente

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class User(UserBase):
    ID: int
    Persona_ID: int

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    Nombre_Usuario: Optional[str] = None
    Correo_Electronico: Optional[EmailStr] = None
    Contrasena: str
    Numero_Telefonico_Movil: Optional[str] = None
