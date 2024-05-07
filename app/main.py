from fastapi import FastAPI

from books import get_books

app = FastAPI()


@app.get("/books")
def books(q: str):
    return get_books(q)
    