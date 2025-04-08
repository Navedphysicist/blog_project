from fastapi import APIRouter, File, UploadFile
import shutil


router = APIRouter(
    prefix='/file',
    tags=['file']
)

@router.post('/')
def get_file(file:bytes = File(...) ):
    content = file.decode('utf-8')
    content_lines = content.split('\n')
    return{
        'content' : content_lines
    }


@router.post('/upload')
def upload_file(upload_file:UploadFile = File(...)):
    path = f"uploaded_files/{upload_file.filename}"
    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(upload_file.file,buffer)

    return{
        'filename': path
    }