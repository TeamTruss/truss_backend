from pydantic import BaseModel

class PostHouseSchema(BaseModel):
  title : str
  image: str
  subImage1: str
  subImage2: str
  detailImage: str
  buildingImage: str
  blueprint: str
  costImage: str
  officeImage: str
  price : int
  floorSpace : int
  roomNumber : int
  toiletNumber : int
  hasLoft : bool