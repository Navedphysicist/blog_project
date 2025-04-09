from fastapi import APIRouter,Request,Form,UploadFile,File
from fastapi.templating import Jinja2Templates
import shutil


router = APIRouter(
    prefix='/templates',
    tags=['templates']
)

templates = Jinja2Templates(directory='templates')

@router.post('/user_profile')
async def show_user_profile(
        request : Request,
        name : str = Form(...),
        email : str = Form(...),
        position : str = Form(...),
        avatar : UploadFile = File(None)
):
    avatar_url = None
    if avatar:
     file_location =   f"templates/static/avatars/{avatar.filename}"
     with open(file_location,"wb") as buffer:
        shutil.copyfileobj(avatar.file,buffer)

    avatar_url = f"/templates/static/avatars/{avatar.filename}"

    return templates.TemplateResponse('user_profile.html',{
       'request':request,
       'name': name,
       'email':email,
       'position':position,
       'avatar_url':avatar_url
    })

    