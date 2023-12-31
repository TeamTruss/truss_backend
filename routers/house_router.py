from fastapi import APIRouter, HTTPException
from typing import Optional
from func.get_count import get_count
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
  try:
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
  except:
    session.rollback()
    raise
  finally:
    session.close()

@house_router.get("")
async def get_houses(skip:int, limit:int, price:Optional[int]=None, floorSpace:Optional[int]=None, roomNumber:Optional[int]=None, toiletNumber:Optional[int]=None):
  try:
    response=session.query(House)
    if(price): response=response.filter(House.price<=price)
    if(floorSpace): response=response.filter(House.floorSpace<=floorSpace)
    if(roomNumber): response=response.filter(House.roomNumber==roomNumber)
    if(toiletNumber): response=response.filter(House.toiletNumber==toiletNumber)
    response=response.order_by(House.id.desc()).all()
    return response[skip : skip + limit]
  except:
    session.rollback()
    raise
  finally:
    session.close()

@house_router.get("/last")
async def get_house_last():
  response=session.query(House).order_by(House.id.desc()).first()
  return response

@house_router.get("/count")
async def get_house_count(minPrice:Optional[int]=None,maxPrice:Optional[int]=None, minFloorSpace:Optional[int]=None, maxFloorSpace:Optional[int]=None, roomNumber:Optional[int]=None, toiletNumber:Optional[int]=None):
  response=session.query(House)
  if(minPrice): response=response.filter(House.price>=minPrice)
  if(maxPrice): response=response.filter(House.price<=maxPrice)
  if(minFloorSpace): response=response.filter(House.floorSpace>=minFloorSpace)
  if(maxFloorSpace): response=response.filter(House.floorSpace<=maxFloorSpace)
  if(roomNumber): response=response.filter(House.roomNumber==roomNumber)
  if(toiletNumber): response=response.filter(House.toiletNumber==toiletNumber)
  return response.count() #get_count(response)

@house_router.get("/{pid}")
async def get_house(pid: int):
  response=session.query(House).filter(House.id == pid).all()
  return response

