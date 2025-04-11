# pylint: disable=too-few-public-methods, invalid-name, non-ascii-name
"""Modelo ORM para representar la asignación de espacios físicos a servicios médicos."""

import enum
import uuid
import datetime
from sqlalchemy import Column, String, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from config.db import Base

class EstatusAprobacionEnum(str, enum.Enum):
    """
    Estado de aprobación de un espacio médico asignado.

    Valores posibles:
    - Pendiente: Aún no ha sido aprobado ni rechazado.
    - Aprobado: La asignación fue aceptada.
    - Rechazado: La asignación fue denegada.
    """
    Pendiente = 'Pendiente'
    Aprobado = 'Aprobado'
    Rechazado = 'Rechazado'


class EstatusEnum(str, enum.Enum):
    """
    Estado general del registro (activo/inactivo).

    Valores posibles:
    - Activo: La asignación está en uso.
    - Inactivo: La asignación está cancelada o caduca.
    """
    Activo = 'Activo'
    Inactivo = 'Inactivo'


class ServiciosMedicosEspacios(Base):
    """
    Modelo que representa la asignación de un espacio físico a un servicio médico.
    
    Permite llevar control de qué servicio médico está usando qué espacio del hospital,
    cuándo lo está usando, y bajo qué condiciones fue aprobado.
    """

    __tablename__ = 'tbc_servicios_medicos_espacios'  # Nombre de la tabla en la base de datos

    # ID único para cada asignación (UUID)
    id = Column(
        String(36),
        primary_key=True,
        index=True,
        default=lambda: str(uuid.uuid4())
    )

    # Clave foránea al servicio médico asignado
    fk_servicio = Column(
        String(36),
        ForeignKey("tbc_servicios_medicos.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    # Clave foránea al espacio físico asignado
    fk_espacio = Column(
        String(36),
        ForeignKey("tbc_espacios.id"),
        nullable=False,
        index=True
    )

    # Comentarios u observaciones adicionales sobre la asignación
    observaciones = Column(String(255), nullable=True)

    # Estado de aprobación de la asignación
    estatus_aprobacion = Column(
        Enum(EstatusAprobacionEnum),
        nullable=False,
        default=EstatusAprobacionEnum.Pendiente
    )

    # Estado general del registro (activo o inactivo)
    estatus = Column(
        Enum(EstatusEnum),
        nullable=False,
        default=EstatusEnum.Activo
    )

    # Fecha en la que se registró la asignación
    fecha_registro = Column(
        DateTime,
        default=datetime.datetime.utcnow
    )

    # Fecha de inicio de uso del espacio (opcional)
    fecha_inicio = Column(DateTime, nullable=True)

    # Fecha de término de uso del espacio (opcional)
    fecha_termino = Column(DateTime, nullable=True)

    # Fecha en que se actualizó por última vez la asignación
    fecha_ultima_actualizacion = Column(
        DateTime,
        nullable=True,
        onupdate=datetime.datetime.utcnow
    )

    # Relación con el servicio médico (lado inverso: espacios)
    servicio = relationship("ServiceM", back_populates="espacios")

    # Relación con el espacio físico (lado inverso: servicios_medicos_espacios)
    espacio = relationship("Espacio", back_populates="servicios_medicos_espacios")
