from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import crud.usersrols, config.db, schemas.usersrols, models.usersrols
from typing import List
from jwt_config import solicita_token
from portadortoken import Portador

key = Fernet.generate_key()
f = Fernet(key)

userrol = APIRouter()

models.usersrols.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 🔹 Listar relaciones usuario-rol (PROTEGIDO)
@userrol.get(
    "/usersrols/",
    response_model=List[schemas.usersrols.UserRol],
    tags=["Usuarios Roles"],
    dependencies=[Depends(Portador())],
    summary="Listar asignaciones de usuario a rol",
    description="""
Devuelve una lista paginada de todas las relaciones entre usuarios y roles.

- Protegido por JWT.
- Puedes usar `skip` y `limit` para paginar.
"""
)
def read_usersrols(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_usersrols = crud.usersrols.get_usersrols(db=db, skip=skip, limit=limit)
    return db_usersrols

# 🔹 Consultar una asignación específica (PROTEGIDO)
@userrol.post(
    "/userrol/{id_user}/{id_rol}",
    response_model=schemas.usersrols.UserRol,
    tags=["Usuarios Roles"],
    dependencies=[Depends(Portador())],
    summary="Consultar asignación usuario-rol",
    description="""
Devuelve la relación específica entre un usuario y un rol, usando sus IDs.

- Protegido por JWT.
- Retorna error 404 si no existe la asignación.
"""
)
def read_rol(id_user: int, id_rol: int, db: Session = Depends(get_db)):
    db_userrol = crud.usersrols.get_userrol(db=db, id_user=id_user, id_rol=id_rol)
    if db_userrol is None:
        raise HTTPException(status_code=404, detail="UserRol no existe")
    return db_userrol

# 🔹 Crear asignación usuario-rol (PROTEGIDO)
@userrol.post(
    "/userrols/",
    response_model=schemas.usersrols.UserRol,
    tags=["Usuarios Roles"],
    dependencies=[Depends(Portador())],
    summary="Asignar usuario a rol",
    description="""
Asocia un usuario existente con un rol existente.

- Protegido por JWT.
- Retorna error 400 si la asignación ya existe.
"""
)
def create_user(userrol: schemas.usersrols.UserRolCreate, db: Session = Depends(get_db)):
    db_userrol = crud.usersrols.get_userrol(db=db, id_user=userrol.Usuario_ID, id_rol=userrol.Rol_ID)
    if db_userrol:
        raise HTTPException(status_code=400, detail="Usuario existente intenta nuevamente")
    return crud.usersrols.create_userrol(db=db, userrol=userrol)

# 🔹 Actualizar asignación usuario-rol (PROTEGIDO)
@userrol.put(
    "/userrol/{id_user}/{id_rol}",
    response_model=schemas.usersrols.UserRol,
    tags=["Usuarios Roles"],
    dependencies=[Depends(Portador())],
    summary="Actualizar asignación usuario-rol",
    description="""
Modifica una relación específica entre un usuario y un rol.

- Protegido por JWT.
- Retorna error 404 si no se encuentra.
"""
)
def update_user(id_user: int, id_rol: int, userrol: schemas.usersrols.UserRolUpdate, db: Session = Depends(get_db)):
    db_userrol = crud.usersrols.update_userrol(db=db, id_user=id_user, id_rol=id_rol, userrol=userrol)
    if db_userrol is None:
        raise HTTPException(status_code=404, detail="Usuario no existe, no actualizado")
    return db_userrol

# 🔹 Eliminar asignación usuario-rol (PROTEGIDO)
@userrol.delete(
    "/userrol/{id_user}/{id_rol}",
    response_model=schemas.usersrols.UserRol,
    tags=["Usuarios Roles"],
    dependencies=[Depends(Portador())],
    summary="Eliminar asignación usuario-rol",
    description="""
Elimina la relación entre un usuario y un rol.

- Protegido por JWT.
- Retorna error 404 si la relación no existe.
"""
)
def delete_rol(id_user: int, id_rol: int, db: Session = Depends(get_db)):
    db_userrol = crud.usersrols.delete_userrol(db=db, id_user=id_user, id_rol=id_rol)
    if db_userrol is None:
        raise HTTPException(status_code=404, detail="Usuario no existe, no se pudo eliminar")
    return db_userrol
