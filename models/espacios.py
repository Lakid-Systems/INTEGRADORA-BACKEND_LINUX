import uuid
from sqlalchemy.dialects.postgresql import UUID

class Espacio(Base):
    __tablename__ = 'tbc_espacios'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    tipo = Column(Enum(TipoEspacioEnum), nullable=False)
    nombre = Column(String(100), nullable=False)

    departamento_id = Column(
        UUID(as_uuid=True),
        ForeignKey("tbc_departamentos.id", ondelete="SET NULL"),
        nullable=True,
        index=True
    )

    estatus = Column(Enum(EstatusEnum), nullable=False, default=EstatusEnum.Activo)
    fecha_registro = Column(DateTime, default=datetime.datetime.utcnow)
    fecha_actualizacion = Column(DateTime, nullable=True, onupdate=datetime.datetime.utcnow)
    capacidad = Column(Integer, nullable=True)

    espacio_superior_id = Column(
        UUID(as_uuid=True),
        ForeignKey("tbc_espacios.id", ondelete="SET NULL"),
        nullable=True
    )

    servicios_medicos_espacios = relationship("ServiciosMedicosEspacios", back_populates="espacio")
