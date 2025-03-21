from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum, Date, text
from sqlalchemy.orm import relationship
from config.db import Base
import enum
from datetime import datetime

class MyGenero(str, enum.Enum):
    Masculino = "Masculino"
    Femenino = "Femenino"
    Otro = "Otro"

class MySangre(str, enum.Enum):
    AP = "A+"
    AN = "A-"
    BP = "B+"
    BN = "B-"
    ABP = "AB+"
    ABN = "AB-"
    OP = "O+"
    ON = "O-" 

class Person(Base):
    __tablename__ = "tbb_personas"

    ID = Column(Integer, primary_key=True, index=True)
    usuario = relationship("User", back_populates="persona", uselist=False)  # 🔹 ¡NO importar `User` aquí!

    Titulo_Cortesia = Column(String(20))
    Nombre = Column(String(80), nullable=False)
    Primer_Apellido = Column(String(80), nullable=False)
    Segundo_Apellido = Column(String(80), nullable=True)
    CURP = Column(String(18), unique=True, nullable=False)
    Correo_Electronico = Column(String(100), unique=True, nullable=False)  
    Telefono = Column(String(15), nullable=True)  
    Fecha_Nacimiento = Column(Date, nullable=False)
    Fotografia = Column(String(100), nullable=True)
    Genero = Column(Enum(MyGenero), nullable=False)
    Tipo_Sangre = Column(Enum(MySangre), nullable=False)
    Estatus = Column(Boolean, default=False, nullable=False)

    Fecha_Registro = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'))
    Fecha_Actualizacion = Column(DateTime, nullable=True, onupdate=datetime.utcnow)
