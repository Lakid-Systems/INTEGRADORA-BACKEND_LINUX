from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 🔹 Importar configuración de la BD
from config.db import Base, engine
import models  # 🔹 Importa todos los modelos desde __init__.py

# 🔹 INICIALIZAR FASTAPI
app = FastAPI(
    title="HOSPITAL S.A. de C.V.",
    description="API para el almacenamiento de información de un hospital"
)

# 🔹 Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["http://localhost:8080"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔹 IMPORTAR TODAS LAS RUTAS
from routes.users import users_router
from routes.persons import persons_router
from routes.rol import rol
from routes.userrol import userrol
from routes.receta import receta
from routes.citas import cita
from routes.expediente import expediente
from routes.cirugia import cirugia_router
from routes.horarios import horarios
from routes.espacios import espacio
from routes.areas_medicas import area_medica
from routes.bitacora import bitacora
from routes.consumibles import consumible
from routes.departamentos import departamentos
from routes.dispensaciones import dispensacion
from routes.estudios import estudios
from routes.resultados_estudios import resultados_estudios
from routes.lotes import lote
from routes.medicamentos import medicamento
from routes.personal_medico import personal_medico
from routes.puestos import puesto
from routes.puestos_departamentos import puesto_departamento
from routes.solicitudes import request
from routes.tbb_aprobaciones import tbb_aprobaciones
from routes.tbc_organos import tbc_organos
from routes.servicios_medicos import serviceM
from routes.servicios_medicos_espacios import router as servicios_espacios_router
from routes.servicios_medicos_consumibles import servicios_medicos_consumibles  # 🔹 Cambio de nombre para mantener consistencia

# 🔹 INCLUIR LAS RUTAS
app.include_router(users_router)
app.include_router(persons_router)
app.include_router(serviceM)
app.include_router(servicios_espacios_router)
app.include_router(rol)
app.include_router(userrol)
app.include_router(receta)
app.include_router(cita)
app.include_router(expediente)
app.include_router(cirugia_router)
app.include_router(horarios)
app.include_router(espacio)
app.include_router(area_medica)
app.include_router(bitacora)
app.include_router(consumible)
app.include_router(departamentos)
app.include_router(dispensacion)
app.include_router(estudios)
app.include_router(resultados_estudios)
app.include_router(lote)
app.include_router(medicamento)
app.include_router(personal_medico)
app.include_router(puesto)
app.include_router(puesto_departamento)
app.include_router(request)
app.include_router(tbb_aprobaciones)
app.include_router(tbc_organos)
app.include_router(servicios_medicos_consumibles)

# 🔹 CREAR LAS TABLAS **DESPUÉS DE REGISTRAR LAS RUTAS**
print("🔄 Creando las tablas en MySQL si no existen...")
Base.metadata.create_all(bind=engine)
print("✅ Tablas creadas exitosamente en MySQL")
