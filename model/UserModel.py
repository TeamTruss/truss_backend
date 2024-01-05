from sqlalchemy import Column, TEXT, BIGINT, BOOLEAN
from sqlalchemy.orm import  declarative_base

Base = declarative_base()

class User(Base):
  __tablename__ = 'user'
  id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
  name = Column(TEXT, nullable=False)
  role = Column(TEXT, nullable=False)