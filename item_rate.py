from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

# class made for request model
class Item(BaseModel):
    item_id:int
    item_name:str
    price:float
    tax:int | None=None

@app.post("/items/")
def item_price(item:Item):
    item_dict=item.dict()
    if item.tax:
        price_with_tax=item.price +item.tax
        item_dict.update({"price_with_tax":price_with_tax})
    return item_dict

@app.put("/items/{item_id}")
def update_item(item_id:int,item:Item):
    return{"item_id":item_id,**item.dict()}

