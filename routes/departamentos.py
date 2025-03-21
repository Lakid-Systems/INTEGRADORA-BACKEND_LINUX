from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import schemas.departamentos as schemas
import models.departamentos as models
import crud.departamentos as crud
import config.db
from portadortoken import Portador

departamentos = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 🔹 Obtener todos los departamentos (PROTEGIDO)
@departamentos.get("/departamentos/", response_model=List[schemas.Departamento], dependencies=[Depends(Portador())])
def get_departamentos(db: Session = Depends(get_db)):
    return crud.get_departamentos(db)

# 🔹 Obtener un departamento por ID (PROTEGIDO)
@departamentos.get("/departamentos/{id}", response_model=schemas.Departamento, dependencies=[Depends(Portador())])
def get_departamento(id: int, db: Session = Depends(get_db)):
    departamento = crud.get_departamento(db, id)
    if departamento is None:
        raise HTTPException(status_code=404, detail="Departamento no encontrado")
    return departamento

# 🔹 Crear un nuevo departamento (LIBRE, SIN AUTENTICACIÓN)
@departamentos.post("/departamentos/", response_model=schemas.Departamento)
def create_departamento(departamento: schemas.DepartamentoCreate, db: Session = Depends(get_db)):
    return crud.create_departamento(db, departamento)

# 🔹 Actualizar un departamento por ID (PROTEGIDO)
@departamentos.put("/departamentos/{id}", response_model=schemas.Departamento, dependencies=[Depends(Portador())])
def update_departamento(id: int, departamento_data: schemas.DepartamentoUpdate, db: Session = Depends(get_db)):
    db_departamento = crud.update_departamento(db, id, departamento_data)
    if db_departamento is None:
        raise HTTPException(status_code=404, detail="Departamento no encontrado")
    return db_departamento

# 🔹 Eliminar un departamento por ID (PROTEGIDO)
@departamentos.delete("/departamentos/{id}", response_model=dict, dependencies=[Depends(Portador())])
def delete_departamento(id: int, db: Session = Depends(get_db)):
    db_departamento = crud.delete_departamento(db, id)
    if db_departamento is None:
        raise HTTPException(status_code=404, detail="Departamento no encontrado")
    return {"message": "Departamento eliminado correctamente"}
