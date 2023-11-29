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

