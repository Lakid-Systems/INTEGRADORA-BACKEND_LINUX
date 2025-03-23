from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime, date
from uuid import UUID


class PersonBase(BaseModel):
    Titulo_Cortesia: str = Field(..., example="Dr.")  # Prefijo de cortesía (Ej: Dr., Sr., Sra.)
    Nombre: str = Field(..., example="Carlos")  # Nombre de la persona
    Primer_Apellido: str = Field(..., example="Ramírez")  # Primer apellido
    Segundo_Apellido: str = Field(..., example="Gómez")  # Segundo apellido (puede ser opcional)
    CURP: str = Field(..., example="RAGC890101HDFLNN09")  # CURP de la persona
    Correo_Electronico: str = Field(..., example="carlos.ramirez@example.com")  # Correo válido
    Telefono: str = Field(..., example="5551234567")  # Teléfono móvil o de contacto
    Fecha_Nacimiento: date = Field(..., example="1989-01-01")  # Fecha de nacimiento en formato YYYY-MM-DD
    Fotografia: Optional[str] = Field(None, example="https://example.com/photo.jpg")  # URL de la foto (opcional)
    Genero: str = Field(..., example="Masculino")  # Opciones: Masculino, Femenino, Otro
    Tipo_Sangre: str = Field(..., example="O+")  # Tipo de sangre (Ej: A+, O-, etc.)
    Estatus: bool = Field(..., example=True)  # Estado de la persona (activo/inactivo)
    Fecha_Registro: Optional[datetime] = Field(None, example="2025-03-21T22:19:44.610Z")  # Fecha de creación
    Fecha_Actualizacion: Optional[datetime] = Field(None, example="2025-03-21T22:19:44.610Z")  # Última actualización

class PersonCreate(PersonBase):
    """Modelo para la creación de una persona"""
    pass

class PersonUpdate(PersonBase):
    """Modelo para la actualización de una persona"""
    pass

class Person(PersonBase):
    """Modelo para la respuesta al consultar una persona"""
    ID: UUID = Field(..., example="3fa85f64-5717-4562-b3fc-2c963f66afa6")

    class Config:
        from_attributes = True
