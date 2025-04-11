from fastapi import HTTPException, Request, Depends
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from jwt_config import valida_token
import crud.users, config.db, models.users

models.users.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Portador(HTTPBearer):
    async def __call__(self, request: Request, db: Session = Depends(get_db)):
        autorizacion = await super().__call__(request)
        try:
            dato = valida_token(autorizacion.credentials)
        except Exception:
            raise HTTPException(status_code=401, detail="Token inválido o expirado")
        
        correo = dato.get("correo")
        if correo is None:
            raise HTTPException(status_code=404, detail="Correo no encontrado en el token")
        
        db_userlogin = crud.users.get_user_by_email(db, correo)
        if db_userlogin is None:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
        return db_userlogin
