from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from config.CORS import origins, methods, headers
from config.database import engineconn

from routers.office_router import office_router
from routers.user_router import user_router
from routers.post_router import post_router
from routers.house_router import house_router
from routers.security_router import security_router

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
app.include_router(user_router)
app.include_router(post_router)
app.include_router(house_router)
app.include_router(security_router)

# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc