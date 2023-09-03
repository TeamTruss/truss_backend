from fastapi import APIRouter, HTTPException
from model.model import Office
from schemas.schema import OfficeSchema
from config.database import engineconn

office_router = APIRouter(
  prefix="/api/office",
  tags=["office"],
  responses={404: {"description": "Not found"}},
)

engine = engineconn()
session = engine.sessionmaker()

@office_router.post("/")
async def post_office(office:OfficeSchema):
  session.add(
    Office(
      officeType=office.officeType,
      officeName=office.officeName,
      communication=office.communication,
      price=office.price,
      sigongResult=office.result,
      keepingDeadline=office.keepingDeadline,
      afterService=office.afterService,
      satisfaction=office.satisfaction,
      description=office.description
    )
  )
  session.commit()
  return office

@office_router.get("/")
async def get_offices():
  return {
    "title": "string",
    "src": "string",
    "minDate": "string",
    "maxDate": "string",
    "minPrice": "string"
  }