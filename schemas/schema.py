from pydantic import BaseModel

class BuilderSchema(BaseModel): 
  name: str
  url: str

class OfficeSchema(BaseModel): 
  name: str
  url: str
  
class BuildingSchema(BaseModel): 
  name: str
  src: str
  price: str
  minPrice: str
  minDate: str
  maxDate: str
  desc: str
  rate: float
  like: int
  date: str
  office: BuilderSchema
  builder: OfficeSchema
