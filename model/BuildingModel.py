from sqlalchemy import Column, TEXT, BIGINT, BOOLEAN
from sqlalchemy.orm import  declarative_base

Base = declarative_base()

class PostHouse(Base):
  __tablename__ = 'house'
  id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
  title = Column(TEXT, nullable=False)
  image = Column(TEXT, nullable=False)
  subImage1 = Column(TEXT, nullable=False)
  subImage2 = Column(TEXT, nullable=False)
  detailImage = Column(TEXT, nullable=False)
  buildingImage = Column(TEXT, nullable=False)
  blueprint = Column(TEXT, nullable=False)
  costImage = Column(TEXT, nullable=False)
  officeImage = Column(TEXT, nullable=False)
  price = Column(BIGINT, nullable=False)
  floorSpace = Column(BIGINT, nullable=False)
  roomNumber = Column(BIGINT, nullable=False)
  toiletNumber = Column(BIGINT, nullable=False)
  hasLoft = Column(BOOLEAN, nullable=False)