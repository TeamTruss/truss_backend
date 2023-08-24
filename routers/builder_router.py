from fastapi import APIRouter, HTTPException
from model.model import Builder
from schemas.schema import BuilderSchema
from config.database import engineconn

builder_router = APIRouter(
  prefix="/api/builder",
  tags=["builder"],
  responses={404: {"description": "Not found"}},
)

engine = engineconn()
session = engine.sessionmaker()

@builder_router.post("/")
async def post_builder(builder:BuilderSchema):
  session.add(
    Builder(
      name=builder.name,
      sotong= builder.sotong,
      price=builder.price,
      sigongResult=builder.sigongResult,
      dateJunsu=builder.dateJunsu,
      AS=builder.AS,
      satisfaction=builder.satisfaction,
      description=builder.description
    )
  )
  session.commit()
  return builder

@builder_router.get("/")
async def get_builders():
  return {
    "title": "string",
    "src": "string",
    "minDate": "string",
    "maxDate": "string",
    "minPrice": "string"
  }