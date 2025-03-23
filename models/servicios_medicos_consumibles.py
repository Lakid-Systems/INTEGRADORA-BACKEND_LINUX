from config.db import Base
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from sqlalchemy.dialects.postgresql import UUID


class ServiciosMedicosConsumibles(Base):
    __tablename__ = "tbd_servicios_medicos_consumibles"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    id_servicio = Column(UUID(as_uuid=True), ForeignKey("tbc_servicios_medicos.id", ondelete="CASCADE"), nullable=False)
    id_consumible = Column(UUID(as_uuid=True), ForeignKey("tbc_consumibles.id", ondelete="CASCADE"), nullable=False)
    cantidad_usada = Column(Integer, nullable=False)
    fecha_uso = Column(DateTime, nullable=False, server_default=func.now())
    observaciones = Column(Text, nullable=True)

    # 🔹 Relación con `ServiceM`
    servicio = relationship("ServiceM", back_populates="consumibles")

    # 🔹 Relación con `Consumible`
    consumible = relationship("Consumible", back_populates="servicios")
