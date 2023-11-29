from sqlalchemy import Column, TEXT, BIGINT, BOOLEAN
from sqlalchemy.orm import  declarative_base

Base = declarative_base()

class Person(Base):
  __tablename__ = 'person'
  id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
  name = Column(TEXT, nullable=False)
  phoneNumber = Column(TEXT, nullable=False)
  type = Column(TEXT, nullable=False)
  location = Column(TEXT, nullable=False)
  agree = Column(BOOLEAN, nullable=False)