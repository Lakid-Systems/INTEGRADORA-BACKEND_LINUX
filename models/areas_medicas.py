# pylint: disable=too-few-public-methods
"""Modelo ORM para representar las áreas médicas del hospital."""

from datetime import datetime
import uuid
from sqlalchemy import Column, String, Text, DateTime, Boolean, text
from config.db import Base

class AreaMedica(Base):
    """
    Representa un área médica dentro del hospital.
    
    Cada instancia de esta clase equivale a una fila en la tabla 'tbc_areas_medicas'.
    Ejemplos de áreas médicas: Pediatría, Cardiología, Urgencias, etc.
    """

    __tablename__ = "tbc_areas_medicas"  # Nombre de la tabla en la base de datos

    # Identificador único del área médica (UUID)
    ID = Column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),  # Genera automáticamente un UUID al crear el registro
        nullable=False
    )

    # Nombre del área médica (obligatorio)
    Nombre = Column(String(150), nullable=False)

    # Descripción detallada del área médica (opcional)
    Descripcion = Column(Text, nullable=True)

    # Estado del registro (activo o inactivo). Por defecto es True (activo)
    Estatus = Column(Boolean, default=True, nullable=False)

    # Fecha de creación del registro, asignada automáticamente por el servidor
    Fecha_Registro = Column(
        DateTime,
        nullable=False,
        server_default=text('CURRENT_TIMESTAMP')  # Valor por defecto actual del servidor
    )

    # Fecha de la última actualización del registro (automáticamente se actualiza con cada modificación)
    Fecha_Actualizacion = Column(
        DateTime,
        nullable=True,
        onupdate=datetime.utcnow  # Actualiza con la hora actual cuando se modifica el registro
    )

    def __repr__(self):
        """
        Representación legible de una instancia del modelo AreaMedica.
        Útil para depuración y logs.
        """
        return (
            f"<AreaMedica(ID={self.ID}, Nombre='{self.Nombre}', "
            f"Estatus='{self.Estatus}')>"
        )
