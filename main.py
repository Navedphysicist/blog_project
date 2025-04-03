from fastapi import FastAPI
from db.database import engine , Base
from routers import user,blog , auth, product
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.include_router(user.router)
app.include_router(blog.router)
app.include_router(auth.router)
app.include_router(product.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins= ['*'],
    allow_credentials = True,
    allow_methods=['*'],
    allow_headers=['*']  )


@app.get('/')
def index():
    return {'message':'Welcome to Blog API'}


Base.metadata.create_all(engine)


