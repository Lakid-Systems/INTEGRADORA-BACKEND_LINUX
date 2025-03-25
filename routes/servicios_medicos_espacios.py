# pylint: disable=too-many-arguments, redefined-builtin
"""Rutas de FastAPI para la asignación de espacios a servicios médicos."""

from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from portadortoken import Portador
import crud.servicios_medicos_espacios as crud
import schemas.servicios_medicos_espacios as schemas
import config.db

router = APIRouter()

def get_db():
    """
    Dependencia para obtener una sesión de base de datos.
    """
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get(
    "/servicios_espacios/",
    response_model=List[schemas.ServiciosMedicosEspacios],
    tags=["Servicios Médicos Espacios"],
    dependencies=[Depends(Portador())]
)
def read_servicios_espacios(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    """
    Lista todas las relaciones entre servicios médicos y espacios (paginado).
    """
    return crud.get_servicios_espacios(db, skip, limit)


@router.get(
    "/servicios_espacios/{id}",
    response_model=schemas.ServiciosMedicosEspacios,
    tags=["Servicios Médicos Espacios"],
    dependencies=[Depends(Portador())]
)
def read_servicio_espacio(id: int, db: Session = Depends(get_db)):
    """
    Obtiene una relación específica entre servicio y espacio por su ID.
    """
    servicio_espacio = crud.get_servicio_espacio(db, id)
    if not servicio_espacio:
        raise HTTPException(status_code=404, detail="ServicioEspacio no encontrado")
    return servicio_espacio


@router.post(
    "/servicios_espacios/",
    response_model=schemas.ServiciosMedicosEspacios,
    tags=["Servicios Médicos Espacios"]
)
def create_servicio_espacio(
    servicio_espacio_data: schemas.ServiciosMedicosEspaciosCreate,
    db: Session = Depends(get_db)
):
    """
    Crea una nueva relación entre un servicio médico y un espacio.
    """
    return crud.create_servicio_espacio(db, servicio_espacio_data)


@router.put(
    "/servicios_espacios/{id}",
    response_model=schemas.ServiciosMedicosEspacios,
    tags=["Servicios Médicos Espacios"],
    dependencies=[Depends(Portador())]
)
def update_servicio_espacio(
    id: int,
    servicio_espacio_data: schemas.ServiciosMedicosEspaciosUpdate,
    db: Session = Depends(get_db)
):
    """
    Actualiza una relación entre servicio médico y espacio existente.
    """
    servicio_espacio = crud.update_servicio_espacio(db, id, servicio_espacio_data)
    if not servicio_espacio:
        raise HTTPException(status_code=404, detail="ServicioEspacio no encontrado")
    return servicio_espacio


@router.delete(
    "/servicios_espacios/{id}",
    response_model=dict,
    tags=["Servicios Médicos Espacios"],
    dependencies=[Depends(Portador())]
)
def delete_servicio_espacio(id: int, db: Session = Depends(get_db)):
    """
    Elimina una relación entre servicio médico y espacio por ID.
    """
    servicio_espacio = crud.delete_servicio_espacio(db, id)
    if not servicio_espacio:
        raise HTTPException(status_code=404, detail="ServicioEspacio no encontrado")
    return {"message": "ServicioEspacio eliminado correctamente"}
