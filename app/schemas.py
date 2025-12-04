
from pydantic import BaseModel, EmailStr
from typing import Optional
import datetime


# Base schema shared by all Genre-related schemas.
# This defines the fields that a Genre must have when sent from the client.
class GenreBase(BaseModel):
    name: str

# Schema used when creating a new Genre (POST request).
# Inherits all fields from GenreBase.
# No ID because the database generates it.
class GenreCreate(GenreBase):
    pass

class Genre(GenreBase):
    id: int
    class Config:
        orm_mode = True

class BookBase(BaseModel):
    title: str
    author: str
    pages: Optional[int] = None
    genre_id: int

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    genre: Optional[Genre] = None
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    class Config:
        orm_mode = True

class BorrowedBase(BaseModel):
    user_id: int
    book_id: int
    borrowed_date: Optional[datetime.date] = None
    return_date: Optional[datetime.date] = None

class BorrowedCreate(BorrowedBase):
    pass