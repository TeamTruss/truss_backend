from pydantic import BaseModel

class PostPostSchema(BaseModel):
  title : str
  text : str
  author : str
  category : str
  thumbnail : str