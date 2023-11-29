from datetime import datetime
from sqlalchemy import Column, TEXT, BIGINT, DateTime
from sqlalchemy.orm import  declarative_base

Base = declarative_base()

class Post(Base):
  __tablename__ = 'post'
  id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
  title = Column(TEXT, nullable=False)
  text = Column(TEXT, nullable=False)
  author = Column(TEXT, nullable=False)
  created_at = Column(DateTime, nullable=False, default=datetime.now)
  updated_at = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
  category = Column(TEXT, nullable=False)
  thumbnail = Column(TEXT, nullable=False)
  likeCount = Column(BIGINT, nullable=False)
  viewCount = Column(BIGINT, nullable=False)
  comments = Column(TEXT, nullable=False)