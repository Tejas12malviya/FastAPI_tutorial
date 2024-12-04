from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
from typing import List

app=FastAPI()

class Image(BaseModel):
    url:HttpUrl
    name :str

class Item(BaseModel):
    name:str
    Description:str |None=None
    price:float
    tax:float |None=None
    tags:set[str]=set()
    Images:list[Image] | None=None

@app.put("/item/{item_id}")
def update_item(item_id:int,item:Item):
    results={"item_id":item_id,"item":item}
    return results







class Image(BaseModel):
    url: HttpUrl
    name: str

@app.post("/images/multiple/")
async def create_multiple_images(images: list[Image]):
    return images 







class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.put("/items/{item_id}")
def update_item(
    item_id:int,
    item:Annotated[
        Item,
        Body(     # contains predefined values as given in examples
            examples=[
                {
                    "name":"Foo",
                    "description":"A very nice Item",
                    "price":25.1,
                    "tax":2.1
                }
            ]
        )
    ]

):
    result={"item_id":item_id,"item":item}
    return result
