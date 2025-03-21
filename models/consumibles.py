from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from config.db import Base

class Consumible(Base):
    __tablename__ = "tbc_consumibles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=False)
    tipo = Column(String(50), nullable=False)
    departamento = Column(String(50), nullable=False)
    cantidad_existencia = Column(Integer, nullable=False)
    detalle = Column(Text, nullable=True)
    fecha_registro = Column(DateTime, nullable=False, server_default=func.now())  
    fecha_actualizacion = Column(DateTime, nullable=True, onupdate=func.now())  
    estatus = Column(Boolean, nullable=True)
    observaciones = Column(Text, nullable=True)
    espacio_medico = Column(String(50), nullable=True)

    # 🔹 Relación con `ServiciosMedicosConsumibles`
    servicios = relationship("ServiciosMedicosConsumibles", back_populates="consumible")
