from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, models
from ..departments import get_db

# router for all user-related endpoints
# prefix: "/users" -> all routes begin with /users
# tags:["users"] -> groups endpoints in the API docs
router = APIRouter(
    prefix="/users",
    tags=["users"],
)