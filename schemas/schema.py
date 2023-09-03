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




class BuildingSchema(BaseModel): 
  name: str
  src: str
  price: str
  description: str
  rate: float
  like_num: int
  date: str
  office: OfficeSchema
