
from typing import Optional

from fastapi import FastAPI
from pydantic import  BaseModel,Field


# Body do not allow any type of validation but pydantic allows us to do it using BaseModel, Field

app=FastAPI()

class Book:
    id:int
    title:str
    author:str
    description:str
    rating:int

    def __init__(self,id,title,author,description,rating):
        self.id=id
        self.title=title
        self.author=author
        self.description=description
        self.rating=rating

class BookRequest(BaseModel):
    id: Optional[int]=Field(description="Id is not needed on create.",default=None) # by implementing optional we do not need to post id ,it becomes optional . It automatically take its value any shows null response for post if nothing is posted
    title: str=Field(min_length=3)
    author:str=Field(min_length=3)
    description:str=Field(min_length=1,max_length=100)
    rating:int=Field(gt=0,lt=6)
     # To give example values for the post we use "jason_schema_extra" in model_config inside the BookRequest.
    model_config={
        "json_schema_extra":{
            "example":{
                "title":"A new Book",
                "author":"Author_name",
                "description":"About_book",
                "rating":5
            }
        }
    }

Books=[
    Book(1,'2 State','Chetan Bhagat','A very nice book',5),
    Book(2, 'Ram Chandra Series', 'Amish Tripathi', 'Mythology book', 5),
    Book(3, 'The Shiva Trilogy', 'Amish Tripathi', 'Mythology book', 4),
    Book(4, 'Wings of Fire', 'A.P.J. Abdul Kalam', 'A very nice book', 5),
    Book(5, 'The 3 Mistakes of My Life', 'Chetan Bhagat', 'A very nice book', 4)
]

@app.get("/")
def read_all_books():
    return Books

@app.get("/book/{book_id}")
def book_id(book_id:int):
    for book in Books:
        if book.id==book_id:
            return book

@app.get("/books/")
def read_book(rating:int):
    list=[]
    for book in Books:
        if book.rating==rating:
            list.append(book)
    return list

@app.post("/create_book/")
def create_book(book:BookRequest):
    new_book=Book(**book.dict())
    Books.append(new_book_id(new_book))
    return book

# after defining this function we get unique id's for entering each data through post, even we post any data it shows the previous_id+1
def new_book_id(n:Book):
    if len(Books)>0:
        n.id=Books[-1].id+1
    else:
        n.id=1

    return n

@app.put("/books/update_book")
def update_book(book:BookRequest):
    for i in range(len(Books)):
        if Books[i].id ==book.id:
            Books[i]==book

@app.delete("/books/delete_book/{book_id}")
def delete_book(book_id:int):
    for i in range(len(Books)):
        if Books[i].id==book_id:
            Books.pop(i)
            break
