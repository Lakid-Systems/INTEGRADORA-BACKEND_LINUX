from typing import List, Union,Literal
from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional
import models.persons
class PersonBase(BaseModel):
    Titulo_Cortesia: str
    Nombre: str
    Primer_Apellido: str
    Segundo_Apellido: str
    CURP: str  
    Correo_Electronico: str 
    Telefono: str  
    Fecha_Nacimiento: date
    Fotografia: Optional[str] = None 
    Genero: str#List[Literal["Masculino", "Femenino", "Otro"]]
    Tipo_Sangre: str
    Estatus: bool
    Fecha_Registro: Optional[datetime] = None  # ✅ Ahora es opcional
    Fecha_Actualizacion: Optional[datetime] = None

class PersonCreate(PersonBase):
    pass

class PersonUpdate(PersonBase):
    pass

class Person(PersonBase):
    ID: int
    class Config:
        from_attributes = True 


