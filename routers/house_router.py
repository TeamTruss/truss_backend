from fastapi import APIRouter, HTTPException
from model.model import House
from schemas.schema import HouseSchema
from config.database import engineconn

house_router = APIRouter(
  prefix="/api/house",
  tags=["house"],
  responses={404: {"description": "Not found"}},
)

engine = engineconn()
session = engine.sessionmaker()

@house_router.post("/")
async def post_house(house:HouseSchema):
  
  session.add(
    House(
      title = house.title,
      image = house.image,
      subImage1 = house.subImage1,
      subImage2 = house.subImage2,
      buildingImage = house.buildingImage,
      blueprint = house.blueprint,
      costImage = house.costImage,
      officeImage = house.officeImage,
      price = house.price,
      floorSpace = house.floorSpace,
      roomNumber = house.roomNumber,
      toiletNumber = house.toiletNumber,
      hasLoft = house.hasLoft,
    )
  )
  print(session)
  session.commit()
  
  return house

@house_router.get("/")
async def get_house():
  response=session.query(House).all()
  return response

@house_router.get("/{pid}")
async def get_house(pid: int):
  response=session.query(House).filter(House.id == pid).all()
  return response

@house_router.get("/count/")
async def get_house_count():
  response=session.query(House).count()
  return response