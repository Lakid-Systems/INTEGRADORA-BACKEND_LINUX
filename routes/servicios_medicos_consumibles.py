from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import crud.servicios_medicos_consumibles, config.db, schemas.servicios_medicos_consumibles, models.servicios_medicos_consumibles
from portadortoken import Portador  

servicios_medicos_consumibles = APIRouter()  # 🔹 Cambio de variable para mantener coherencia con el modelo

models.servicios_medicos_consumibles.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@servicios_medicos_consumibles.get("/servicios-medicos-consumibles/", response_model=List[schemas.servicios_medicos_consumibles.ServiciosMedicosConsumibles], tags=["Servicios Médicos Consumibles"], dependencies=[Depends(Portador())])
def read_servicios_medicos_consumibles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.servicios_medicos_consumibles.get_all(db=db, skip=skip, limit=limit)

@servicios_medicos_consumibles.get("/servicio-medico-consumible/{id}", response_model=schemas.servicios_medicos_consumibles.ServiciosMedicosConsumibles, tags=["Servicios Médicos Consumibles"], dependencies=[Depends(Portador())])
def read_servicio_medico_consumible(id: int, db: Session = Depends(get_db)):
    record = crud.servicios_medicos_consumibles.get_by_id(db=db, id=id)
    if record is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return record

@servicios_medicos_consumibles.post("/servicio-medico-consumible/", response_model=schemas.servicios_medicos_consumibles.ServiciosMedicosConsumibles, tags=["Servicios Médicos Consumibles"])
def create_servicio_medico_consumible(data: schemas.servicios_medicos_consumibles.ServiciosMedicosConsumiblesCreate, db: Session = Depends(get_db)):
    return crud.servicios_medicos_consumibles.create(db=db, data=data)

@servicios_medicos_consumibles.put("/servicio-medico-consumible/{id}", response_model=schemas.servicios_medicos_consumibles.ServiciosMedicosConsumibles, tags=["Servicios Médicos Consumibles"], dependencies=[Depends(Portador())])
def update_servicio_medico_consumible(id: int, data: schemas.servicios_medicos_consumibles.ServiciosMedicosConsumiblesUpdate, db: Session = Depends(get_db)):
    updated_record = crud.servicios_medicos_consumibles.update(db=db, id=id, data=data)
    if updated_record is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return updated_record

@servicios_medicos_consumibles.delete("/servicio-medico-consumible/{id}", response_model=schemas.servicios_medicos_consumibles.ServiciosMedicosConsumibles, tags=["Servicios Médicos Consumibles"], dependencies=[Depends(Portador())])
def delete_servicio_medico_consumible(id: int, db: Session = Depends(get_db)):
    deleted_record = crud.servicios_medicos_consumibles.delete(db=db, id=id)
    if deleted_record is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return deleted_record
