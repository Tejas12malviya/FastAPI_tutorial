from fastapi import FastAPI, Query, Path
from typing import Annotated

app=FastAPI()

@app.get("/items/{item_id}")
def read_item(
    item_id:Annotated[int,Path(title="The ID of item to get")],
    q:Annotated[str|None,Query(alias="item-query")]=None
):
    result={"item_id":item_id}
    if q:
        result.update({"q":q})
    return result


# path parameter with default value as "Hello"

@app.get("/item/{item_id}")
def read_item(item_id: Annotated[int,Path(title="The ID of the item to get")],q:str|None=Query(default="Hello",max_length=50)):
    result={"item_id":item_id}
    if q :
        result.update({"q":q})
    return result  

# path parameter with with fixed pattern

@app.get("/item/")
def read_item(
    q:Annotated[
        str|None,Query(min_length=3,max_length=50,pattern="^fixedquery$")
    ]=None,
):
    result={"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}
    if q:
        result.update({'q':q})
    return result

'''
We can use generic validation such as :
alias 
title
description etc

and specific validation for strings are :
min_length
max_length
pattern etc

'''
