import models.consumibles
import schemas.consumibles
from sqlalchemy.orm import Session

def get_consumible(db: Session, id: int):
    return db.query(models.consumibles.Consumible).filter(models.consumibles.Consumible.id == id).first()

def get_consumibles_by_nombre(db: Session, nombre: str):
    return db.query(models.consumibles.Consumible).filter(models.consumibles.Consumible.nombre == nombre).first()

def get_consumibles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.consumibles.Consumible).offset(skip).limit(limit).all()

def create_consumible(db: Session, consumible: schemas.consumibles.ConsumibleCreate):
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


def update_consumible(db: Session, id: int, consumible: schemas.consumibles.ConsumibleUpdate):
    db_consumible = db.query(models.consumibles.Consumible).filter(models.consumibles.Consumible.id == id).first()
    if db_consumible:
        for key, value in consumible.dict(exclude_unset=True).items():
            setattr(db_consumible, key, value)
        db.commit()
        db.refresh(db_consumible)
    return db_consumible

def delete_consumible(db: Session, id: int):
    db_consumible = db.query(models.consumibles.Consumible).filter(models.consumibles.Consumible.id == id).first()
    if db_consumible:
        db.delete(db_consumible)
        db.commit()
    return db_consumible
