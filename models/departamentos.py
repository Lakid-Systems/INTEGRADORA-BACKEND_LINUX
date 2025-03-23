import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, Boolean, DateTime
from config.db import Base
import datetime

class Departamentos(Base):
    __tablename__ = "tbc_departamentos"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    nombre = Column(String(100), nullable=False)
    area_medica_id = Column(UUID(as_uuid=True), nullable=True)
    departamento_superior_id = Column(UUID(as_uuid=True), nullable=True)
    responsable_id = Column(UUID(as_uuid=True), nullable=True)

    estatus = Column(Boolean, default=True)
    fecha_registro = Column(DateTime, default=datetime.datetime.utcnow)
    fecha_actualizacion = Column(DateTime, nullable=True, onupdate=datetime.datetime.utcnow)
