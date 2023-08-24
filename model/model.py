from sqlalchemy import Column, TEXT, BIGINT, BOOLEAN
from sqlalchemy.orm import  declarative_base
  
Base = declarative_base()

class Builder(Base):
  __tablename__ = 'builder'
  id = Column(BIGINT, nullable=False, autoincrement= True, primary_key=True)
  name = Column(TEXT, nullable=False)
  sotong = Column(TEXT, nullable=False)
  price = Column(TEXT, nullable=False)
  sigongResult = Column(TEXT, nullable=False)
  dateJunsu = Column(TEXT, nullable=False)
  afterService = Column(TEXT, nullable=False)
  satisfaction = Column(TEXT, nullable=False)
  description = Column(TEXT, nullable=False)

class Constructor(Base):
  __tablename__ = 'constructor'
  id = Column(BIGINT, nullable=False, autoincrement= True, primary_key=True)
  name = Column(TEXT, nullable=False)
  sotong = Column(TEXT, nullable=False)
  price = Column(TEXT, nullable=False)
  sigongResult = Column(TEXT, nullable=False)
  dateJunsu = Column(TEXT, nullable=False)
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