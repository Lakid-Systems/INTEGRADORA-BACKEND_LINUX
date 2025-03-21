from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.horarios, config.db, schemas.horarios, models.horarios
from typing import List


horarios = APIRouter()

models.horarios.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@horarios.get("/horarios/", response_model=List[schemas.horarios.Horario], tags=["Horarios"])
def read_horarios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_horarios = crud.horarios.get_horarios(db=db, skip=skip, limit=limit)
    return db_horarios

@horarios.get("/horario/{horario_id}", response_model=schemas.horarios.Horario, tags=["Horarios"])
def read_horario(horario_id: int, db: Session = Depends(get_db)):
    db_horario = crud.horarios.get_horario(db=db, horario_id=horario_id)
    if db_horario is None:
        raise HTTPException(status_code=404, detail="Horario no encontrado")
    return db_horario

@horarios.post("/horario/", response_model=schemas.horarios.Horario, tags=["Horarios"])
def create_horario(horario: schemas.horarios.HorarioCreate, db: Session = Depends(get_db)):
    return crud.horarios.create_horario(db=db, horario=horario)

@horarios.put("/horario/{horario_id}", response_model=schemas.horarios.Horario, tags=["Horarios"])
def update_horario(horario_id: int, horario: schemas.horarios.HorarioUpdate, db: Session = Depends(get_db)):
    db_horario = crud.horarios.update_horario(db=db, horario_id=horario_id, horario=horario)
    if db_horario is None:
        raise HTTPException(status_code=404, detail="Horario no encontrado, no actualizado")
    return db_horario

@horarios.delete("/horario/{horario_id}", response_model=schemas.horarios.Horario, tags=["Horarios"])
def delete_horario(horario_id: int, db: Session = Depends(get_db)):
    db_horario = crud.horarios.delete_horario(db=db, horario_id=horario_id)
    if db_horario is None:
        raise HTTPException(status_code=404, detail="Horario no encontrado, no se pudo eliminar")
    return db_horario
