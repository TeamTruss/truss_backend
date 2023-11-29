from pydantic import BaseModel

from schemas.OfficeSchema import PostOfficeSchema

class PostBuildingSchema(BaseModel): 
  name: str
  src: str
  price: str
  description: str
  rate: float
  like_num: int
  date: str
  office: PostOfficeSchema