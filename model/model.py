from sqlalchemy import Column, TEXT, BIGINT
from sqlalchemy.orm import  declarative_base
  
Base = declarative_base()

class Builder(Base):
  __tablename__ = 'builder'
  id = Column(BIGINT, nullable=False, autoincrement= True, primary_key=True)
  name = Column(TEXT, nullable=False)
  url = Column(TEXT, nullable=False)

class Office(Base):
  __tablename__ = 'office'
  id = Column(BIGINT, nullable=False, autoincrement= True, primary_key=True)
  name = Column(TEXT, nullable=False)
  url = Column(TEXT, nullable=False)

class Building(Base):
  __tablename__ = 'building'
  id = Column(BIGINT, nullable=False, autoincrement= True, primary_key=True)
  name = Column(TEXT, nullable=False)
  url = Column(TEXT, nullable=False)