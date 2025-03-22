from pydantic import BaseModel, Field, constr
from typing import Optional
import datetime

class ServiciosMedicosEspaciosBase(BaseModel):
    fk_servicio: int = Field(..., example=5)  # ID del servicio médico asignado
    fk_espacio: int = Field(..., example=12)  # ID del espacio hospitalario asignado
    observaciones: Optional[constr(max_length=255)] = Field(None, example="Este consultorio se usa solo en el turno matutino.")  
    estatus_aprobacion: Optional[constr(max_length=20)] = Field("Pendiente", example="Aprobado")  # Estado de aprobación
    estatus: Optional[constr(max_length=20)] = Field("Activo", example="Inactivo")  # Estado general del registro
    fecha_inicio: Optional[datetime.datetime] = Field(None, example="2025-04-01T08:00:00.000Z")  # Fecha de inicio del uso del espacio
    fecha_termino: Optional[datetime.datetime] = Field(None, example="2025-04-01T16:00:00.000Z")  # Fecha de fin del uso del espacio

class ServiciosMedicosEspaciosCreate(ServiciosMedicosEspaciosBase):
    """Modelo para la creación de una asignación de servicio médico a un espacio"""
    pass

class ServiciosMedicosEspaciosUpdate(BaseModel):
    """Modelo para la actualización de una asignación de servicio médico a un espacio"""
    observaciones: Optional[constr(max_length=255)] = Field(None, example="Cambio de horario a la tarde.")
    estatus_aprobacion: Optional[constr(max_length=20)] = Field(None, example="Pendiente")
    estatus: Optional[constr(max_length=20)] = Field(None, example="Activo")
    fecha_inicio: Optional[datetime.datetime] = Field(None, example="2025-04-02T08:00:00.000Z")
    fecha_termino: Optional[datetime.datetime] = Field(None, example="2025-04-02T16:00:00.000Z")
    fecha_ultima_actualizacion: datetime.datetime = Field(default_factory=datetime.datetime.utcnow, example="2025-04-01T12:00:00.000Z")

class ServiciosMedicosEspacios(ServiciosMedicosEspaciosBase):
    """Modelo para la respuesta al consultar una asignación de servicio médico a un espacio"""
    id: int = Field(..., example=100)  # ID único de la asignación
    fecha_registro: Optional[datetime.datetime] = Field(None, example="2025-03-21T22:19:44.610Z")  
    fecha_ultima_actualizacion: Optional[datetime.datetime] = Field(None, example="2025-04-01T12:00:00.000Z")  

    class Config:
        from_attributes = True
