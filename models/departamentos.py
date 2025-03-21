from sqlalchemy import Column, Integer, String, Boolean, DateTime
from config.db import Base
import datetime

class Departamentos(Base):
    __tablename__ = "tbc_departamentos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    area_medica_id = Column(Integer, nullable=True)
    departamento_superior_id = Column(Integer, nullable=True)
    responsable_id = Column(Integer, nullable=True)

    estatus = Column(Boolean, default=True)
    fecha_registro = Column(DateTime, default=datetime.datetime.utcnow)
    fecha_actualizacion = Column(DateTime, nullable=True, onupdate=datetime.datetime.utcnow)
