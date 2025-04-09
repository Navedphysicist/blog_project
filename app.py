from fastapi import FastAPI,HTTPException,Depends
from typing import Dict
from pydantic import BaseModel

app  = FastAPI()

def get_token():
     return 'secure-token'


def check_user_authoriztion(token:str = Depends(get_token) ):
    if token != 'secure-token':
        raise HTTPException(status_code=401,detail='Unauthorized')
    return {'user' : 'Authenticated'}
    

@app.get('/profile')
def get_profile(user:Dict = Depends(check_user_authoriztion)):
    return {'msg':'User Profile'}



@app.get('/settings')
def get_settings(setting: Dict = Depends(check_user_authoriztion)):
    return {'msg':'Settings'}


# class Account:
#     def __init__(self,name,email):
#         self.name = name
#         self.email = email

# @app.post('/user')
# def create_user(user:Account = Depends()):
#     return {
#         'username' : user.name,
#         'useremail': user.email
#     }

class Account(BaseModel):
        name : str
        email:str

@app.post('/user')
def create_user(user:Account):
    return {
        'username' : user.name,
        'useremail': user.email
    }