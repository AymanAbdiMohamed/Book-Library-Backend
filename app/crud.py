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

#Borrow/Return
def borrow_book(db: Session, borrow: schemas.BorrowedCreate):
    # can mark a book as borrowed.
        # - borrowed_ate defaults to today's date if not provided.
    
    borrowed_date = borrowed.borrowed_date or datetime.date.today()
    record = models.BorrowedBooks(
        user_id=borrowed.user_id,
        book_id=borrow.book_id,
        borrowed_date=borrowed_date
    )
    db.add(record)
    db.commit()
    return record

def return_book(db: Session, borrow: schemas.BorrowedCreate):
    # mark a borrowed book as returned.
    # - finds the matching borrow record and sets returned_date to today's date.
    rec = db.query(models.BorrowedBooks).filter(
        models.BorrowedBooks.user_id == borrowed.user_id,
        models.BorrowedBooks.book_id == borrowed.book_id
    ).first()

    if not rec:
        # no borrowed record found for this user/book
        return None
    
    rec.return_date = borrow.return_date or datetime.date.today()
    db.commit()
    return rec

def get_borrowed_for_user(db: Session, user_id: int):
    # ftech all borrowed-book records for a specific user
    return db.query(models.BorrowedBooks).filter(
        models.BorrowedBooks.user_id == user_id
    ).all()