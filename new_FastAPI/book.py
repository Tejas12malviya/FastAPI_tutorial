from fastapi import FastAPI,Body
app=FastAPI()

Books=[
    {'title':'Title One','author':'Author One','category':'Science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'Chemistry'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'Physics'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'Math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'Math'},
    {'title': 'Title Six', 'author': 'Author One', 'category': 'Math'}

]


@app.get("/")
async def book():
    return Books

@app.get("/read_all_books")
async def book():
    return Books

@app.get("/book/{book_title}")
def book_title(book_title:str):
    for book in Books:
        if book.get('title').casefold()==book_title.casefold():
            return book

@app.get("/book/")
def book_title(book_author:str):
    list=[]
    for book in Books:
        if book.get('author').casefold()==book_author.casefold():
            list.append(book)

@app.post("/add_book/")
def add_book(book=Body()):
    Books.append(book)
    return book

@app.put("/update_book/{book_title}")
def update_book(book_title:str,book=Body()):
    for i in range(len(Books)):
        if Books[i].get('title').casefold()==book_title.casefold():
            Books[i]==book
            return book

@app.delete("/delete_book/{book_title}")
def delete_book(book_title:str):
    for i in range(len(Books)):
        if Books[i].get('title').casefold()==book_title.casefold():
            book=Books[i]
            del Books[i]
            return book
        else:
            return 'Book not Found'