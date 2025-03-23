from sqlalchemy import Column, String, Text, DateTime, Boolean, text
from config.db import Base
from datetime import datetime
import uuid

# 🔹 Modelo que representa un área médica del hospital (ej: Pediatría, Cardiología)
class AreaMedica(Base):
    __tablename__ = "tbc_areas_medicas"  # Nombre de la tabla en la base de datos

    # ID único del área médica (UUID como string)
    ID = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False)

    # Nombre del área médica
    Nombre = Column(String(150), nullable=False)

    # Descripción detallada del área médica (opcional)
    Descripcion = Column(Text, nullable=True)

    # Estatus del área (True = activa, False = inactiva)
    Estatus = Column(Boolean, default=True, nullable=False)

    # Fecha de creación del registro (automática)
    Fecha_Registro = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'))

    # Fecha de última actualización (si se modifica)
    Fecha_Actualizacion = Column(DateTime, nullable=True, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<AreaMedica(ID={self.ID}, Nombre='{self.Nombre}', Estatus='{self.Estatus}')>"
