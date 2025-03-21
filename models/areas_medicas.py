from sqlalchemy import Column, String, Text, DateTime, Boolean, text
from sqlalchemy.ext.declarative import declarative_base
import uuid
from datetime import datetime

Base = declarative_base()

class AreaMedica(Base):
    __tablename__ = "tbc_areas_medicas"

    ID = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False)
    Nombre = Column(String(150), nullable=False)
    Descripcion = Column(Text, nullable=True)
    
    Estatus = Column(Boolean, default=True, nullable=False)
    
    Fecha_Registro = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'))  
    Fecha_Actualizacion = Column(DateTime, nullable=True, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<AreaMedica(ID={self.ID}, Nombre='{self.Nombre}', Estatus='{self.Estatus}')>"
