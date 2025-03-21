from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.servicios_medicos, config.db, schemas.servicios_medicos, models.servicios_medicos
from typing import List
from portadortoken import Portador  

serviceM = APIRouter()

models.servicios_medicos.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 🔒 Rutas protegidas con JWT
@serviceM.get("/servicios_medicos/", response_model=List[schemas.servicios_medicos.Service], tags=["Servicios Médicos"], dependencies=[Depends(Portador())])
def read_servicesM(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return crud.servicios_medicos.get_servicesM(db=db, skip=skip, limit=limit)

@serviceM.get("/servicios_medicos/{id}", response_model=schemas.servicios_medicos.Service, tags=["Servicios Médicos"], dependencies=[Depends(Portador())])
def read_serviceM(id: int, db: Session = Depends(get_db)):
    db_serviceM = crud.servicios_medicos.get_serviceM(db=db, id=id)
    if db_serviceM is None:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return db_serviceM

@serviceM.post("/servicios_medicos/", response_model=schemas.servicios_medicos.Service, tags=["Servicios Médicos"], dependencies=[Depends(Portador())])
def create_serviceM(service: schemas.servicios_medicos.ServiceMCreate, db: Session = Depends(get_db)):
    db_serviceM = crud.servicios_medicos.get_serviceM_by_nombre(db, nombre=service.nombre)
    if db_serviceM:
        raise HTTPException(status_code=400, detail="Servicio existente, intenta nuevamente")
    return crud.servicios_medicos.create_serviceM(db=db, service=service)

@serviceM.put("/servicios_medicos/{id}", response_model=schemas.servicios_medicos.Service, tags=["Servicios Médicos"], dependencies=[Depends(Portador())])
def update_serviceM(id: int, service: schemas.servicios_medicos.ServiceMUpdate, db: Session = Depends(get_db)):
    db_serviceM = crud.servicios_medicos.update_serviceM(db=db, id=id, service=service)
    if db_serviceM is None:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return db_serviceM

@serviceM.delete("/servicios_medicos/{id}", response_model=schemas.servicios_medicos.Service, tags=["Servicios Médicos"], dependencies=[Depends(Portador())])
def delete_serviceM(id: int, db: Session = Depends(get_db)):
    db_serviceM = crud.servicios_medicos.delete_serviceM(db=db, id=id)
    if db_serviceM is None:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return db_serviceM
