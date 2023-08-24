from pydantic import BaseModel

class BuilderSchema(BaseModel): 
  name: str
  sotong: str
  price: str
  sigongResult: str
  dateJunsu: str
  AS: str
  satisfaction: str
  description: str

class ConstructorSchema(BaseModel): 
  name: str
  sotong: str
  price: str
  sigongResult: str
  dateJunsu: str
  AS: str
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
  constructor: ConstructorSchema
  builder: BuilderSchema
