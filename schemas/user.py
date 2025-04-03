from pydantic import BaseModel
from typing import List, Optional
from schemas.blog import Blog

class UserBase(BaseModel):
    username : str
    email : str
    password : str


class UserPartial(BaseModel):
    username : Optional[str] = None
    email : Optional[str] = None
    password : Optional[str] = None



class UserDisplay(BaseModel):
    username: str
    email: str
    blogs : List[Blog] = []

    class Config():
        from_atrributes = True


class Login(BaseModel):
    email : str
    password : str