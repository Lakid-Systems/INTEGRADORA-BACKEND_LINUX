# pylint: disable=too-few-public-methods
"""Modelo ORM para representar consumibles usados en un servicio médico específico."""

import uuid
from sqlalchemy import Column, String, ForeignKey, DateTime, Text, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from config.db import Base

class ServiciosMedicosConsumibles(Base):
    """
    Representa la relación entre un servicio médico y los consumibles utilizados en dicho servicio.
    
    Esta tabla almacena cuántas unidades de un consumible fueron usadas en un servicio médico específico,
    junto con la fecha de uso y observaciones adicionales.
    """

    __tablename__ = "tbd_servicios_medicos_consumibles"  # Nombre de la tabla en la base de datos

    # Identificador único del registro (UUID)
    id = Column(
        String(36),
        primary_key=True,
        index=True,
        default=lambda: str(uuid.uuid4())
    )

    # Clave foránea al servicio médico en el que se usó el consumible
    id_servicio = Column(
        String(36),
        ForeignKey("tbc_servicios_medicos.id", ondelete="CASCADE"),
        nullable=False
    )

    # Clave foránea al consumible utilizado en el servicio
    id_consumible = Column(
        String(36),
        ForeignKey("tbc_consumibles.id", ondelete="CASCADE"),
        nullable=False
    )

    # Cantidad del consumible que fue utilizada
    cantidad_usada = Column(Integer, nullable=False)

    # Fecha en la que se utilizó el consumible (por defecto: momento actual)
    fecha_uso = Column(
        DateTime,
        nullable=False,
        server_default=func.now()
    )

    # Observaciones adicionales relacionadas con el uso del consumible (opcional)
    observaciones = Column(Text, nullable=True)

    # Relación con el modelo del servicio médico (ServiceM) — lado inverso definido como "consumibles"
    servicio = relationship("ServiceM", back_populates="consumibles")

    # Relación con el modelo del consumible (Consumible) — lado inverso definido como "servicios"
    consumible = relationship("Consumible", back_populates="servicios")
