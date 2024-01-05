from fastapi import APIRouter, HTTPException
from model.UserModel import User
from schemas.UserSchema import PostUserSchema
from config.database import engineconn

user_router = APIRouter(
  prefix="/api/user",
  tags=["user"],
  responses={404: {"description": "Not found"}},
)

engine = engineconn()
session = engine.sessionmaker()

@user_router.post("/")
async def post_user(User:PostUserSchema):
  try:
    session.add(
      User(
        name = User.name,
        role = "user"
      )
    )
    session.commit()
  except:
    session.rollback()
  finally:
    session.close()

@user_router.get("/")
async def get_users():
  response=session.query(User).all()
  return response
