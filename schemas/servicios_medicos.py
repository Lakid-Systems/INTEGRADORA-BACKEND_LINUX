from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Optional

class ServiceMBase(BaseModel):
    nombre: str = Field(..., example="Consulta General")  # Nombre del servicio
    descripcion: Optional[str] = Field(None, example="Atención médica general para diagnóstico y evaluación.")  # Breve descripción
    observaciones: Optional[str] = Field(None, example="Este servicio se brinda de lunes a viernes de 8 AM a 5 PM.")  # Notas adicionales
    fecha_registro: Optional[datetime] = Field(None, example="2025-03-21T22:19:44.610Z")  # Fecha de creación del registro
    fecha_actualizacion: Optional[datetime] = Field(None, example="2025-03-21T22:19:44.610Z")  # Última modificación

class ServiceMCreate(ServiceMBase):
    """Modelo para la creación de un servicio médico"""
    pass

class ServiceMUpdate(BaseModel):  
    """Modelo para la actualización de un servicio médico"""
    nombre: Optional[str] = Field(None, example="Consulta Pediátrica")
    descripcion: Optional[str] = Field(None, example="Consulta médica especializada en niños y adolescentes.")
    observaciones: Optional[str] = Field(None, example="Disponible solo en el turno matutino.")
    fecha_actualizacion: Optional[datetime] = Field(None, example="2025-03-22T10:00:00.000Z")

class Service(ServiceMBase):
    """Modelo para la respuesta al consultar un servicio médico"""
    id: int = Field(..., example=10)  # ID único del servicio médico
    model_config = ConfigDict(from_attributes=True)
