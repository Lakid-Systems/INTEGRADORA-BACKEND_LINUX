from jwt import encode, decode
from datetime import datetime, timedelta

def solicita_token(dato: dict) -> str:
    """
    Genera un token JWT con expiración de 24 horas e incluye
    el correo y nombre del usuario en el payload.
    """
    expiracion = datetime.utcnow() + timedelta(hours=24)

    payload = {
        "message": "Token válido por 24 horas",
        "exp": expiracion,
        "correo": dato.get("Correo_Electronico"),  # extrae del schema recibido
        "usuario": dato.get("Nombre_Usuario")      # también puede venir del modelo
    }

    token = encode(payload=payload, key='mi_clave', algorithm='HS256')
    return token

def valida_token(token: str) -> dict:
    try:
        return decode(token, key='mi_clave', algorithms=['HS256'])
    except Exception as e:
        raise Exception("Token inválido o expirado") from e
