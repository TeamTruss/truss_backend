from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class PostOfficeSchema(BaseModel): 
  officeType: str
  officeName: str
  communication: str
  price: str
  result: str
  keepingDeadline: str
  afterService: str
  satisfaction: str
  description: str













