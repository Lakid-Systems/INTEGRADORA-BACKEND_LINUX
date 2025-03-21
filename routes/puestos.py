from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import List
import crud.puestos, config.db, schemas.puestos, models.puestos
from jwt_config import solicita_token
from portadortoken import Portador

puesto = APIRouter()

models.puestos.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@puesto.get("/puestos/", response_model=List[schemas.puestos.Puesto], tags=["Puestos"], dependencies=[Depends(Portador())])
def read_puestos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_puestos = crud.puestos.get_puestos(db=db, skip=skip, limit=limit)
    return db_puestos

@puesto.get("/puesto/{id}", response_model=schemas.puestos.Puesto, tags=["Puestos"], dependencies=[Depends(Portador())])
def read_puesto(id: int, db: Session = Depends(get_db)):
    db_puesto = crud.puestos.get_puesto(db=db, id=id)
    if db_puesto is None:
        raise HTTPException(status_code=404, detail="Puesto no encontrado")
    return db_puesto

@puesto.post("/puestos/", response_model=schemas.puestos.Puesto, tags=["Puestos"])
def create_puesto(puesto: schemas.puestos.PuestoCreate, db: Session = Depends(get_db)):
    db_puesto = crud.puestos.get_puesto_by_nombre(db, nombre=puesto.Nombre)
    if db_puesto:
        raise HTTPException(status_code=400, detail="El nombre del puesto ya existe")
    return crud.puestos.create_puesto(db=db, puesto=puesto)

@puesto.put("/puesto/{id}", response_model=schemas.puestos.Puesto, tags=["Puestos"], dependencies=[Depends(Portador())])
def update_puesto(id: int, puesto: schemas.puestos.PuestoUpdate, db: Session = Depends(get_db)):
    db_puesto = crud.puestos.update_puesto(db=db, id=id, puesto=puesto)
    if db_puesto is None:
        raise HTTPException(status_code=404, detail="Puesto no encontrado, no se pudo actualizar")
    return db_puesto

@puesto.delete("/puesto/{id}", response_model=schemas.puestos.Puesto, tags=["Puestos"], dependencies=[Depends(Portador())])
def delete_puesto(id: int, db: Session = Depends(get_db)):
    db_puesto = crud.puestos.delete_puesto(db=db, id=id)
    if db_puesto is None:
        raise HTTPException(status_code=404, detail="Puesto no encontrado, no se pudo eliminar")
    return db_puesto
