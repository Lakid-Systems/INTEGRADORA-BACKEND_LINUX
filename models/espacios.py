from config.db import Base
from sqlalchemy import Column, Integer, String, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import enum
import datetime

class TipoEspacioEnum(str, enum.Enum):
    Consultorio = 'Consultorio'
    Laboratorio = 'Laboratorio'
    Quirófano = 'Quirófano'
    Sala_de_Espera = 'Sala de Espera'
    Edificio = 'Edificio'
    Estacionamiento = 'Estacionamiento'
    Habitación = 'Habitación'
    Cama = 'Cama'
    Sala_Maternidad = 'Sala Maternidad'
    Cunero = 'Cunero'
    Anfiteatro = 'Anfiteatro'
    Oficina = 'Oficina'
    Sala_de_Juntas = 'Sala de Juntas'
    Auditorio = 'Auditorio'
    Cafeteria = 'Cafeteria'
    Capilla = 'Capilla'
    Farmacia = 'Farmacia'
    Ventanilla = 'Ventanilla'
    Recepción = 'Recepción'
    Piso = 'Piso'

class EstatusEnum(str, enum.Enum):
    Activo = 'Activo'
    Inactivo = 'Inactivo'

class Espacio(Base):
    __tablename__ = 'tbc_espacios'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tipo = Column(Enum(TipoEspacioEnum), nullable=False)
    nombre = Column(String(100), nullable=False)
    departamento_id = Column(Integer, ForeignKey("tbc_departamentos.id", ondelete="SET NULL"), nullable=True, index=True)
    estatus = Column(Enum(EstatusEnum), nullable=False, default=EstatusEnum.Activo)
    fecha_registro = Column(DateTime, default=datetime.datetime.utcnow)
    fecha_actualizacion = Column(DateTime, nullable=True, onupdate=datetime.datetime.utcnow)
    capacidad = Column(Integer, nullable=True)
    espacio_superior_id = Column(Integer, ForeignKey("tbc_espacios.id", ondelete="SET NULL"), nullable=True)

    # Relación con Servicios Médicos Espacios
    servicios_medicos_espacios = relationship("ServiciosMedicosEspacios", back_populates="espacio") 
