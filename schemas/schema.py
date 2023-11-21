from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class OfficeSchema(BaseModel): 
  officeType: str
  officeName: str
  communication: str
  price: str
  result: str
  keepingDeadline: str
  afterService: str
  satisfaction: str
  description: str

class PersonSchema(BaseModel):
  name: str
  phoneNumber: str
  type: str
  location: str
  agree: bool

class PostSchema(BaseModel):
  title : str
  text : str
  author : str
  category : str
  thumbnail : str

class HouseSchema(BaseModel):
  title : str
  image: str
  subImage1: str
  subImage2: str
  buildingImage: str
  blueprint: str
  costImage: str
  officeImage: str
  price : int
  floorSpace : int
  roomNumber : int
  toiletNumber : int
  hasLoft : bool






class BuildingSchema(BaseModel): 
  name: str
  src: str
  price: str
  description: str
  rate: float
  like_num: int
  date: str
  office: OfficeSchema
