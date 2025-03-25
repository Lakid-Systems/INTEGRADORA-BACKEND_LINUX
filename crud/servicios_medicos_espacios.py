"""Módulo CRUD para gestionar la relación entre servicios médicos y espacios."""

from datetime import datetime
from sqlalchemy.orm import Session
import models.servicios_medicos_espacios as models
import schemas.servicios_medicos_espacios as schemas

def get_servicio_espacio(db: Session, servicio_espacio_id: int):
    """
    Obtiene un registro de servicio-espacio por su ID.

    Args:
        db (Session): Sesión de base de datos.
        servicio_espacio_id (int): ID de la relación.

    Returns:
        ServiciosMedicosEspacios: Instancia encontrada o None.
    """
    return db.query(models.ServiciosMedicosEspacios).filter(
        models.ServiciosMedicosEspacios.id == servicio_espacio_id
    ).first()


def get_servicios_espacios(db: Session, skip: int = 0, limit: int = 10):
    """
    Obtiene una lista paginada de servicios médicos vinculados a espacios.

    Args:
        db (Session): Sesión de base de datos.
        skip (int): Registros a omitir.
        limit (int): Máximo número de registros.

    Returns:
        List[ServiciosMedicosEspacios]: Lista de registros.
    """
    return db.query(models.ServiciosMedicosEspacios).offset(skip).limit(limit).all()


def create_servicio_espacio(
    db: Session, servicio_espacio: schemas.ServiciosMedicosEspaciosCreate
):
    """
    Crea un nuevo vínculo entre un servicio médico y un espacio.

    Args:
        db (Session): Sesión de base de datos.
        servicio_espacio (ServiciosMedicosEspaciosCreate): Datos del nuevo registro.

    Returns:
        ServiciosMedicosEspacios: Instancia creada.
    """
    db_servicio_espacio = models.ServiciosMedicosEspacios(
        **servicio_espacio.dict(),
        fecha_registro=datetime.utcnow()
    )
    db.add(db_servicio_espacio)
    db.commit()
    db.refresh(db_servicio_espacio)
    return db_servicio_espacio


def update_servicio_espacio(
    db: Session,
    servicio_espacio_id: int,
    servicio_espacio: schemas.ServiciosMedicosEspaciosUpdate
):
    """
    Actualiza un vínculo existente entre un servicio y un espacio.

    Args:
        db (Session): Sesión de base de datos.
        servicio_espacio_id (int): ID del registro a actualizar.
        servicio_espacio (ServiciosMedicosEspaciosUpdate): Datos a modificar.

    Returns:
        ServiciosMedicosEspacios: Instancia actualizada o None si no se encontró.
    """
    db_servicio_espacio = db.query(models.ServiciosMedicosEspacios).filter(
        models.ServiciosMedicosEspacios.id == servicio_espacio_id
    ).first()
    if db_servicio_espacio:
        for var, value in servicio_espacio.dict(exclude_unset=True).items():
            setattr(db_servicio_espacio, var, value)
        db.commit()
        db.refresh(db_servicio_espacio)
    return db_servicio_espacio


def delete_servicio_espacio(db: Session, servicio_espacio_id: int):
    """
    Elimina un vínculo entre servicio médico y espacio.

    Args:
        db (Session): Sesión de base de datos.
        servicio_espacio_id (int): ID del registro a eliminar.

    Returns:
        ServiciosMedicosEspacios: Instancia eliminada o None si no existe.
    """
    db_servicio_espacio = db.query(models.ServiciosMedicosEspacios).filter(
        models.ServiciosMedicosEspacios.id == servicio_espacio_id
    ).first()
    if db_servicio_espacio:
        db.delete(db_servicio_espacio)
        db.commit()
    return db_servicio_espacio
