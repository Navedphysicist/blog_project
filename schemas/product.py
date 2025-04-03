from pydantic import BaseModel

class ProdcutInfo(BaseModel):
    name : str
    brand_name : str
    price : float