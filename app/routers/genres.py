from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..deps import get_db

# Router for all genre-related endpoints.
# prefix="/genres" means every endpoint here starts with /genres
# tags=["genres"] is used in the API docs grouping
router = APIRouter(prefix="/genres", tags=["genres"])


@router.post("/", response_model=schemas.Genre)
def create_genre(genre: schemas.GenreCreate, db: Session = Depends(get_db)):
    """
    Create a new genre.

    - `genre`: Pydantic schema containing the new genre's name.
    - `db`: SQLAlchemy session obtained from dependency injection.
    
    Steps:
    1. Fetch all genres from DB.
    2. Check if a genre with the same name already exists (case-insensitive).
    3. If exists → return a 400 error.
    4. Otherwise → create and return the new genre.
    """
    # List comprehension to check if name already exists
    existing = [g for g in crud.get_genres(db) if g.name.lower() == genre.name.lower()]

    if existing:
        # Raise an error if genre is duplicated
        raise HTTPException(status_code=400, detail="Genre already exists")

    # Create genre in DB through CRUD layer
    return crud.create_genre(db, genre)


@router.get("/", response_model=list[schemas.Genre])
def list_genres(db: Session = Depends(get_db)):
    """
    Return a list of all genres in the database.

    - `db`: SQLAlchemy session.
    - Uses the CRUD layer to fetch all genres.
    """
    return crud.get_genres(db)


@router.delete("/{genre_id}", response_model=schemas.Genre)
def delete_genre(genre_id: int, db: Session = Depends(get_db)):
    """
    Delete a genre by ID.

    - `genre_id`: The ID of the genre to delete.
    - `db`: SQLAlchemy session.
    
    Returns the deleted genre or raises a 404 error if not found.
    """
    deleted_genre = crud.delete_genre(db, genre_id)
    
    if not deleted_genre:
        raise HTTPException(status_code=404, detail="Genre not found")
    
    return deleted_genre
