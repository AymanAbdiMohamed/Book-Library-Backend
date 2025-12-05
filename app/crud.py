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
    db.add(db_genre)
    db.commit()
    db.refresh(db_genre)
    return db_genre
