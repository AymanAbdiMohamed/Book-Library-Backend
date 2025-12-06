from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .. import schemas, models, crud
from ..deps import get_db

# router for all book-related endpoints
# prefix="/books" -> every endpoint starts with /books
# tags=["books"] -> groups endpoints under "books" in the documentation

router = APIRouter(
    prefix="/books",
    tags=["books"]
)

@router.post("/", response_model=schemas.Book)
def create_books(book: schemas.BookCreate, db: Session = Depends(get_db)):
    """
    Create a new book in the library.
    """
    genre = db.query(models.Genre).filter(models.Genre.id == book.genre_id).first()
    if not genre:
        # raise an error if the genre_id is invalid
        raise HTTPException(status_code=400, detail="Genre not found")
    # pass the data to the CRUD function to create the new book
    return crud.create_book(db=db, book=book)

@router.get("/", response_model=list[schemas.Book])
def list_books(db: Session = Depends(get_db)):
    # return a list of all books in the database
    # simpliy calls the CRUD layer to fetch all records
    return crud.get_books(db)

@router.get("/genre/{genre_id}", response_model=list[schemas.Book])
def book_by_genre(genre_id: int, db: Session = Depends(get_db)):
    # Return all books that belong to a specific genre
    # genre_id: the ID of the genre to filter books by
    # delegates the filtering logic to the CRUD layer
    return crud.get_books_by_genre(db, genre_id=genre_id)