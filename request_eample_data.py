from fastapi import FastAPI
from pydantic import BaseModel,Field

app=FastAPI()

class Item(BaseModel):
    name:str
    description:str|None=None
    price:float
    tax:float|None=None

    model_config={
        "json_schema_extra":{
            "examples":[
                {
                    "name":"Foo",
                    "description":"This is example of the data your app can receive.",
                    "price":250,
                    "tax":18.8
                }
            ]
        }
    }

@app.post("/items/{item_id}")
def update_item(item_id:int,item:Item):
    result= {"item_id":item_id,"item":item}
    return result

# ----------------------------------------------------------------------------------------------------------

class Items(BaseModel):
    name:str=Field(examples=["Foo","Bar"])
    description:str|None=Field(default=None, examples=["A very nice Item"])
    price:float=Field(examples=[100.25])
    tax:float|None=Field(default=None,examples=[18.25])

@app.put("/item/{item_id}")
def update_item(item_id:int,item:Items):
    result={"item_id":item_id,"item":item}
    return result

# ----------------------------------------------------------------------------------------------------------

from typing import Annotated
from fastapi import FastAPI,Body
from pydantic import BaseModel,Field

# app=FastAPI()

class Item_new(BaseModel):
    name:str
    description:str|None=None
    price:float
    tax:float|None=None

@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Annotated[
        Item_new,
        Body(
            openapi_examples={
                "normal": {
                    "summary": "A normal example",
                    "description": "A **normal** item works correctly.",
                    "value": {
                        "name": "Foo",
                        "description": "A very nice Item",
                        "price": 35.4,
                        "tax": 3.2,
                    },
                },
                "converted": {
                    "summary": "An example with converted data",
                    "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                    "value": {
                        "name": "Bar",
                        "price": "35.4",
                    },
                },
                "invalid": {
                    "summary": "Invalid data is rejected with an error",
                    "value": {
                        "name": "Baz",
                        "price": "thirty five point four",
                    },
                },
            },
        ),
    ],
):
    results = {"item_id": item_id, "item": item}
    return results
                 