# pylint: disable=too-few-public-methods
"""Modelo ORM para representar los consumibles médicos del hospital."""

import uuid
import enum
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, Enum, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from config.db import Base

class TipoConsumibleEnum(str, enum.Enum):
    """
    Enumeración para representar los tipos de consumibles médicos.
    
    Valores posibles:
    - Medicamento: Medicamentos y fármacos.
    - Insumo: Material médico como gasas, guantes, etc.
    - Equipo: Herramientas o aparatos reutilizables.
    - Otro: Cualquier otro tipo de consumible.
    """
    Medicamento = "Medicamento"
    Insumo = "Insumo"
    Equipo = "Equipo"
    Otro = "Otro"

class Consumible(Base):
    """
    Representa un consumible o insumo médico utilizado dentro del hospital.
    
    Ejemplos: guantes, jeringas, medicamentos, equipo médico, etc.
    Cada instancia corresponde a una fila en la tabla 'tbc_consumibles'.
    """
    __tablename__ = "tbc_consumibles"  # Nombre de la tabla en la base de datos

    # Identificador único del consumible (UUID)
    id = Column(String(36), primary_key=True, index=True, default=lambda: str(uuid.uuid4()))

    # Nombre del consumible
    nombre = Column(String(100), nullable=False)

    # Descripción detallada del consumible
    descripcion = Column(Text, nullable=False)

    # Tipo de consumible, definido por la enumeración TipoConsumibleEnum
    tipo = Column(Enum(TipoConsumibleEnum), nullable=False)

    # Clave foránea al departamento al que pertenece el consumible (puede ser nulo)
    departamento_id = Column(
        String(36),
        ForeignKey("tbc_departamentos.id", ondelete="SET NULL"),
        nullable=True
    )

    # Cantidad existente en inventario
    cantidad_existencia = Column(Integer, nullable=False)

    # Detalles adicionales del consumible (opcional)
    detalle = Column(Text, nullable=True)

    # Fecha de creación del registro (asignada automáticamente)
    fecha_registro = Column(DateTime, nullable=False, server_default=func.now())

    # Fecha de la última actualización (se actualiza automáticamente al modificar)
    fecha_actualizacion = Column(DateTime, nullable=True, onupdate=func.now())

    # Estatus del consumible (activo/inactivo)
    estatus = Column(Boolean, nullable=True)

    # Observaciones adicionales (opcional)
    observaciones = Column(Text, nullable=True)

    # Nombre del espacio físico donde se encuentra (opcional)
    espacio_medico = Column(String(50), nullable=True)

    # Relación con la tabla de servicios médicos consumibles
    servicios = relationship(
        "ServiciosMedicosConsumibles",  # Clase relacionada
        back_populates="consumible"    # Atributo inverso en la clase relacionada
    )
