from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, models
from ..deps import get_db

# Router for all user-related endpoints
# prefix="/users" → all routes begin with /users
# tags=["users"] → groups endpoints in the API docs
router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user account.

    Steps:
    1. Check if a user with the same email already exists.
    2. If yes → return a 400 error.
    3. Otherwise → create the user via the CRUD layer.
    """

    # Check if email is already registered
    existing = db.query(models.User).filter(models.User.email == user.email).first()

    if existing:
        # Prevent duplicate accounts
        raise HTTPException(status_code=400, detail="Email already registered")

    # Delegate user creation to the CRUD layer
    return crud.create_user(db, user)


@router.get("/", response_model=list[schemas.User])
def list_users(db: Session = Depends(get_db)):
    """
    List all users in the system.
    
    Simply fetches all user records via CRUD.
    """
    return crud.get_users(db)


@router.post("/borrow", response_model=schemas.BorrowedBase)
def borrow_book(borrow: schemas.BorrowedCreate, db: Session = Depends(get_db)):
    """
    Mark a book as borrowed by a user.

    Steps:
    1. Check that both the user_id and book_id exist.
    2. If either is missing → return a 400 error.
    3. Otherwise → create a borrow record via CRUD.
    """

    # Validate that the user exists
    user = db.query(models.User).filter(models.User.id == borrow.user_id).first()

    # Validate that the book exists
    book = db.query(models.Book).filter(models.Book.id == borrow.book_id).first()

    if not user or not book:
        raise HTTPException(status_code=400, detail="User or Book not found")

    # Create borrow record through CRUD
    return crud.borrow_book(db, borrow)


@router.post("/return", respomse_model=schemas.BorrowedBase)
def return_book(borrow: schemas.BorrowedCreate, db: Session = Depends(get_db)):
    """
    Mark a borrowed book as returned by a user.
    - This looks up the borrow record.
    - If record does not exist -> 404 error.
    - Otherwise -> delete the borrow record via CRUD.
    """
    rec = crud.return_book(db, borrow)

    if not rec:
        raise HTTPException(status_code=404, detail="Borrow record not found")
    
    return rec


@router.get("/{user_id}}/borrowed", response_model=list[schemas.BorrowedBase])
