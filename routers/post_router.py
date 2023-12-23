from fastapi import APIRouter, HTTPException
from typing import Optional
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
  try:
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
    session.commit()
    return session.query(Post).order_by(Post.id.desc()).first()
  except:
    session.rollback()

@post_router.get("")
async def get_posts(skip:int, limit:int, category:Optional[str]=None):
  response=session.query(Post)
  if(category): response=response.filter(Post.category==category)
  response=response.order_by(Post.id.desc()).all()
  return response[skip : skip + limit]

@post_router.get("/count")
async def get_posts_count(category:Optional[str]=None):
  response=session.query(Post)
  if(category): response=response.filter(Post.category==category)
  return response.count()

@post_router.get("/{pid}")
async def get_post(pid:int):
  response=session.query(Post).filter(Post.id==pid).one()
  return response
