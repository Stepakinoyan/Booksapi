import requests
from schema import Books
from fake_useragent import UserAgent


def get_books(q: str):
    headers = {
        'user-agent': UserAgent().random
    }

    response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={q}", headers=headers).json()


    books = Books(**response)

    return books.model_dump(mode="json")