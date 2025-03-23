from config.db import Base
from sqlalchemy import Column, String, ForeignKey, DateTime, Text, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid

# 🔹 Modelo que representa los consumibles usados en un servicio médico específico
class ServiciosMedicosConsumibles(Base):
    __tablename__ = "tbd_servicios_medicos_consumibles"  # Nombre de la tabla en la base de datos

    # ID único del registro (UUID como string)
    id = Column(String(36), primary_key=True, index=True, default=lambda: str(uuid.uuid4()))

    # ID del servicio médico asociado
    id_servicio = Column(String(36), ForeignKey("tbc_servicios_medicos.id", ondelete="CASCADE"), nullable=False)

    # ID del consumible utilizado
    id_consumible = Column(String(36), ForeignKey("tbc_consumibles.id", ondelete="CASCADE"), nullable=False)

    # Cantidad de consumible utilizada
    cantidad_usada = Column(Integer, nullable=False)

    # Fecha de uso del consumible (se asigna automáticamente)
    fecha_uso = Column(DateTime, nullable=False, server_default=func.now())

    # Observaciones adicionales (opcional)
    observaciones = Column(Text, nullable=True)

    # 🔹 Relación con `ServiceM`
    servicio = relationship("ServiceM", back_populates="consumibles")

    # 🔹 Relación con `Consumible`
    consumible = relationship("Consumible", back_populates="servicios")
