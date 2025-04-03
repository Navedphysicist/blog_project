from pydantic import BaseModel


class Blog(BaseModel):
    title : str
    content : str

    class Config:
        from_atrributes = True

