import models.areas_medicas
import schemas.areas_medicas
from sqlalchemy.orm import Session

# ✅ Obtener un área médica por ID (Ahora usa `id: str` porque es un UUID)
def get_area_medica(db: Session, id: str):
    return db.query(models.areas_medicas.AreaMedica).filter(models.areas_medicas.AreaMedica.ID == id).first()

# ✅ Obtener un área médica por Nombre
def get_area_medica_by_nombre(db: Session, nombre: str):
    return db.query(models.areas_medicas.AreaMedica).filter(models.areas_medicas.AreaMedica.Nombre == nombre).first()

# ✅ Obtener todas las áreas médicas con paginación
def get_areas_medicas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.areas_medicas.AreaMedica).offset(skip).limit(limit).all()

# ✅ Crear un área médica (Se eliminó `Fecha_Registro` y `Fecha_Actualizacion`)
def create_area_medica(db: Session, area: schemas.areas_medicas.AreaMedicaCreate):
    db_area = models.areas_medicas.AreaMedica(
        Nombre=area.Nombre,
        Descripcion=area.Descripcion,
        Estatus=area.Estatus  
    )
    db.add(db_area)
    db.commit()
    db.refresh(db_area)
    return db_area

# ✅ Actualizar un área médica (Ahora usa `id: str` y evita sobrescribir con `None`)
def update_area_medica(db: Session, id: str, area: schemas.areas_medicas.AreaMedicaUpdate):
    db_area = db.query(models.areas_medicas.AreaMedica).filter(models.areas_medicas.AreaMedica.ID == id).first()
    if db_area:
        for key, value in area.dict(exclude_unset=True).items():
            setattr(db_area, key, value)
        db.commit()
        db.refresh(db_area)
    return db_area

# ✅ Eliminar un área médica (Ahora usa `id: str`)
def delete_area_medica(db: Session, id: str):
    db_area = db.query(models.areas_medicas.AreaMedica).filter(models.areas_medicas.AreaMedica.ID == id).first()
    if db_area:
        db.delete(db_area)
        db.commit()
    return db_area
