from sqlalchemy import Column, Integer, ForeignKey, String, Enum, DateTime
from sqlalchemy.orm import relationship
from config.db import Base
import enum
import datetime

# Enumeraciones
class EstatusAprobacionEnum(str, enum.Enum):
    Pendiente = 'Pendiente'
    Aprobado = 'Aprobado'
    Rechazado = 'Rechazado'

class EstatusEnum(str, enum.Enum):
    Activo = 'Activo'
    Inactivo = 'Inactivo'

class ServiciosMedicosEspacios(Base):
    __tablename__ = 'tbc_servicios_medicos_espacios'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    fk_servicio = Column(Integer, ForeignKey("tbc_servicios_medicos.id", ondelete="CASCADE"), nullable=False, index=True)  # ⚠️ Corregido ForeignKey
    fk_espacio = Column(Integer, ForeignKey("tbc_espacios.id"), nullable=False, index=True)
    observaciones = Column(String(255), nullable=True)
    estatus_aprobacion = Column(Enum(EstatusAprobacionEnum), nullable=False, default=EstatusAprobacionEnum.Pendiente)
    estatus = Column(Enum(EstatusEnum), nullable=False, default=EstatusEnum.Activo)
    fecha_registro = Column(DateTime, default=datetime.datetime.utcnow)
    fecha_inicio = Column(DateTime, nullable=True)
    fecha_termino = Column(DateTime, nullable=True)
    fecha_ultima_actualizacion = Column(DateTime, nullable=True, onupdate=datetime.datetime.utcnow)

    # 🔹 Relación con Servicios Médicos
    servicio = relationship("ServiceM", back_populates="espacios")  # ⚠️ Asegurar que coincide con "espacios" en ServiceM

    # 🔹 Relación con Espacio
    espacio = relationship("Espacio", back_populates="servicios_medicos_espacios")
