from fastapi import APIRouter, Depends
from schemas.user import UserDisplay,UserBase,UserPartial
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user
from typing import List


router = APIRouter(
    prefix='/user',
    tags = ['User']
)

@router.post('/',response_model=UserDisplay)
def create_user(request : UserBase, db:Session = Depends(get_db)):
    return db_user.create_user(db,request)
   
@router.get('/',response_model= List[UserDisplay])
def get_all_users(db:Session = Depends(get_db)):
    return db_user.get_all_users(db)

@router.get('/{id}')
def get_user(id : int ,db:Session= Depends(get_db)):
    return db_user.get_user(db,id)

@router.put('/{id}')
def update_user(id:int,request:UserBase,db:Session = Depends(get_db)):
    return db_user.update_user(db,id,request)

@router.patch('/{id}')
def update_user_partial(id:int,request:UserPartial,db:Session = Depends(get_db)):
    return db_user.update_user_partial(db,id,request)

@router.delete('/{id}')
def delete_user(id:int,db:Session = Depends(get_db)):
    return db_user.delete_user(db,id)