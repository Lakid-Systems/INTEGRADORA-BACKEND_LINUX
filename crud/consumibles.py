import models.consumibles
import schemas.consumibles
from sqlalchemy.orm import Session

# 🔹 Obtener un consumible por su ID
def get_consumible(db: Session, id: int):
    """
    Retorna un consumible por su identificador único (ID).
    """
    return db.query(models.consumibles.Consumible).filter(models.consumibles.Consumible.id == id).first()

# 🔹 Obtener un consumible por su nombre
def get_consumibles_by_nombre(db: Session, nombre: str):
    """
    Retorna el primer consumible que coincida exactamente con el nombre proporcionado.
    """
    return db.query(models.consumibles.Consumible).filter(models.consumibles.Consumible.nombre == nombre).first()

# 🔹 Obtener todos los consumibles (con paginación)
def get_consumibles(db: Session, skip: int = 0, limit: int = 10):
    """
    Retorna una lista paginada de consumibles disponibles.
    """
    return db.query(models.consumibles.Consumible).offset(skip).limit(limit).all()

# 🔹 Crear un nuevo consumible
def create_consumible(db: Session, consumible: schemas.consumibles.ConsumibleCreate):
    """
    Registra un nuevo consumible en la base de datos.
    """
    db_consumible = models.consumibles.Consumible(
        nombre=consumible.nombre,
        descripcion=consumible.descripcion,
        tipo=consumible.tipo,
        departamento=consumible.departamento,
        cantidad_existencia=consumible.cantidad_existencia,
        detalle=consumible.detalle,
        estatus=consumible.estatus,
        observaciones=consumible.observaciones,
        espacio_medico=consumible.espacio_medico
    )
    db.add(db_consumible)
    db.commit()
    db.refresh(db_consumible)
    return db_consumible

# 🔹 Actualizar un consumible existente
def update_consumible(db: Session, id: int, consumible: schemas.consumibles.ConsumibleUpdate):
    """
    Actualiza los campos del consumible especificado. Solo modifica los datos enviados.
    """
    db_consumible = db.query(models.consumibles.Consumible).filter(models.consumibles.Consumible.id == id).first()
    if db_consumible:
        for key, value in consumible.dict(exclude_unset=True).items():
            setattr(db_consumible, key, value)
        db.commit()
        db.refresh(db_consumible)
    return db_consumible

# 🔹 Eliminar un consumible por ID
def delete_consumible(db: Session, id: int):
    """
    Elimina un consumible de la base de datos según su ID.
    """
    db_consumible = db.query(models.consumibles.Consumible).filter(models.consumibles.Consumible.id == id).first()
    if db_consumible:
        db.delete(db_consumible)
        db.commit()
    return db_consumible
