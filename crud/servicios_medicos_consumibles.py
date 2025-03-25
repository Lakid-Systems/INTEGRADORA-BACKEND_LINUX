"""Módulo CRUD para manejar la relación entre servicios médicos y consumibles."""

from sqlalchemy.orm import Session
import models.servicios_medicos_consumibles
import schemas.servicios_medicos_consumibles

def get_by_id(db: Session, id: int):  # pylint: disable=redefined-builtin
    """
    Obtiene un registro por su ID.

    Args:
        db (Session): Sesión de base de datos.
        id (int): Identificador del registro.

    Returns:
        ServiciosMedicosConsumibles: Instancia encontrada o None.
    """
    return db.query(models.servicios_medicos_consumibles.ServiciosMedicosConsumibles).filter(
        models.servicios_medicos_consumibles.ServiciosMedicosConsumibles.id == id
    ).first()


def get_all(db: Session, skip: int = 0, limit: int = 10):
    """
    Obtiene todos los registros con paginación.

    Args:
        db (Session): Sesión de base de datos.
        skip (int): Registros a omitir.
        limit (int): Cantidad máxima de registros.

    Returns:
        List[ServiciosMedicosConsumibles]: Lista de registros.
    """
    return db.query(models.servicios_medicos_consumibles.ServiciosMedicosConsumibles).offset(
        skip
    ).limit(limit).all()


def create(
    db: Session, data: schemas.servicios_medicos_consumibles.ServiciosMedicosConsumiblesCreate
):
    """
    Crea un nuevo registro de consumo de servicio médico.

    Args:
        db (Session): Sesión de base de datos.
        data (ServiciosMedicosConsumiblesCreate): Datos del nuevo registro.

    Returns:
        ServiciosMedicosConsumibles: Instancia creada.
    """
    db_record = models.servicios_medicos_consumibles.ServiciosMedicosConsumibles(
        id_servicio=data.id_servicio,
        id_consumible=data.id_consumible,
        cantidad_usada=data.cantidad_usada,
        fecha_uso=data.fecha_uso,
        observaciones=data.observaciones
    )
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record


def update(
    db: Session,
    id: int,  # pylint: disable=redefined-builtin
    data: schemas.servicios_medicos_consumibles.ServiciosMedicosConsumiblesUpdate
):
    """
    Actualiza los datos de un registro existente.

    Args:
        db (Session): Sesión de base de datos.
        id (int): ID del registro a modificar.
        data (ServiciosMedicosConsumiblesUpdate): Campos a actualizar.

    Returns:
        ServiciosMedicosConsumibles: Instancia actualizada o None si no se encontró.
    """
    db_record = db.query(models.servicios_medicos_consumibles.ServiciosMedicosConsumibles).filter(
        models.servicios_medicos_consumibles.ServiciosMedicosConsumibles.id == id
    ).first()
    if db_record:
        for key, value in data.dict(exclude_unset=True).items():
            setattr(db_record, key, value)
        db.commit()
        db.refresh(db_record)
    return db_record


def delete(db: Session, id: int):  # pylint: disable=redefined-builtin
    """
    Elimina un registro por su ID.

    Args:
        db (Session): Sesión de base de datos.
        id (int): ID del registro a eliminar.

    Returns:
        ServiciosMedicosConsumibles: Instancia eliminada o None si no se encontró.
    """
    db_record = db.query(models.servicios_medicos_consumibles.ServiciosMedicosConsumibles).filter(
        models.servicios_medicos_consumibles.ServiciosMedicosConsumibles.id == id
    ).first()
    if db_record:
        db.delete(db_record)
        db.commit()
    return db_record
