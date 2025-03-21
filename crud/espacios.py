from sqlalchemy.orm import Session
import models.espacios as models
import schemas.espacios as schemas
from datetime import datetime

def get_espacio(db: Session, espacio_id: int):
    return db.query(models.Espacio).filter(models.Espacio.id == espacio_id).first()

def get_espacios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Espacio).offset(skip).limit(limit).all()

def create_espacio(db: Session, espacio: schemas.EspacioCreate):
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

def update_espacio(db: Session, espacio_id: int, espacio: schemas.EspacioUpdate):
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

def delete_espacio(db: Session, espacio_id: int):
    db_espacio = db.query(models.Espacio).filter(models.Espacio.id == espacio_id).first()
    if db_espacio:
        try:
            db.delete(db_espacio)
            db.commit()
        except Exception as e:
            db.rollback()
            raise e
    return db_espacio
