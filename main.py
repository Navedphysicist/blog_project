from fastapi import FastAPI,Request
from db.database import engine , Base
from routers import user,blog , auth, product,handle_file,templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import time
import asyncio


app = FastAPI()

app.include_router(user.router)
app.include_router(blog.router)
app.include_router(auth.router)
app.include_router(product.router)
app.include_router(handle_file.router)
app.include_router(templates.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins= ['*'],
    allow_credentials = True,
    allow_methods=['*'],
    allow_headers=['*']  )

app.mount('/files',StaticFiles(directory='uploaded_files'), name='files')
app.mount('/templates/static',StaticFiles(directory='templates/static'), name='templates/static')

@app.middleware('http')
async def log_requests(request:Request,call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start
    print(f"Request: {request.url} | Time Take: {duration}")
    return response


@app.get('/blocking')
def blocking_route():
    time.sleep(10)  #blocking

    return{
        'route' : 'blocking'
    }
@app.get('/non-blocking')
async def non_blocking_route():
   await asyncio.sleep(10) 
   return {
       'route': 'non-blocking'
   }



@app.get('/')
def index():
    return {'message':'Welcome to Blog API'}


Base.metadata.create_all(engine)


