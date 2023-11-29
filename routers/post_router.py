from fastapi import APIRouter, HTTPException
from model.PostModel import Post
from schemas.PostSchema import PostPostSchema
from config.database import engineconn

post_router = APIRouter(
  prefix="/api/post",
  tags=["post"],
  responses={404: {"description": "Not found"}},
)

engine = engineconn()
session = engine.sessionmaker()

@post_router.post("")
async def post_post(post:PostPostSchema):
  session.add(
    Post(
      title = post.title,
      text = post.text,
      author = post.author,
      category = post.category,
      thumbnail = post.thumbnail,
      likeCount = 0,
      viewCount = 0,
      comments = ""
    )
  )
  try:
    session.commit()
  except:
    session.rollback()
    raise
  finally:
    session.close() 
  return post

@post_router.get("")
async def get_posts():
  response=session.query(Post).all()#.filter(Post.timestamp > 20)
  return response

@post_router.get("/{pid}")
async def get_post(pid:int):
  response=session.query(Post).filter(Post.id==pid).one()
  return response
