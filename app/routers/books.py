from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..import schemas, models, crud
from ..departments import get_db

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