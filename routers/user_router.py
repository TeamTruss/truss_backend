from fastapi import APIRouter, HTTPException
from model.PersonModel import Person
from schemas.PersonSchema import PostPersonSchema
from config.database import engineconn

person_router = APIRouter(
  prefix="/api/user",
  tags=["person"],
  responses={404: {"description": "Not found"}},
)

engine = engineconn()
session = engine.sessionmaker()

@person_router.post("/")
async def post_person(person:PostPersonSchema):
  try:
    session.add(
      Person(
        name = person.name,
        phoneNumber = person.phoneNumber,
        type = person.type,
        location = person.location,
        agree = person.agree,
      )
    )
    session.commit()
  except:
    session.rollback()

@person_router.get("/")
async def get_persons():
  response=session.query(Person).all()
  return response
