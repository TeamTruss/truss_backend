from fastapi import APIRouter, Depends, HTTPException

from config.database import engineconn
from config.Oauth import oauth2_scheme

security_router = APIRouter(
  prefix="/api/security",
  tags=["security"],
  responses={404: {"description": "Not found"}},
)

engine = engineconn()
session = engine.sessionmaker()

@security_router.post("/signin")
async def signin(token: str = Depends(oauth2_scheme)):
  
  return { "token": token }

@security_router.post("/signout")
async def signout(sign:str):
  session.add(
  )
  session.commit()
  return sign

@security_router.post("/validate")
async def validate(sign:str):
  session.add(
  )
  session.commit()
  return sign

@security_router.post("/refresh")
async def refresh(sign:str):
  session.add(
  )
  session.commit()
  return sign