import models.persons
import schemas.persons
from sqlalchemy.orm import Session
import models, schemas

# 🔹 Obtener una persona por su ID
def get_person(db: Session, id: int):
    """
    Retorna una persona por su ID.
    """
    return db.query(models.persons.Person).filter(models.persons.Person.ID == id).first()

# 🔹 Obtener una persona por su nombre (exacto)
def get_person_by_nombre(db: Session, person: str):
    """
    Retorna la primera persona que coincida exactamente con el nombre.
    """
    return db.query(models.persons.Person).filter(models.persons.Person.Nombre == person).first()

# 🔹 Obtener todas las personas con paginación
def get_persons(db: Session, skip: int = 0, limit: int = 10):
    """
    Retorna una lista paginada de personas registradas.
    """
    return db.query(models.persons.Person).offset(skip).limit(limit).all()

# 🔹 Crear una nueva persona
def create_person(db: Session, person: schemas.persons.PersonCreate):
    """
    Crea y guarda una nueva persona en la base de datos.
    """
    db_person = models.persons.Person(
        Titulo_Cortesia=person.Titulo_Cortesia,
        Nombre=person.Nombre,
        Primer_Apellido=person.Primer_Apellido,
        Segundo_Apellido=person.Segundo_Apellido,
        CURP=person.CURP,
        Correo_Electronico=person.Correo_Electronico,
        Telefono=person.Telefono,
        Fecha_Nacimiento=person.Fecha_Nacimiento,
        Fotografia=person.Fotografia,
        Genero=person.Genero,
        Tipo_Sangre=person.Tipo_Sangre,
        Estatus=person.Estatus,
        Fecha_Registro=person.Fecha_Registro,
        Fecha_Actualizacion=person.Fecha_Actualizacion
    )
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person

# 🔹 Actualizar una persona existente
def update_person(db: Session, id: int, person: schemas.persons.PersonUpdate):
    """
    Actualiza los datos de una persona. Solo los campos proporcionados serán modificados.
    """
    db_person = db.query(models.persons.Person).filter(models.persons.Person.ID == id).first()
    if db_person:
        for var, value in vars(person).items():
            setattr(db_person, var, value) if value else None
        db.commit()
        db.refresh(db_person)
    return db_person

# 🔹 Eliminar una persona por ID
def delete_person(db: Session, id: int):
    """
    Elimina una persona de la base de datos según su ID.
    """
    db_person = db.query(models.persons.Person).filter(models.persons.Person.ID == id).first()
    if db_person:
        db.delete(db_person)
        db.commit()
    return db_person
