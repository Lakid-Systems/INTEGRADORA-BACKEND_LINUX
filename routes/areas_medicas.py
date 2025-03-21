from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import List
import crud.areas_medicas, config.db, schemas.areas_medicas, models.areas_medicas
from jwt_config import solicita_token
from portadortoken import Portador

area_medica = APIRouter()

models.areas_medicas.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ Obtener todas las áreas médicas
@area_medica.get("/areas_medicas/", response_model=List[schemas.areas_medicas.AreaMedica], tags=["Áreas Médicas"], dependencies=[Depends(Portador())])
def read_areas_medicas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.areas_medicas.get_areas_medicas(db=db, skip=skip, limit=limit)

# ✅ Obtener un área médica por ID 
@area_medica.get("/area_medica/{id}", response_model=schemas.areas_medicas.AreaMedica, tags=["Áreas Médicas"], dependencies=[Depends(Portador())])
def read_area_medica(id: str, db: Session = Depends(get_db)):
    db_area = crud.areas_medicas.get_area_medica(db=db, id=id)
    if db_area is None:
        raise HTTPException(status_code=404, detail="Área médica no encontrada")
    return db_area

# ✅ Crear una nueva área médica
@area_medica.post("/areas_medicas/", response_model=schemas.areas_medicas.AreaMedica, tags=["Áreas Médicas"])
def create_area_medica(area: schemas.areas_medicas.AreaMedicaCreate, db: Session = Depends(get_db)):
    db_area = crud.areas_medicas.get_area_medica_by_nombre(db, nombre=area.Nombre)
    if db_area:
        raise HTTPException(status_code=400, detail="El nombre del área médica ya existe")
    return crud.areas_medicas.create_area_medica(db=db, area=area)

# ✅ Actualizar un área médica (Corrigido `id: int` → `id: str`)
@area_medica.put("/area_medica/{id}", response_model=schemas.areas_medicas.AreaMedica, tags=["Áreas Médicas"], dependencies=[Depends(Portador())])
def update_area_medica(id: str, area: schemas.areas_medicas.AreaMedicaUpdate, db: Session = Depends(get_db)):
    db_area = crud.areas_medicas.update_area_medica(db=db, id=id, area=area)
    if db_area is None:
        raise HTTPException(status_code=404, detail="Área médica no encontrada, no se pudo actualizar")
    return db_area

# ✅ Eliminar un área médica (Corrigido `id: int` → `id: str`)
@area_medica.delete("/area_medica/{id}", response_model=schemas.areas_medicas.AreaMedica, tags=["Áreas Médicas"], dependencies=[Depends(Portador())])
def delete_area_medica(id: str, db: Session = Depends(get_db)):
    db_area = crud.areas_medicas.delete_area_medica(db=db, id=id)
    if db_area is None:
        raise HTTPException(status_code=404, detail="Área médica no encontrada, no se pudo eliminar")
    return {"message": "Area eliminado correctamente"}
