from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

# 📁 Imports locales
import schemas.departamentos as schemas
import models.departamentos as models
import crud.departamentos as crud
import config.db
from portadortoken import Portador

# 🧭 Inicializa el router con prefijo y categoría para la documentación
departamentos = APIRouter(
    prefix="/departamentos",
    tags=["Departamentos"]
)

# 🔌 Dependencia para obtener la sesión de la base de datos
def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 📘 Obtener todos los departamentos (PROTEGIDO)
@departamentos.get("/", response_model=List[schemas.Departamento], dependencies=[Depends(Portador())])
def get_departamentos(db: Session = Depends(get_db)):
    """
    Retorna todos los departamentos registrados en el sistema.
    """
    return crud.get_departamentos(db)

# 📘 Obtener un departamento por ID (PROTEGIDO)
@departamentos.get("/{id}", response_model=schemas.Departamento, dependencies=[Depends(Portador())])
def get_departamento(id: int, db: Session = Depends(get_db)):
    """
    Retorna un solo departamento por su ID.
    """
    departamento = crud.get_departamento(db, id)
    if departamento is None:
        raise HTTPException(status_code=404, detail="Departamento no encontrado")
    return departamento

# 🟢 Crear un nuevo departamento (SIN AUTENTICACIÓN)
@departamentos.post("/", response_model=schemas.Departamento)
def create_departamento(departamento: schemas.DepartamentoCreate, db: Session = Depends(get_db)):
    """
    Crea un nuevo departamento en el sistema.
    """
    return crud.create_departamento(db, departamento)

# 🟠 Actualizar un departamento existente (PROTEGIDO)
@departamentos.put("/{id}", response_model=schemas.Departamento, dependencies=[Depends(Portador())])
def update_departamento(id: int, departamento_data: schemas.DepartamentoUpdate, db: Session = Depends(get_db)):
    """
    Actualiza la información de un departamento por ID.
    """
    db_departamento = crud.update_departamento(db, id, departamento_data)
    if db_departamento is None:
        raise HTTPException(status_code=404, detail="Departamento no encontrado")
    return db_departamento

# 🔴 Eliminar un departamento por ID (PROTEGIDO)
@departamentos.delete("/{id}", response_model=dict, dependencies=[Depends(Portador())])
def delete_departamento(id: int, db: Session = Depends(get_db)):
    """
    Elimina un departamento del sistema por su ID.
    """
    db_departamento = crud.delete_departamento(db, id)
    if db_departamento is None:
        raise HTTPException(status_code=404, detail="Departamento no encontrado")
    return {"message": "Departamento eliminado correctamente"}
