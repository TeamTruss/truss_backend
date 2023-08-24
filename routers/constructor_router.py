from fastapi import APIRouter, HTTPException
from model.model import Constructor
from schemas.schema import ConstructorSchema
from config.database import engineconn

constructor_router = APIRouter(
  prefix="/api/constructor",
  tags=["constructor"],
  responses={404: {"description": "Not found"}},
)

engine = engineconn()
session = engine.sessionmaker()

@constructor_router.post("/")
async def post_constructor(constructor:ConstructorSchema):
  session.add(
    constructor(
      name=constructor.name,
      sotong= constructor.sotong,
      price=constructor.price,
      sigongResult=constructor.sigongResult,
      dateJunsu=constructor.dateJunsu,
      afterService=constructor.afterService,
      satisfaction=constructor.satisfaction,
      description=constructor.description
    )
  )
  session.commit()
  return constructor

@constructor_router.get("/")
async def get_constructors():
  return {
    "title": "string",
    "src": "string",
    "minDate": "string",
    "maxDate": "string",
    "minPrice": "string"
  }