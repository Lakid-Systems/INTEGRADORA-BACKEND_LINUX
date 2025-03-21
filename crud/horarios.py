from sqlalchemy.orm import Session
import models.horarios
import schemas.horarios

def create_horario(db: Session, horario: schemas.horarios.HorarioCreate):
    db_horario = models.horarios.Horario(**horario.dict())
    db.add(db_horario)
    db.commit()
    db.refresh(db_horario)
    return db_horario

def get_horario(db: Session, horario_id: int):
    return db.query(models.horarios.Horario).filter(models.horarios.Horario.horario_id == horario_id).first()

def get_horarios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.horarios.Horario).offset(skip).limit(limit).all()

def update_horario(db: Session, horario_id: int, horario: schemas.horarios.HorarioUpdate):
    db_horario = db.query(models.horarios.Horario).filter(models.horarios.Horario.horario_id == horario_id).first()
    if db_horario:
        for var, value in vars(horario).items():
            setattr(db_horario, var, value) if value else None
        db.commit()
        db.refresh(db_horario)
    return db_horario


def delete_horario(db: Session, horario_id: int):
    db_horario = db.query(models.horarios.Horario).filter(models.horarios.Horario.horario_id == horario_id).first()
    if db_horario:
        db.delete(db_horario)
        db.commit()
    return db_horario
