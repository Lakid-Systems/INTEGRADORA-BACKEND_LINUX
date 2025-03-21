from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.persons, config.db, schemas.persons, models.persons
from typing import List
from portadortoken import Portador  # ✅ Se usa para proteger rutas

persons_router = APIRouter()  # ✅ Renombrado para evitar conflictos con otros routers

models.persons.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 🔹🚀 Rutas protegidas con JWT (Solo accesibles con token)
@persons_router.get("/persons/", response_model=List[schemas.persons.Person], tags=["Personas"], dependencies=[Depends(Portador())])
def read_persons(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_persons = crud.persons.get_persons(db=db, skip=skip, limit=limit)
    return db_persons

@persons_router.get("/person/{id}", response_model=schemas.persons.Person, tags=["Personas"], dependencies=[Depends(Portador())])
def read_person(id: int, db: Session = Depends(get_db)):
    db_person = crud.persons.get_person(db=db, id=id)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    return db_person

@persons_router.put("/person/{id}", response_model=schemas.persons.Person, tags=["Personas"], dependencies=[Depends(Portador())])
def update_person(id: int, person: schemas.persons.PersonUpdate, db: Session = Depends(get_db)):
    db_person = crud.persons.update_person(db=db, id=id, person=person)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Persona no existe, no actualizada")
    return db_person

@persons_router.delete("/person/{id}", response_model=schemas.persons.Person, tags=["Personas"], dependencies=[Depends(Portador())])
def delete_person(id: int, db: Session = Depends(get_db)):
    db_person = crud.persons.delete_person(db=db, id=id)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Persona no existe, no se pudo eliminar")
    return db_person

# 🔹✅ Ruta NO protegida para registrar una persona (cualquiera puede crear una persona)
@persons_router.post("/person/", response_model=schemas.persons.Person, tags=["Personas"])
def create_person(person: schemas.persons.PersonCreate, db: Session = Depends(get_db)):
    db_person = crud.persons.get_person_by_nombre(db, person=person.Nombre)
    if db_person:
        raise HTTPException(status_code=400, detail="Usuario existente intenta nuevamente")
    return crud.persons.create_person(db=db, person=person)
