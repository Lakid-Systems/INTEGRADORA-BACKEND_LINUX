from sqlalchemy import func, Column, Integer, String, Boolean, DateTime, Enum, Date, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base
import enum, datetime


# Enum para el personal Medico
class EnumTipoPersonal(enum.Enum):
    Médico = "Médico"
    Enfermero = "Enfermero"
    Administrativo = "Administrativo"
    Directivo = "Directivo"
    Apoyo = "Apoyo"
    Residente = "Residente"
    Interno = "Interno"


# Enum para el personal
class EnumEstatus(enum.Enum):
    Activo = "Activo"
    Inactivo = "Inactivo"


# Modelo de la base
class PersonalMedico(Base):
    __tablename__ = "tbb_personal_medico"

    Persona_ID =  Column(Integer, ForeignKey("tbb_personas.ID"), primary_key=True,  index=True)
    Departamento_ID = Column(Integer)
    Cedula_Profesional = Column(String(100))
    Tipo = Column(Enum(EnumTipoPersonal))
    Especialidad = Column(String(255))
    Fecha_Registro = Column(DateTime, default=func.now())
    Fecha_Contratacion = Column(DateTime)
    Fecha_Termino_Contrato = Column(DateTime)
    Salario = Column(DECIMAL(10, 2))
    Estatus = Column(Enum(EnumEstatus))
    Fecha_Actualizacion = Column(DateTime)