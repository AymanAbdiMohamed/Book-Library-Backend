from sqlalchemy.orm import Session
from . import models, schemas
import datetime

#Genre
def get_genres(db: Session):
    # fetch all genre from the database
    return db.query(models.Genre).all()

def create_genre(db: Session, genre: schemas.GenreCreate):
    # create a new genre using data from GenreCreate schema
    db_genre = models.Genre(name=genre.name)
    db.add(db_genre) # add new genre object to the database session
    db.commit() # commit transaction to save to DB
    db.refresh(db_genre) # refresh object with DB-generated fields; such as id
    return db_genre

#Books
def get_books(db: Session):
    return db.query(models.Books).all()

de create_book(db: Session, book: schemas.BookCreate):
    # create a new book entry
    db_book = models.Boook(
        title=book.title,
        author=book.author,
        pages=book.pages,
        genre_id=book.genre_id
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

#Users
def get_users(db: Session):
    # fetch all users from the system
    return db.query(models.Users).all()

def create_user(db: Session, user: schemas.UserCreate):
    # create a new user with name and email
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user