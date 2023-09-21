from sqlalchemy import Column, TEXT, BIGINT, BOOLEAN
from sqlalchemy.orm import  declarative_base
  
Base = declarative_base()

class Office(Base):
  __tablename__ = 'office'
  id = Column(BIGINT, nullable=False, autoincrement= True, primary_key=True)
  officeType = Column(TEXT, nullable=False)
  officeName = Column(TEXT, nullable=False)
  communication = Column(TEXT, nullable=False)
  price = Column(TEXT, nullable=False)
  result = Column(TEXT, nullable=False)
  keepingDeadline = Column(TEXT, nullable=False)
  afterService = Column(TEXT, nullable=False)
  satisfaction = Column(TEXT, nullable=False)
  description = Column(TEXT, nullable=False)

class Person(Base):
  __tablename__ = 'person'
  id = Column(BIGINT, nullable=False, autoincrement= True, primary_key=True)
  name = Column(TEXT, nullable=False)
  phoneNumber = Column(TEXT, nullable=False)
  type = Column(TEXT, nullable=False)
  location = Column(TEXT, nullable=False)
  agree = Column(BOOLEAN, nullable=False)

class Comment(Base):
  __tablename__ = 'comment'
  id= Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
  author=Column(BIGINT, nullable=False)
  text=Column(TEXT, nullable=False)

class Post(Base):
  __tablename__ = 'post'
  id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
  title = Column(TEXT, nullable=False)
  text = Column(TEXT, nullable=False)
  pictures = Column(TEXT, nullable=False)
  author = Column(TEXT, nullable=False)
  timestamp = Column(BIGINT, nullable=False)
  category = Column(TEXT, nullable=False)
  thumbnail = Column(TEXT, nullable=False)
  likeCount = Column(BIGINT, nullable=False)
  viewCount = Column(BIGINT, nullable=False)
  comments = Column(TEXT, nullable=False)
  

