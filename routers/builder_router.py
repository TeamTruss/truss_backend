from fastapi import APIRouter, HTTPException
from dto.dto import Builder
from schemas.schema import BuilderSchema
from config.database import engineconn

builder_router = APIRouter(
  prefix="/builder",
  tags=["builder"],
  responses={404: {"description": "Not found"}},
)

engine = engineconn()
session = engine.sessionmaker()

@builder_router.post("/")
async def post_builder(builder:BuilderSchema):
  addMemo = Builder(name=builder.name, url=builder.url)
  session.add(addMemo)
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

@builder_router.get("/{builder_id}")
async def get_builder(builder_id: int):
  # if builder_id:
  #   raise HTTPException(status_code=404, detail="Item not found")
  return {
    "title": "string",
    "src": "string",
    "minDate": "string",
    "maxDate": "string",
    "minPrice": "string"
  }