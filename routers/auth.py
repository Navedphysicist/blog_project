from fastapi import APIRouter, Depends
from schemas.user import Login
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user




router = APIRouter(
    prefix='/auth',
    tags = ['Auth']
)


@router.post('/login')
def login(request:Login , db: Session = Depends(get_db)):
    return db_user.login_user(db,request.email, request.password)