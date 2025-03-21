from sqlalchemy import Column,Integer,String,Boolean,DateTime,ForeignKey,Enum
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base
import models.persons
import enum



class MyEstatusCita(enum.Enum):
    activo = "Activo"
    inactivo = "Inactivo"
    bloqueado = "Bloqueado"
    suspendido = "Suspendido"


class Cita(Base):
    __tablename__ = "tbb_citas"
    
    ID = Column(Integer, primary_key=True, index=True)
    Persona_ID = Column(Integer, ForeignKey("tbb_personas.ID"))
    Hora_Cita = Column(DateTime)
    Telefono = Column(String(20)) 
    Correo_Electronico = Column(String(255))
    Motivo_Cita = Column(String(255))
    Estatus = Column(Enum(MyEstatusCita))
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)

    