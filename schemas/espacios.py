from pydantic import BaseModel, constr, Field
from typing import Optional
import datetime

class EspacioBase(BaseModel):
    tipo: constr(max_length=50) = Field(..., example="Consultorio")  # Tipo de espacio hospitalario
    nombre: constr(max_length=100) = Field(..., example="Consultorio 101")  # Nombre del espacio
    departamento_id: Optional[int] = Field(None, example=3)  # ID del departamento al que pertenece
    estatus: constr(max_length=20) = Field(..., example="Activo")  # Estado del espacio (Activo/Inactivo)
    capacidad: Optional[int] = Field(None, example=5)  # Capacidad máxima de personas en el espacio
    espacio_superior_id: Optional[int] = Field(None, example=1)  # ID del espacio superior (si es parte de otro espacio)

class EspacioCreate(EspacioBase):
    """Modelo para la creación de un espacio hospitalario"""
    pass

class EspacioUpdate(BaseModel):
    """Modelo para la actualización de un espacio hospitalario"""
    tipo: Optional[constr(max_length=50)] = Field(None, example="Sala de Operaciones")
    nombre: Optional[constr(max_length=100)] = Field(None, example="Quirófano Principal")
    departamento_id: Optional[int] = Field(None, example=5)
    estatus: Optional[constr(max_length=20)] = Field(None, example="Inactivo")
    capacidad: Optional[int] = Field(None, example=10)
    espacio_superior_id: Optional[int] = Field(None, example=2)
    fecha_actualizacion: datetime.datetime = Field(default_factory=datetime.datetime.utcnow, example="2025-04-02T12:00:00.000Z")

class Espacio(EspacioBase):
    """Modelo para la respuesta al consultar un espacio hospitalario"""
    id: int = Field(..., example=101)  # ID único del espacio
    fecha_registro: Optional[datetime.datetime] = Field(None, example="2025-03-21T22:19:44.610Z")  
    fecha_actualizacion: Optional[datetime.datetime] = Field(None, example="2025-04-01T12:00:00.000Z")  

    class Config:
        from_attributes = True
