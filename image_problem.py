from fastapi import FastAPI
from pydantic import BaseModel,HttpUrl

app=FastAPI()

class Image(BaseModel):
    url:HttpUrl
    name:str

class Item(BaseModel):
    name:str
    description:str|None=None
    price:int
    tax:float|None=None
    tags:set[str]=set()
    image:Image|None=None

@app.put("/item/{item_id}")
def update_item(item_id:int,item:Item):
    result={"item_id":item_id,"item":item}
    return result


# ----------------------------------------------------------------------------------------------------------
# Deeply Nested model for image

class Image(BaseModel):
    url:HttpUrl
    name:str

class Item(BaseModel):
    item_name:str
    description:str|None=None
    price:int
    tax:float|None=None
    images:list[Image]|None=None

class Offer(BaseModel):
    name:str
    description:str|None=None
    price:float
    item:list[Item]

@app.post("/offers/",description="This is deeply nested image post docker")
def create_offer(offer:Offer):
    return offer

