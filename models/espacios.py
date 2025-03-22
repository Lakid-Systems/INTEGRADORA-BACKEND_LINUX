from config.db import Base
from sqlalchemy import Column, Integer, String, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import enum
import datetime

# 🔹 Enumeración de tipos de espacios disponibles en el hospital
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

# 🔹 Enumeración para el estatus del espacio
class EstatusEnum(str, enum.Enum):
    Activo = 'Activo'
    Inactivo = 'Inactivo'

# 🔹 Modelo que representa un espacio físico dentro del hospital
class Espacio(Base):
    __tablename__ = 'tbc_espacios'  # Nombre de la tabla en la base de datos

    # ID único del espacio (PK)
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    # Tipo de espacio según la enumeración definida (obligatorio)
    tipo = Column(Enum(TipoEspacioEnum), nullable=False)

    # Nombre identificador del espacio (ej: "Consultorio 3B", "Quirófano 2")
    nombre = Column(String(100), nullable=False)

    # ID del departamento al que pertenece (relación externa, opcional)
    departamento_id = Column(
        Integer,
        ForeignKey("tbc_departamentos.id", ondelete="SET NULL"),
        nullable=True,
        index=True
    )

    # Estado del espacio (Activo o Inactivo)
    estatus = Column(Enum(EstatusEnum), nullable=False, default=EstatusEnum.Activo)

    # Fecha de creación del registro (por defecto: ahora)
    fecha_registro = Column(DateTime, default=datetime.datetime.utcnow)

    # Fecha de última actualización del espacio
    fecha_actualizacion = Column(DateTime, nullable=True, onupdate=datetime.datetime.utcnow)

    # Capacidad máxima del espacio (opcional)
    capacidad = Column(Integer, nullable=True)

    # ID del espacio superior (jerarquía, opcional)
    espacio_superior_id = Column(
        Integer,
        ForeignKey("tbc_espacios.id", ondelete="SET NULL"),
        nullable=True
    )

    # 🔗 Relación con tabla intermedia Servicios Médicos Espacios
    servicios_medicos_espacios = relationship(
        "ServiciosMedicosEspacios",
        back_populates="espacio"
    )
