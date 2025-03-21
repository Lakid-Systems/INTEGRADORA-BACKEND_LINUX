import models.puestos
import schemas.puestos
from sqlalchemy.orm import Session

def get_puesto(db: Session, id: int):
    return db.query(models.puestos.Puesto).filter(models.puestos.Puesto.PuestoID == id).first()

def get_puesto_by_nombre(db: Session, nombre: str):
    return db.query(models.puestos.Puesto).filter(models.puestos.Puesto.Nombre == nombre).first()

def get_puestos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.puestos.Puesto).offset(skip).limit(limit).all()

def create_puesto(db: Session, puesto: schemas.puestos.PuestoCreate):
    db_puesto = models.puestos.Puesto(
        Nombre=puesto.Nombre,
        Descripcion=puesto.Descripcion,
        Salario=puesto.Salario,
        Turno=puesto.Turno,
        Creado=puesto.Creado,
        Modificado=puesto.Modificado
    )
    db.add(db_puesto)
    db.commit()
    db.refresh(db_puesto)
    return db_puesto

def update_puesto(db: Session, id: int, puesto: schemas.puestos.PuestoUpdate):
    db_puesto = db.query(models.puestos.Puesto).filter(models.puestos.Puesto.PuestoID == id).first()
    if db_puesto:
        for var, value in vars(puesto).items():
            if value is not None:
                setattr(db_puesto, var, value)
        db.commit()
        db.refresh(db_puesto)
    return db_puesto

def delete_puesto(db: Session, id: int):
    db_puesto = db.query(models.puestos.Puesto).filter(models.puestos.Puesto.PuestoID == id).first()
    if db_puesto:
        db.delete(db_puesto)
        db.commit()
    return db_puesto
