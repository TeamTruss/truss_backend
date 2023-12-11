from fastapi import APIRouter, HTTPException
from typing import Optional
from model.HouseModel import House
from schemas.HouseSchema import PostHouseSchema
from config.database import engineconn

house_router = APIRouter(
  prefix="/api/house",
  tags=["house"],
  responses={404: {"description": "Not found"}},
)

engine = engineconn()
session = engine.sessionmaker()

@house_router.post("")
async def post_house(house:PostHouseSchema):
  session.add(
    House(
      title = house.title,
      image = house.image,
      subImage1 = house.subImage1,
      subImage2 = house.subImage2,
      detailImage = house.detailImage,
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
  session.commit()
  
  return house

@house_router.get("")
async def get_house(skip:int, limit:int ,price:Optional[int]=None, floorSpace:Optional[int]=None, roomNumber:Optional[int]=None, toiletNumber:Optional[int]=None):
  response=session.query(House)
  if(price): response=response.filter(House.price<=price)
  if(floorSpace): response=response.filter(House.floorSpace<=floorSpace)
  if(roomNumber): response=response.filter(House.roomNumber==roomNumber)
  if(toiletNumber): response=response.filter(House.toiletNumber==toiletNumber)
  response=response.order_by(House.id.desc()).all()
  return response[skip : skip + limit]

@house_router.get("/last")
async def get_house_last():
  response=session.query(House).order_by(House.id.desc()).first()
  return response

@house_router.get("/{pid}")
async def get_house(pid: int):
  response=session.query(House).filter(House.id == pid).all()
  return response