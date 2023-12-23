from fastapi import APIRouter, HTTPException
from model.OfficeModel import Office
from schemas.OfficeSchema import PostOfficeSchema
from config.database import engineconn

office_router = APIRouter(
  prefix="/api/office",
  tags=["office"],
  responses={404: {"description": "Not found"}},
)

engine = engineconn()
session = engine.sessionmaker()

@office_router.post("/")
async def post_office(office:PostOfficeSchema):
  try:
    session.add(
      Office(
        officeType = office.officeType,
        officeName = office.officeName,
        communication = office.communication,
        price = office.price,
        result = office.result,
        keepingDeadline = office.keepingDeadline,
        afterService = office.afterService,
        satisfaction = office.satisfaction,
        description = office.description
      )
    )
    session.commit()
  except:
    session.rollback()

@office_router.get("/")
async def get_offices():
  response=session.query(Office).all()#filter(Office.age > 20)
  return response