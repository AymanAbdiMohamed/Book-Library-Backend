from sqlalchemy.orm import Session
from . import models, schemas
import datetime


# Genre CRUD
def get_genres(db: Session):
    return db.query(models.Genre).all()


def create_genre(db: Session, genre: schemas.GenreCreate):
    db_genre = models.Genre(name=genre.name)
    db.add(db_genre)
    db.commit()
    db.refresh(db_genre)
    return db_genre


# Books
def get_books(db: Session):
    return db.query(models.Book).all()


def get_books_by_genre(db: Session, genre_id: int):
    return db.query(models.Book).filter(models.Book.genre_id == genre_id).all()


def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(
        title=book.title,
        author=book.author,
        pages=book.pages,
        genre_id=book.genre_id,
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


# Users
def get_users(db: Session):
    return db.query(models.User).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Borrow / Return
def borrow_book(db: Session, borrow: schemas.BorrowedCreate):
    borrowed_date = borrow.borrowed_date or datetime.date.today()
    record = models.BorrowedBooks(
        user_id=borrow.user_id,
        book_id=borrow.book_id,
        borrowed_date=borrowed_date,
        return_date=borrow.return_date,
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


def return_book(db: Session, borrow: schemas.BorrowedCreate):
    rec = (
        db.query(models.BorrowedBooks)
        .filter(
            models.BorrowedBooks.user_id == borrow.user_id,
            models.BorrowedBooks.book_id == borrow.book_id,
        )
        .first()
    )
    if not rec:
        return None

    rec.return_date = borrow.return_date or datetime.date.today()
    db.commit()
    db.refresh(rec)
    return rec


def get_borrowed_for_user(db: Session, user_id: int):
    return db.query(models.BorrowedBooks).filter(models.BorrowedBooks.user_id == user_id).all()