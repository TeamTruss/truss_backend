from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from config.CORS import origins, methods, headers

from config.database import engineconn
from routers.office_router import office_router
from routers.person_router import person_router

app = FastAPI(
  title="Truss API",
  description="Backend server for Truss",
  version="0.0.1"
)

engine = engineconn()
session = engine.sessionmaker()

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=methods,
  allow_headers=headers,
)

app.include_router(office_router)
app.include_router(person_router)

# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc