from fastapi import APIRouter, Depends
from schemas.blog import Blog
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_blog
from typing import List
from utils.token import oauth2_scheme , get_current_user
from schemas.user import UserBase


router = APIRouter(
    prefix='/blogs',
    tags=['blogs']
)

@router.post('/',response_model=Blog)
def create_blog(request : Blog,db:Session = Depends(get_db), current_user:UserBase= Depends(get_current_user)):
    user_id = current_user.id
    return db_blog.create_blog(db,request,user_id)

@router.get('/',response_model=List[Blog])
def get_all_blogs(db:Session = Depends(get_db)):
    return db_blog.get_all_blogs(db)