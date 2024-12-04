from fastapi import FastAPI,Query,Path
from pydantic import BaseModel
from typing import Annotated

app=FastAPI()


@app.get("/items/")
def read_items(q:str | None =None):
    result={"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}
    if q:
        result.update({"q":q})
    return result


# Giving limit to query parameter
@app.get("/item/")
def read_items(q:Annotated[str |None,Query(max_length=50)] =None):
    result={"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}
    if q:
        result.update({"q":q})
    return result