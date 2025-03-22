from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum, text
from sqlalchemy.orm import relationship
from config.db import Base
import enum
from datetime import datetime

# 🔹 Enumeración de estados posibles para la cuenta de usuario
class MyEstatus(str, enum.Enum):
    Activo = "Activo"
    Inactivo = "Inactivo"
    Bloqueado = "Bloqueado"
    Suspendido = "Suspendido"

# 🔹 Modelo de usuario del sistema
class User(Base):
    __tablename__ = "tbb_usuarios"  # Nombre de la tabla en la base de datos

    # ID único del usuario (PK)
    ID = Column(Integer, primary_key=True, index=True)

    # Relación con la tabla tbb_personas (FK)
    Persona_ID = Column(Integer, ForeignKey("tbb_personas.ID"), nullable=False)

    # Relación ORM: un usuario está vinculado a una persona
    persona = relationship("Person", back_populates="usuario")  # Relación inversa en Person

    # Nombre único de usuario (para login)
    Nombre_Usuario = Column(String(60), unique=True, nullable=False)

    # Correo electrónico del usuario (único)
    Correo_Electronico = Column(String(100), unique=True, nullable=False)

    # Contraseña cifrada del usuario
    Contrasena = Column(String(255), nullable=False)

    # Número de teléfono móvil (opcional)
    Numero_Telefonico_Movil = Column(String(20), nullable=True)

    # Estado del usuario (activo, inactivo, suspendido, bloqueado)
    Estatus = Column(Enum(MyEstatus), default=MyEstatus.Activo, nullable=False)

    # Fecha de registro automático (se genera al crear el registro)
    Fecha_Registro = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'))

    # Fecha de última modificación (actualiza automáticamente al modificar)
    Fecha_Actualizacion = Column(DateTime, nullable=True, onupdate=datetime.utcnow)
