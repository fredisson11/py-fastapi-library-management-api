from dataclasses import field
from datetime import date
from pydantic import BaseModel

from models import Book


class AuthorBase(BaseModel):
    name: str
    bio: str = None


class AuthorCreate(AuthorBase):
    pass


class Author(AuthorBase):
    id: int
    books: list["Book"] = field(default_factory=list)

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    title: str
    summary: str = None
    publication_date: date = None


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int
    author_id: int
    author: Author

    class Config:
        orm_mode = True
