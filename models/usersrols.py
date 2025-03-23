from sqlalchemy import Column, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base
import models.users, models.rols  # Importaciones necesarias para las relaciones
import uuid
from sqlalchemy.dialects.postgresql import UUID


# 🔹 Modelo que representa la relación entre usuarios y roles
# Cada combinación Usuario_ID + Rol_ID forma una clave primaria compuesta
class UserRol(Base):
    __tablename__ = "tbd_usuarios_roles"  # Nombre de la tabla relacional (intermedia)

    # 🔑 Clave primaria compuesta: ID del usuario
    Usuario_ID = Column(UUID(as_uuid=True), ForeignKey("tbb_usuarios.ID"), primary_key=True)

    # 🔑 Clave primaria compuesta: ID del rol
    Rol_ID = Column(UUID(as_uuid=True), ForeignKey("tbc_roles.ID"), primary_key=True)

    # Estado de la asignación (activo/inactivo)
    Estatus = Column(Boolean, nullable=True)

    # Fecha en que se creó la asignación
    Fecha_Registro = Column(DateTime, nullable=True)

    # Fecha de última modificación
    Fecha_Actualizacion = Column(DateTime, nullable=True)

    # 🔹 Relación con Rol
    rol = relationship("Rol", back_populates="usuarios_roles")