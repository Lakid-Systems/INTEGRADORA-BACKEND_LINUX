# pylint: disable=too-few-public-methods, invalid-name, non-ascii-name
"""Modelo ORM para representar los espacios físicos del hospital."""

import enum
import uuid
import datetime
from sqlalchemy import Column, String, Enum, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship
from config.db import Base

class TipoEspacioEnum(str, enum.Enum):
    """
    Enumeración de tipos de espacios disponibles en el hospital.

    Ejemplos:
    - Consultorio: Espacio para atención médica individual.
    - Quirófano: Sala de operaciones.
    - Habitación: Espacio asignado a pacientes.
    - Piso: Nivel dentro del hospital, puede contener otros espacios.
    """
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
    """
    Enumeración para el estatus del espacio.

    - Activo: Espacio actualmente en uso.
    - Inactivo: Espacio fuera de operación.
    """
    Activo = 'Activo'
    Inactivo = 'Inactivo'


class Espacio(Base):
    """
    Modelo que representa un espacio físico dentro del hospital.
    
    Puede representar desde una cama o consultorio, hasta pisos y edificios enteros.
    """

    __tablename__ = 'tbc_espacios'  # Nombre de la tabla en la base de datos

    # ID único del espacio (UUID)
    id = Column(
        String(36),
        primary_key=True,
        index=True,
        default=lambda: str(uuid.uuid4())
    )

    # Tipo de espacio (según la enumeración TipoEspacioEnum)
    tipo = Column(Enum(TipoEspacioEnum), nullable=False)

    # Nombre identificativo del espacio (ej. "Quirófano 3")
    nombre = Column(String(100), nullable=False)

    # Clave foránea al departamento responsable (puede ser nulo)
    departamento_id = Column(
        String(36),
        ForeignKey("tbc_departamentos.id", ondelete="SET NULL"),
        nullable=True,
        index=True
    )

    # Estatus del espacio (activo/inactivo)
    estatus = Column(
        Enum(EstatusEnum),
        nullable=False,
        default=EstatusEnum.Activo
    )

    # Fecha de registro del espacio (por defecto, fecha actual)
    fecha_registro = Column(
        DateTime,
        default=datetime.datetime.utcnow
    )

    # Fecha de última actualización del espacio (opcional)
    fecha_actualizacion = Column(
        DateTime,
        nullable=True,
        onupdate=datetime.datetime.utcnow
    )

    # Capacidad del espacio (opcional, ej. personas o camas)
    capacidad = Column(Integer, nullable=True)

    # Referencia a otro espacio "padre" (por ejemplo, una cama dentro de una habitación)
    espacio_superior_id = Column(
        String(36),
        ForeignKey("tbc_espacios.id", ondelete="SET NULL"),
        nullable=True
    )

    # Relación con la tabla ServiciosMedicosEspacios
    servicios_medicos_espacios = relationship(
        "ServiciosMedicosEspacios",
        back_populates="espacio"
    )
