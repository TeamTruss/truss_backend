from datetime import datetime
from sqlalchemy import ARRAY, Column, TEXT, BIGINT, BOOLEAN, DateTime
from sqlalchemy.orm import  declarative_base
  
Base = declarative_base()

class Comment(Base):
  __tablename__ = 'comment'
  id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
  author = Column(BIGINT, nullable=False)
  text = Column(TEXT, nullable=False)

class User(Base):
  __tablename__ = 'User'
  id=Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
  name=Column(TEXT, nullable=False)

class RatingPost(Base):
  __tablename__ = 'rating_post'
  id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
  title = Column(TEXT, nullable=False)
  thumbnail = Column(TEXT, nullable=False)
  author = Column(BIGINT, nullable=False)
  rate = Column(BIGINT, nullable=False)




