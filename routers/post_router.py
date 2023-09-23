from fastapi import APIRouter, HTTPException
from model.model import Post
from schemas.schema import PostSchema
from config.database import engineconn

post_router = APIRouter(
  prefix="/api/post",
  tags=["post"],
  responses={404: {"description": "Not found"}},
)

engine = engineconn()
session = engine.sessionmaker()

@post_router.post("/")
async def post_post(post:PostSchema):
  session.add(
    Post(
      title = post.title,
      text = post.text,
      pictures = post.pictures,
      author = post.author,
      timestamp = post.timestamp,
      category = post.category,
      thumbnail = post.thumbnail,
      likeCount = post.likeCount,
      viewCount = post.viewCount,
      comments = post.comments
    )
  )
  session.commit()
  return post

@post_router.get("/")
async def get_posts():
  response=session.query(Post).all()
  return response