from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Optional
from uuid import UUID

class ServiceMBase(BaseModel):
    nombre: str = Field(..., example="Consulta General")
    descripcion: Optional[str] = Field(None, example="Atención médica general para diagnóstico y evaluación.")
    observaciones: Optional[str] = Field(None, example="Este servicio se brinda de lunes a viernes de 8 AM a 5 PM.")
    fecha_registro: Optional[datetime] = Field(None, example="2025-03-21T22:19:44.610Z")
    fecha_actualizacion: Optional[datetime] = Field(None, example="2025-03-21T22:19:44.610Z")

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
    id: UUID = Field(..., example="b3c7e9b2-8429-4c71-ae68-61c30269c237")
    model_config = ConfigDict(from_attributes=True)
