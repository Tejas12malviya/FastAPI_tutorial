# To rum this .py file write 'fastapi dev introduction.py' in your terminal 


from fastapi import FastAPI

app = FastAPI()


@app.get("/")   #path operation decorator
async def root():    #path operation function
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def item(item_id:int):  #decelaration of variable path decorator as i.e., caliing item_id in int formate
    return {"item id: ":item_id}

@app.get("/user/{user_name}")
def user(user_name):  #here user_name is set as string by default
    return {"User name is ":user_name}
 

# Note: This path operation decorator will not work because when we will call /user/me , the upper path operation decorator will take me as an attribute for user_name so we need to write it above the /user /{user_name}, Also we can not rewrite the path operation decorator .
@app.get("/user/me")
def user():
    return {"I am the new user"}

@app.get("/user/me")
def user():
    return {"I am working as the new user"}

@app.get("/item/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
