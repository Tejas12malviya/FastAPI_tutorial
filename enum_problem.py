from enum import Enum

from fastapi import FastAPI

class ModelName(str,Enum):
    alexnet ="alexnet"
    resnet="resnet"
    lenet="lenet"

app=FastAPI()

@app.get("/models/{model_name}")
def get_model(model_name: ModelName):
    # if model_name is ModelName.alexnet:
    #     return {"model_name": model_name, "message":"Deep Lerning FTW!"}
    
    if model_name.value=="alexnet":
        return {"model_name": model_name, "message":"Deep Lerning FTW!"}
    if model_name.value=="lenet":
        return{"model_name":model_name,"message":"LeCNN all the images"}
    return {"model_name": model_name,"message":"Have some residuals"}


fake_items_db = [{"item_name":"Foo"},{"item_name":"Bar"},{"item_name":"Baz"}]

@app.get("/items/")
def read_item(skip:int=0, limit:int=10):
    return fake_items_db[skip: skip+limit] 

@app.get("/users/{user_id}/items/{item_id}")
def read_user_items(
    user_id:int,item_id:str, q:str | None=None, short:bool=False
):
    item={"item_id":item_id,"owner_id":user_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

