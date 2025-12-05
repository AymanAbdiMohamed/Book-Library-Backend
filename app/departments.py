# Import the SessionLocal class you created in database.py.
# SessionLocal is a function that creates a new database session each time it is called.
from .database import SessionLocal

# Import the Session type for type-hinting (optional but useful).
from sqlalchemy.orm import Session

# FastAPI's Depends is used for dependency injection.
from fastapi import Depends


def get_db():
    """
    Dependency that provides a database session.

    This function is used in FastAPI routes to automatically create
    a new database session for each request, and then close it when
    the request is finished.
    """
    # Create a new database session
    db = SessionLocal()

    try:
        # `yield` makes this function a generator dependency.
        # FastAPI will give this database session to the path operation
        # and then return here once the request is processed.
        yield db
    finally:
        # This code runs after the request is done.
        # It ensures the database session is CLOSED even if an error occurs.
        db.close()
