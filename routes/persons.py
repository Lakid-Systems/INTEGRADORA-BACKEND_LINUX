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
@persons_router.get(
    "/persons/",
    response_model=List[schemas.persons.Person],
    tags=["Personas"],
    dependencies=[Depends(Portador())],
    summary="Listar personas registradas",
    description="""
Devuelve una lista paginada de todas las personas registradas en el sistema.

- Se requiere autenticación con token JWT.
- Permite controlar la cantidad de resultados con `skip` y `limit`.
"""
)
def read_persons(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_persons = crud.persons.get_persons(db=db, skip=skip, limit=limit)
    return db_persons

@persons_router.get(
    "/person/{id}",
    response_model=schemas.persons.Person,
    tags=["Personas"],
    dependencies=[Depends(Portador())],
    summary="Consultar persona por ID",
    description="""
Devuelve la información de una persona específica según su ID.

- Retorna 404 si no existe la persona.
- Protegido por JWT.
"""
)
def read_person(id: int, db: Session = Depends(get_db)):
    db_person = crud.persons.get_person(db=db, id=id)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    return db_person

@persons_router.put(
    "/person/{id}",
    response_model=schemas.persons.Person,
    tags=["Personas"],
    dependencies=[Depends(Portador())],
    summary="Actualizar persona",
    description="""
Actualiza la información de una persona registrada.

- Solo usuarios autenticados pueden actualizar.
- Retorna 404 si la persona no existe.
"""
)
def update_person(id: int, person: schemas.persons.PersonUpdate, db: Session = Depends(get_db)):
    db_person = crud.persons.update_person(db=db, id=id, person=person)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Persona no existe, no actualizada")
    return db_person

@persons_router.delete(
    "/person/{id}",
    response_model=schemas.persons.Person,
    tags=["Personas"],
    dependencies=[Depends(Portador())],
    summary="Eliminar persona",
    description="""
Elimina a una persona registrada por ID.

- Se requiere autenticación con JWT.
- Retorna 404 si no se encuentra la persona.
"""
)
def delete_person(id: int, db: Session = Depends(get_db)):
    db_person = crud.persons.delete_person(db=db, id=id)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Persona no existe, no se pudo eliminar")
    return db_person

# 🔹✅ Ruta NO protegida para registrar una persona (cualquiera puede crear una persona)
@persons_router.post(
    "/person/",
    response_model=schemas.persons.Person,
    tags=["Personas"],
    summary="Crear persona",
    description="""
Registra una nueva persona en el sistema.

- Verifica si ya existe una persona con el mismo nombre.
- Retorna error 400 si ya existe.
- No requiere token de autenticación.
"""
)
def create_person(person: schemas.persons.PersonCreate, db: Session = Depends(get_db)):
    db_person = crud.persons.get_person_by_nombre(db, person=person.Nombre)
    if db_person:
        raise HTTPException(status_code=400, detail="Usuario existente intenta nuevamente")
    return crud.persons.create_person(db=db, person=person)
