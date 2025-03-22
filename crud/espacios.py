from sqlalchemy.orm import Session
import models.espacios as models
import schemas.espacios as schemas
from datetime import datetime

# 🔹 Obtener un espacio por su ID
def get_espacio(db: Session, espacio_id: int):
    """
    Retorna un espacio según su ID.
    """
    return db.query(models.Espacio).filter(models.Espacio.id == espacio_id).first()

# 🔹 Obtener todos los espacios registrados (con paginación)
def get_espacios(db: Session, skip: int = 0, limit: int = 10):
    """
    Retorna una lista de espacios con paginación (salto y límite).
    """
    return db.query(models.Espacio).offset(skip).limit(limit).all()

# 🔹 Crear un nuevo espacio
def create_espacio(db: Session, espacio: schemas.EspacioCreate):
    """
    Crea y registra un nuevo espacio en la base de datos.
    """
    db_espacio = models.Espacio(
        tipo=espacio.tipo,
        nombre=espacio.nombre,
        departamento_id=espacio.departamento_id,
        estatus=espacio.estatus,
        capacidad=espacio.capacidad,
        espacio_superior_id=espacio.espacio_superior_id,
        fecha_registro=datetime.utcnow()
    )
    db.add(db_espacio)
    try:
        db.commit()
        db.refresh(db_espacio)
    except Exception as e:
        db.rollback()
        raise e
    return db_espacio

# 🔹 Actualizar los datos de un espacio existente
def update_espacio(db: Session, espacio_id: int, espacio: schemas.EspacioUpdate):
    """
    Actualiza los campos de un espacio. Solo se modifican los valores proporcionados.
    """
    db_espacio = db.query(models.Espacio).filter(models.Espacio.id == espacio_id).first()
    if db_espacio:
        for var, value in espacio.dict(exclude_unset=True).items():
            if value is not None:
                setattr(db_espacio, var, value)
        db_espacio.fecha_actualizacion = datetime.utcnow()
        try:
            db.commit()
            db.refresh(db_espacio)
        except Exception as e:
            db.rollback()
            raise e
    return db_espacio

# 🔹 Eliminar un espacio por ID
def delete_espacio(db: Session, espacio_id: int):
    """
    Elimina un espacio de la base de datos si existe.
    """
    db_espacio = db.query(models.Espacio).filter(models.Espacio.id == espacio_id).first()
    if db_espacio:
        try:
            db.delete(db_espacio)
            db.commit()
        except Exception as e:
            db.rollback()
            raise e
    return db_espacio
