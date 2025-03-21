from pydantic import BaseModel
from typing import Optional
from datetime import datetime, time

class HorarioBase(BaseModel):
    empleado_id: int
    nombre: str
    especialidad: str
    dia_semana: str
    hora_inicio: time
    hora_fin: time
    turno: str
    nombre_departamento: str
    nombre_sala: str
    fecha_creacion: Optional[datetime] = None
    fecha_actualizacion: Optional[datetime] = None

class HorarioCreate(HorarioBase):
    pass

class HorarioUpdate(HorarioBase):
    pass

class Horario(HorarioBase):
    horario_id: int

    class Config:
        orm_mode = True
