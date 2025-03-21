from sqlalchemy.orm import Session
import models.servicios_medicos_espacios as models
import schemas.servicios_medicos_espacios as schemas
from datetime import datetime

def get_servicio_espacio(db: Session, servicio_espacio_id: int):
    return db.query(models.ServiciosMedicosEspacios).filter(models.ServiciosMedicosEspacios.id == servicio_espacio_id).first()

def get_servicios_espacios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.ServiciosMedicosEspacios).offset(skip).limit(limit).all()

def create_servicio_espacio(db: Session, servicio_espacio: schemas.ServiciosMedicosEspaciosCreate):
    db_servicio_espacio = models.ServiciosMedicosEspacios(**servicio_espacio.dict(), fecha_registro=datetime.utcnow())
    db.add(db_servicio_espacio)
    db.commit()
    db.refresh(db_servicio_espacio)
    return db_servicio_espacio

def update_servicio_espacio(db: Session, servicio_espacio_id: int, servicio_espacio: schemas.ServiciosMedicosEspaciosUpdate):
    db_servicio_espacio = db.query(models.ServiciosMedicosEspacios).filter(models.ServiciosMedicosEspacios.id == servicio_espacio_id).first()
    if db_servicio_espacio:
        for var, value in servicio_espacio.dict(exclude_unset=True).items():
            setattr(db_servicio_espacio, var, value)
        db.commit()
        db.refresh(db_servicio_espacio)
    return db_servicio_espacio

def delete_servicio_espacio(db: Session, servicio_espacio_id: int):
    db_servicio_espacio = db.query(models.ServiciosMedicosEspacios).filter(models.ServiciosMedicosEspacios.id == servicio_espacio_id).first()
    if db_servicio_espacio:
        db.delete(db_servicio_espacio)
        db.commit()
    return db_servicio_espacio
