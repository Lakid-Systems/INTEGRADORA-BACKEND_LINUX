from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum, Date, text
from sqlalchemy.orm import relationship
from config.db import Base
import enum
from datetime import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID

# 🔹 Enumeración para los géneros disponibles
class MyGenero(str, enum.Enum):
    Masculino = "Masculino"
    Femenino = "Femenino"
    Otro = "Otro"

# 🔹 Enumeración para los tipos de sangre disponibles
class MySangre(str, enum.Enum):
    AP = "A+"
    AN = "A-"
    BP = "B+"
    BN = "B-"
    ABP = "AB+"
    ABN = "AB-"
    OP = "O+"
    ON = "O-" 

# 🔹 Modelo de persona asociado a los usuarios del sistema
class Person(Base):
    __tablename__ = "tbb_personas"  # Nombre de la tabla en la base de datos

    # ID único de la persona (PK)
    ID = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)

    # Relación con el modelo de usuario (1 a 1)
    usuario = relationship("User", back_populates="persona", uselist=False)  # Relación inversa con User

    # Título de cortesía, por ejemplo: "Sr.", "Dra.", "Ing."
    Titulo_Cortesia = Column(String(20))

    # Nombre(s) de la persona
    Nombre = Column(String(80), nullable=False)

    # Primer apellido (obligatorio)
    Primer_Apellido = Column(String(80), nullable=False)

    # Segundo apellido (opcional)
    Segundo_Apellido = Column(String(80), nullable=True)

    # CURP única por persona
    CURP = Column(String(18), unique=True, nullable=False)

    # Correo electrónico único
    Correo_Electronico = Column(String(100), unique=True, nullable=False)

    # Teléfono personal o de contacto (opcional)
    Telefono = Column(String(15), nullable=True)

    # Fecha de nacimiento de la persona
    Fecha_Nacimiento = Column(Date, nullable=False)

    # Ruta o nombre del archivo de la fotografía (opcional)
    Fotografia = Column(String(100), nullable=True)

    # Género (Masculino, Femenino, Otro)
    Genero = Column(Enum(MyGenero), nullable=False)

    # Tipo de sangre (usando Enum personalizado)
    Tipo_Sangre = Column(Enum(MySangre), nullable=False)

    # Estatus activo/inactivo (booleano)
    Estatus = Column(Boolean, default=False, nullable=False)

    # Fecha de registro automática
    Fecha_Registro = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'))

    # Fecha de última modificación (actualiza automáticamente)
    Fecha_Actualizacion = Column(DateTime, nullable=True, onupdate=datetime.utcnow)
