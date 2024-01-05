from sqlalchemy import Column, BIGINT
from sqlalchemy.orm import  declarative_base

from model.HouseModel import House
from model.UserModel import User

Base = declarative_base()

class Heart(Base):
  __tablename__ = 'heart'
  id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
  house_id = Column(House, nullable=False)
  user_id = Column(User, nullable=False)