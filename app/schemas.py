
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

# Schema for Genre response from the database.
# Includes the auto-generated ID and enables ORM mode for SQLAlchemy compatibility.
class Genre(GenreBase):
    id: int
    class Config:
        orm_mode = True



# Base schema for Book with required and optional fields.
class BookBase(BaseModel):
    title: str
    author: str
    pages: Optional[int] = None
    genre_id: int

# Schema used when creating a new Book (POST request).
class BookCreate(BookBase):
    pass

# Schema for Book response from the database.
# Includes the auto-generated ID and related Genre object.
class Book(BookBase):
    id: int
    genre: Optional[Genre] = None
    class Config:
        orm_mode = True



# Base schema for User with required fields.
class UserBase(BaseModel):
    name: str
    email: EmailStr

# Schema used when creating a new User (POST request).
class UserCreate(UserBase):
    pass

# Schema for User response from the database.
# Includes the auto-generated ID.
class User(UserBase):
    id: int
    class Config:
        orm_mode = True



# Base schema for tracking borrowed books with dates.
class BorrowedBase(BaseModel):
    user_id: int
    book_id: int
    borrowed_date: Optional[datetime.date] = None
    return_date: Optional[datetime.date] = None

# Schema used when creating a new Borrowed record (POST request).
class BorrowedCreate(BorrowedBase):
    pass