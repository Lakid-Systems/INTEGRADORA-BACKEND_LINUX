# pylint: disable=too-few-public-methods
"""Modelo ORM para representar los consumibles médicos del hospital."""

import uuid
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from config.db import Base

class Consumible(Base):
    """
    Representa un consumible o insumo médico utilizado dentro del hospital,
    como guantes, jeringas, medicamentos, etc.
    """

    __tablename__ = "tbc_consumibles"

    id = Column(
        String(36),
        primary_key=True,
        index=True,
        default=lambda: str(uuid.uuid4())
    )
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=False)
    tipo = Column(String(50), nullable=False)
    departamento = Column(String(50), nullable=False)
    cantidad_existencia = Column(Integer, nullable=False)
    detalle = Column(Text, nullable=True)
    fecha_registro = Column(
    DateTime,
    nullable=False,
    server_default=func.now()  # pylint: disable=not-callable
    )

    fecha_actualizacion = Column(
    DateTime,
    nullable=True,
    onupdate=func.now()  # pylint: disable=not-callable
    )
    estatus = Column(Boolean, nullable=True)
    observaciones = Column(Text, nullable=True)
    espacio_medico = Column(String(50), nullable=True)

    servicios = relationship(
        "ServiciosMedicosConsumibles",
        back_populates="consumible"
    )
