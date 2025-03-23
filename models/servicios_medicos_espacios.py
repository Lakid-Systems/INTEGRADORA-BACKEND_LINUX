from sqlalchemy import Column, String, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from config.db import Base
import enum
import datetime
import uuid

# 🔹 Enumeración para el estado de aprobación
class EstatusAprobacionEnum(str, enum.Enum):
    Pendiente = 'Pendiente'
    Aprobado = 'Aprobado'
    Rechazado = 'Rechazado'

# 🔹 Enumeración para el estado general
class EstatusEnum(str, enum.Enum):
    Activo = 'Activo'
    Inactivo = 'Inactivo'

# 🔹 Modelo que representa la asignación de un espacio físico a un servicio médico
class ServiciosMedicosEspacios(Base):
    __tablename__ = 'tbc_servicios_medicos_espacios'  # Nombre de la tabla en la base de datos

    # ID único de la asignación (UUID como string)
    id = Column(String(36), primary_key=True, index=True, default=lambda: str(uuid.uuid4()))

    # Clave foránea al servicio médico
    fk_servicio = Column(String(36), ForeignKey("tbc_servicios_medicos.id", ondelete="CASCADE"), nullable=False, index=True)

    # Clave foránea al espacio hospitalario
    fk_espacio = Column(String(36), ForeignKey("tbc_espacios.id"), nullable=False, index=True)

    # Observaciones adicionales (opcional)
    observaciones = Column(String(255), nullable=True)

    # Estado de aprobación del espacio
    estatus_aprobacion = Column(Enum(EstatusAprobacionEnum), nullable=False, default=EstatusAprobacionEnum.Pendiente)

    # Estatus activo/inactivo
    estatus = Column(Enum(EstatusEnum), nullable=False, default=EstatusEnum.Activo)

    # Fecha en que se registró la asignación
    fecha_registro = Column(DateTime, default=datetime.datetime.utcnow)

    # Fecha de inicio del uso del espacio
    fecha_inicio = Column(DateTime, nullable=True)

    # Fecha de término del uso del espacio
    fecha_termino = Column(DateTime, nullable=True)

    # Fecha de última actualización
    fecha_ultima_actualizacion = Column(DateTime, nullable=True, onupdate=datetime.datetime.utcnow)

    # 🔹 Relación con Servicios Médicos
    servicio = relationship("ServiceM", back_populates="espacios")

    # 🔹 Relación con Espacio
    espacio = relationship("Espacio", back_populates="servicios_medicos_espacios")
