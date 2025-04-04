from fastapi import APIRouter, Header , Cookie , Form, UploadFile,File, Depends
from fastapi.responses import Response,HTMLResponse , PlainTextResponse
from typing import Optional , List
from utils.token import oauth2_scheme
# from schemas.product import ProdcutInfo


router = APIRouter(
    prefix='/products',
    tags=['products']
)

products = ['Laptop','Tablet','Smartphone']




@router.get('/')
def get_all_products():
    result = " ".join(products)
    return Response(content=result,media_type='text/plain')


@router.get('/header')
def get_headers(custom_header : Optional[List[str]] = Header(None), my_cookie : Optional[str]= Cookie(None) ):
    return {
        'custom_header' : custom_header,
        'cookie' : my_cookie
    }
    
@router.get('/resposne_header')
def get_response_headers(response  : Response):
    response.headers['token'] = 'lkjslfknfvlsjfrls'
    response.set_cookie(key='my_cookie',value='naved_cookie_2')
    return { 'message' : 'Response headers added'}


@router.get('/{id}', responses={
    200 : {
        'content':{
            'text/html':{
                'example': '<div>Product<div>'
            }
        },
        'description': 'Returns the HTML Response'
    },
     400 : {
        'content':{
            'plain/text':{
                'example': 'Product not available'
            }
        },
        'description': 'Returns the Plain text Response'
    }


})
def get_product(id:int):
    
    if id >= len(products):
        message = f"No product with id: {id} is available."

        return PlainTextResponse(content=message,media_type='Plain/text')

    product = products[id]

    data = f"""
    <head>
    <style>
        .product {{
        width: 500px;
        height: 30px;
        border: 2px inset green;
        background-color: lightblue;
        text-align: center;
        line-height: 30px;
        font-weight: bold;
        font-family: Arial, sans-serif;
        }}
    </style>
    </head>
    <body>

  <div class="product">{product}</div>

</body>
"""
    return  HTMLResponse(content=data,media_type='text/html')


@router.post('/create')
def create_product( name : str = Form(...), 
                   brand_name : str = Form(...), 
                   price : Optional[float] = Form(...),
                   image: UploadFile = File(...),
                   token:str = Depends(oauth2_scheme)):
    return {
        'name' : name,
        'brand' : brand_name,
        'price' : price,
        'image' : image.filename
    }





# @router.post('/create')
# def create_product(request : ProdcutInfo):
#     return {
#         'name' : request.name,
#         'brand' : request.brand_name,
#         'price' : request.price
#     }