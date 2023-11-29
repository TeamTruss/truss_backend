from pydantic import BaseModel

class PostPersonSchema(BaseModel):
  name: str
  phoneNumber: str
  type: str
  location: str
  agree: bool