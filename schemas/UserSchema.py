from pydantic import BaseModel

class PostUserSchema(BaseModel):
  name: str