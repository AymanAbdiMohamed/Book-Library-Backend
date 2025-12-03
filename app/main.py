from fastapi import FastAPI
from .routes import genres, books

app = FastAPI()

app.include_router(genres.routes)
app.include_router(books.routes)