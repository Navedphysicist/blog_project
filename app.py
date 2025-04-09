from fastapi import FastAPI,HTTPException,Depends
from typing import Dict

app  = FastAPI


def check_user_authoriztion(token:str ):
    if token != 'secure-token':
        raise HTTPException
    return {'user' : 'Authenticated'}
    

@app.get('/profile')
def get_profile(user:Dict = Depends(check_user_authoriztion)):
    return {'msg':'User Profile'}


    

@app.get('/settings')
def get_settings(setting: Dict = Depends(check_user_authoriztion)):
    return {'msg':'Settings'}