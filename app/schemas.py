from pydantic import BaseModel



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
    genre_id: int

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    class Config:
        orm_mode = True
