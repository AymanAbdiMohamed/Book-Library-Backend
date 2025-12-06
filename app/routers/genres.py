from fastapi imort APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..departments import get_db

# router fro all genre-related endpoints
# prefix: "/genres" means every endpoint here will start with /genres
# tags=["genres"] is used in the API docs to group these endpoints


router = APIRouter(
    prefix="/genres",
    tags=["genres"],
)
