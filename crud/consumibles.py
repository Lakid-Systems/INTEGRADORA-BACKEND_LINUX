"""Módulo CRUD para operaciones relacionadas con consumibles médicos."""

from sqlalchemy.orm import Session
import models.consumibles
import schemas.consumibles

def get_consumibles(db: Session, skip: int = 0, limit: int = 10):
    """
    Obtiene una lista paginada de consumibles.

    Args:
        db (Session): Sesión de base de datos.
        skip (int): Cantidad de registros a omitir.
        limit (int): Cantidad máxima de registros a retornar.

    Returns:
        List[Consumible]: Lista de consumibles.
    """
    return db.query(models.consumibles.Consumible).offset(skip).limit(limit).all()


def get_consumible(db: Session, id: int):  # pylint: disable=redefined-builtin
    """
    Obtiene un consumible por su ID.

    Args:
        db (Session): Sesión de base de datos.
        id (int): Identificador del consumible.

    Returns:
        Consumible: Instancia encontrada o None.
    """
    return db.query(models.consumibles.Consumible).filter(
        models.consumibles.Consumible.id == id
    ).first()


def get_consumibles_by_nombre(db: Session, nombre: str):
    """
    Obtiene un consumible por su nombre.

    Args:
        db (Session): Sesión de base de datos.
        nombre (str): Nombre del consumible.

    Returns:
        Consumible: Instancia encontrada o None.
    """
    return db.query(models.consumibles.Consumible).filter(
        models.consumibles.Consumible.nombre == nombre
    ).first()


def create_consumible(db: Session, consumible: schemas.consumibles.ConsumibleCreate):
    """
    Crea un nuevo consumible.

    Args:
        db (Session): Sesión de base de datos.
        consumible (ConsumibleCreate): Datos del nuevo consumible.

    Returns:
        Consumible: Instancia creada.
    """
    db_consumible = models.consumibles.Consumible(**consumible.dict())
    db.add(db_consumible)
    db.commit()
    db.refresh(db_consumible)
    return db_consumible


def update_consumible(
    db: Session, id: int, consumible: schemas.consumibles.ConsumibleUpdate
):  # pylint: disable=redefined-builtin
    """
    Actualiza un consumible existente.

    Args:
        db (Session): Sesión de base de datos.
        id (int): ID del consumible a actualizar.
        consumible (ConsumibleUpdate): Datos nuevos a aplicar.

    Returns:
        Consumible: Instancia actualizada o None.
    """
    db_consumible = db.query(models.consumibles.Consumible).filter(
        models.consumibles.Consumible.id == id
    ).first()
    if db_consumible:
        for key, value in consumible.dict(exclude_unset=True).items():
            setattr(db_consumible, key, value)
        db.commit()
        db.refresh(db_consumible)
    return db_consumible


def delete_consumible(db: Session, id: int):  # pylint: disable=redefined-builtin
    """
    Elimina un consumible por su ID.

    Args:
        db (Session): Sesión de base de datos.
        id (int): ID del consumible a eliminar.

    Returns:
        Consumible: Instancia eliminada o None.
    """
    db_consumible = db.query(models.consumibles.Consumible).filter(
        models.consumibles.Consumible.id == id
    ).first()
    if db_consumible:
        db.delete(db_consumible)
        db.commit()
    return db_consumible
