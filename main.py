from fastapi import FastAPI, APIRouter
from starlette.middleware.cors import CORSMiddleware

from config.CORS import origins, methods, headers

from config.database import engineconn
from model.model import Builder
from routers.builder_router import builder_router

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

app.include_router(builder_router)

# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc

@app.get("/")
async def first_get():
  example = session.query(Builder).all()
  return example

@app.get("/building/{item_id}")
async def root(item_id: int):
  return {
    "title": "string{item_id}",
    "src": "string",
    "desc": "string"
  }



@app.get("/office/{office_id}")
async def root(office_id: int):
  return {
    "period": "4개월 21일",
    "dPrice": "5000만원 이하",
    "rate": 4.6,
    "like": 4.7,
    "office":"하우스팩토리",
    "officeURL": "/",
    "builder":"하우스팩토리",
    "builderURL":"/"
  }
