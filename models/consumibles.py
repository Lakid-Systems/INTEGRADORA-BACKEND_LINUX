from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from config.db import Base

# 🔹 Modelo que representa los insumos o materiales médicos consumibles del hospital
class Consumible(Base):
    __tablename__ = "tbc_consumibles"  # Nombre de la tabla en la base de datos

    # ID único del consumible (PK)
    id = Column(Integer, primary_key=True, autoincrement=True)

    # Nombre del consumible (ej: "Guantes", "Jeringas")
    nombre = Column(String(100), nullable=False)

    # Descripción detallada del consumible
    descripcion = Column(Text, nullable=False)

    # Tipo de consumible (ej: "Material quirúrgico", "Farmacéutico")
    tipo = Column(String(50), nullable=False)

    # Departamento al que está asignado (ej: "Urgencias", "Farmacia")
    departamento = Column(String(50), nullable=False)

    # Cantidad disponible en inventario
    cantidad_existencia = Column(Integer, nullable=False)

    # Detalles adicionales del consumible (opcional)
    detalle = Column(Text, nullable=True)

    # Fecha de registro del consumible (generada automáticamente)
    fecha_registro = Column(DateTime, nullable=False, server_default=func.now())

    # Fecha de última actualización del registro
    fecha_actualizacion = Column(DateTime, nullable=True, onupdate=func.now())

    # Estatus del consumible (True = activo, False = inactivo)
    estatus = Column(Boolean, nullable=True)

    # Observaciones adicionales del estado o uso del consumible (opcional)
    observaciones = Column(Text, nullable=True)

    # Campo adicional opcional para indicar el espacio o área médica asociada
    espacio_medico = Column(String(50), nullable=True)

    # 🔗 Relación con tabla Servicios Médicos Consumibles (1:N)
    servicios = relationship("ServiciosMedicosConsumibles", back_populates="consumible")
