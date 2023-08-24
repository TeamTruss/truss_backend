from fastapi import APIRouter, HTTPException
from model.model import Person
from schemas.schema import PersonSchema
from config.database import engineconn

person_router = APIRouter(
  prefix="/api/person",
  tags=["person"],
  responses={404: {"description": "Not found"}},
)

engine = engineconn()
session = engine.sessionmaker()

@person_router.post("/")
async def post_person(person:PersonSchema):
  session.add(
    Person(
      name=person.name,
      phoneNumber=person.phoneNumber,
      type=person.type,
      location=person.location,
      agree=person.agree,
    )
  )
  session.commit()
  return person

@person_router.get("/")
async def get_persons():
  return {
    "title": "string",
    "src": "string",
    "minDate": "string",
    "maxDate": "string",
    "minPrice": "string"
  }
