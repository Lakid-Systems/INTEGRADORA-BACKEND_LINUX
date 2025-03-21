import models.servicios_medicos
import schemas.servicios_medicos
from sqlalchemy.orm import Session

def get_serviceM(db: Session, id: int):
    return db.query(models.servicios_medicos.ServiceM).filter(models.servicios_medicos.ServiceM.id == id).first()

def get_serviceM_by_nombre(db: Session, nombre: str):
    return db.query(models.servicios_medicos.ServiceM).filter(models.servicios_medicos.ServiceM.nombre == nombre).first()

def get_servicesM(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.servicios_medicos.ServiceM).offset(skip).limit(limit).all()

def create_serviceM(db: Session, service: schemas.servicios_medicos.ServiceMCreate):
    db_serviceM = models.servicios_medicos.ServiceM(
        nombre=service.nombre,
        descripcion=service.descripcion,
        observaciones=service.observaciones,
        fecha_registro=service.fecha_registro,
        fecha_actualizacion=service.fecha_actualizacion
    )
    db.add(db_serviceM)
    db.commit()
    db.refresh(db_serviceM)
    return db_serviceM

def update_serviceM(db: Session, id: int, service: schemas.servicios_medicos.ServiceMUpdate):
    db_serviceM = db.query(models.servicios_medicos.ServiceM).filter(models.servicios_medicos.ServiceM.id == id).first()
    if db_serviceM:
        for key, value in service.model_dump(exclude_unset=True).items():
            setattr(db_serviceM, key, value)
        db.commit()
        db.refresh(db_serviceM)
    return db_serviceM

def delete_serviceM(db: Session, id: int):
    db_serviceM = db.query(models.servicios_medicos.ServiceM).filter(models.servicios_medicos.ServiceM.id == id).first()
    if db_serviceM:
        db.delete(db_serviceM)
        db.commit()
    return db_serviceM
