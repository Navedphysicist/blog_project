from fastapi import HTTPException ,status
from sqlalchemy.orm import Session
from schemas.user import UserBase,UserPartial
from models.user import DbUser
from hash import Hash

def create_user(db:Session,request:UserBase):
    new_user = DbUser(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all_users(db:Session):
    users = db.query(DbUser).all()
    return users

def get_user(db:Session,id:int):
    user =  db.query(DbUser).filter(DbUser.id == id).first()

    if not user:
        raise HTTPException(
        status_code= status.HTTP_404_NOT_FOUND,
        detail=f"User with id: {id} not found"
    )

    return user


# def update_user(db:Session,id:int,request:UserBase):
#    user =  db.query(DbUser).filter(DbUser.id == id)

#    if not user.first():
#        return None
   
#    user.update({
#        DbUser.username : request.username,
#        DbUser.email : request.email,
#        DbUser.password : request.password
#    })

#    db.commit()
#    return user
   

def update_user(db:Session,id:int,request:UserBase):
   user =  db.query(DbUser).filter(DbUser.id == id).first()

   if not user:
        raise HTTPException(
        status_code= status.HTTP_404_NOT_FOUND,
        detail=f"User with id: {id} not found"
    )
   
   user.username = request.username
   user.email = request.email
   user.password = request.password


   db.commit()
   db.refresh(user)
   return user

    
def update_user_partial(db:Session,id:int,request : UserPartial):
    user = db.query(DbUser).filter(DbUser.id==id).first()

    if not user:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail=f"User with id: {id} not found"
        )
    
    if request.username is not None:
        user.username = request.username

    if request.email is not None:
        user.email = request.email

    if request.password is not None:
        user.password = request.password

    db.commit()
    db.refresh(user)
    return user


def delete_user(db:Session,id:int):
    user = db.query(DbUser).filter(DbUser.id == id).first()

    if not user:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail=f"User with id: {id} not found"
        )
    
    db.delete(user)
    db.commit()
    return 'User Deleted Successfully'

def login_user(db:Session ,email: str, password: str):
    user  = db.query(DbUser).filter(DbUser.email == email).first()

    if not user:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail=f"User with email: {email} not found"
        )
       
    
    if not Hash.verify(password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect Password"
        )
    
    
    return {'message': "Login Successful" , "username": user.username}