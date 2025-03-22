import models.usersrols
import schemas.usersrols
from sqlalchemy.orm import Session
import models, schemas

# 🔹 Obtener una relación usuario-rol específica
def get_userrol(db: Session, id_user: int, id_rol: int):
    """
    Retorna una relación usuario-rol específica por ID de usuario y rol.
    """
    return db.query(models.usersrols.UserRol).filter(
        models.usersrols.UserRol.Usuario_ID == id_user,
        models.usersrols.UserRol.Rol_ID == id_rol
    ).first()

# 🔹 Obtener todas las relaciones usuario-rol (con paginación)
def get_usersrols(db: Session, skip: int = 0, limit: int = 10):
    """
    Retorna una lista de relaciones usuario-rol con paginación.
    """
    return db.query(models.usersrols.UserRol).offset(skip).limit(limit).all()

# 🔹 Crear una nueva relación usuario-rol
def create_userrol(db: Session, userrol: schemas.usersrols.UserRolCreate):
    """
    Crea una nueva asignación de un rol a un usuario.
    """
    db_userrol = models.usersrols.UserRol(
        Usuario_ID=userrol.Usuario_ID,
        Rol_ID=userrol.Rol_ID,
        Estatus=userrol.Estatus,
        Fecha_Registro=userrol.Fecha_Registro,
        Fecha_Actualizacion=userrol.Fecha_Actualizacion
    )
    db.add(db_userrol)
    db.commit()
    db.refresh(db_userrol)
    return db_userrol

# 🔹 Actualizar una relación usuario-rol existente
def update_userrol(db: Session, id_user: int, id_rol: int, userrol: schemas.usersrols.UserRolUpdate):
    """
    Actualiza los campos de una relación usuario-rol específica.
    """
    db_userrol = db.query(models.usersrols.UserRol).filter(
        models.usersrols.UserRol.Usuario_ID == id_user,
        models.usersrols.UserRol.Rol_ID == id_rol
    ).first()
    if db_userrol:
        for var, value in vars(userrol).items():
            setattr(db_userrol, var, value) if value else None
        db.commit()
        db.refresh(db_userrol)
    return db_userrol

# 🔹 Eliminar una relación usuario-rol
def delete_userrol(db: Session, id_user: int, id_rol: int):
    """
    Elimina una relación entre un usuario y un rol, si existe.
    """
    db_userrol = db.query(models.usersrols.UserRol).filter(
        models.usersrols.UserRol.Usuario_ID == id_user,
        models.usersrols.UserRol.Rol_ID == id_rol
    ).first()
    if db_userrol:
        db.delete(db_userrol)
        db.commit()
    return db_userrol
