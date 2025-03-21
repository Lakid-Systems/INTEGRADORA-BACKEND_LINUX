from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from portadortoken import Portador
import crud.servicios_medicos_espacios as crud
import schemas.servicios_medicos_espacios as schemas
import config.db

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 🔹 Obtener todos los servicios médicos en espacios (PROTEGIDO)
@router.get("/servicios_espacios/", response_model=List[schemas.ServiciosMedicosEspacios], tags=["Servicios Médicos Espacios"], dependencies=[Depends(Portador())])
def read_servicios_espacios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_servicios_espacios(db, skip, limit)

# 🔹 Obtener un servicio médico en un espacio por ID (PROTEGIDO)
@router.get("/servicios_espacios/{id}", response_model=schemas.ServiciosMedicosEspacios, tags=["Servicios Médicos Espacios"], dependencies=[Depends(Portador())])
def read_servicio_espacio(id: int, db: Session = Depends(get_db)):
    servicio_espacio = crud.get_servicio_espacio(db, id)
    if not servicio_espacio:
        raise HTTPException(status_code=404, detail="ServicioEspacio no encontrado")
    return servicio_espacio

# 🔹 Crear una nueva relación entre servicio médico y espacio (LIBRE)
@router.post("/servicios_espacios/", response_model=schemas.ServiciosMedicosEspacios, tags=["Servicios Médicos Espacios"])
def create_servicio_espacio(servicio_espacio_data: schemas.ServiciosMedicosEspaciosCreate, db: Session = Depends(get_db)):
    return crud.create_servicio_espacio(db, servicio_espacio_data)

# 🔹 Actualizar una relación entre servicio médico y espacio (PROTEGIDO)
@router.put("/servicios_espacios/{id}", response_model=schemas.ServiciosMedicosEspacios, tags=["Servicios Médicos Espacios"], dependencies=[Depends(Portador())])
def update_servicio_espacio(id: int, servicio_espacio_data: schemas.ServiciosMedicosEspaciosUpdate, db: Session = Depends(get_db)):
    servicio_espacio = crud.update_servicio_espacio(db, id, servicio_espacio_data)
    if not servicio_espacio:
        raise HTTPException(status_code=404, detail="ServicioEspacio no encontrado")
    return servicio_espacio

# 🔹 Eliminar una relación entre servicio médico y espacio (PROTEGIDO)
@router.delete("/servicios_espacios/{id}", response_model=dict, tags=["Servicios Médicos Espacios"], dependencies=[Depends(Portador())])
def delete_servicio_espacio(id: int, db: Session = Depends(get_db)):
    servicio_espacio = crud.delete_servicio_espacio(db, id)
    if not servicio_espacio:
        raise HTTPException(status_code=404, detail="ServicioEspacio no encontrado")
    return {"message": "ServicioEspacio eliminado correctamente"}
