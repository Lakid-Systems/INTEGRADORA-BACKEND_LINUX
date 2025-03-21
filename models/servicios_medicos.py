from sqlalchemy import Column, Integer, String, Text, DateTime, func
from sqlalchemy.orm import relationship
from config.db import Base

class ServiceM(Base):
    __tablename__ = "tbc_servicios_medicos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False, unique=True)
    descripcion = Column(Text, nullable=True)
    observaciones = Column(Text, nullable=True)
    fecha_registro = Column(DateTime, nullable=False, server_default=func.now())
    fecha_actualizacion = Column(DateTime, nullable=True, onupdate=func.now())

    # 🔹 Relación con Servicios Médicos Consumibles
    consumibles = relationship("ServiciosMedicosConsumibles", back_populates="servicio")

    # 🔹 Relación con Servicios Médicos Espacios (⚠️ POSIBLE ERROR AQUÍ)
    espacios = relationship("ServiciosMedicosEspacios", back_populates="servicio")  # ⚠️ Asegurar que "servicio" existe en ServiciosMedicosEspacios
