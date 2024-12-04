from typing import Annotated,Literal
from fastapi import FastAPI,Query
from pydantic import BaseModel, Field

app=FastAPI()

class FilterParams(BaseModel):
    # model_config = {"extra":"forbid"} 

    limit:int=Field(100, gt=0,le=100)
    offset:int=Field(10,ge=0)
    order_by:Literal["created_at","updated_at"]="created_at"
    tags:list[str]=[]

@app.get("/items/")
def read_items(filter_query:Annotated[FilterParams,Query()]):
    return filter_query 

# Multi body parameters

class User(BaseModel):
    username:str
    fullname:str | None=None

class Item(BaseModel):
    item_id:int
    item_name:str
    price:int
    tax:float | None=None

@app.post("/user/item/")
def update_item(item:Item,user:User):
    item_dict=item.dict()
    if item.tax:
        results=item.price+item.tax
        item_dict.update({"price with tax":results})

    return item_dict,user
  