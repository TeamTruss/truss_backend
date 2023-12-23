from os import environ
from dotenv.main import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

# 디비 접속 URL
DB_CONN_URL = '{}://{}:{}@{}:{}/{}'.format(
    environ['DB_TYPE'],
    environ['DB_USER'],
    environ['DB_PASSWORD'],
    environ['DB_HOST'],
    environ['DB_PORT'],
    environ['DB_NAME'],
)

class engineconn:
  def __init__(self):
    self.engine = create_engine(DB_CONN_URL)

  def sessionmaker(self):
    return sessionmaker(bind=self.engine, autoflush=True, autocommit=False)()
  
  def connection(self):
    return self.engine.connect()
  
