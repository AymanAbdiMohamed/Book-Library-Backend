from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import genres, books, users
from .database import Base, engine

# Create all database tables automatically.
# This is useful in development when you're NOT running Alembic migrations.
# In production, you normally remove this and rely on Alembic instead.
Base.metadata.create_all(bind=engine)

# Initialize the FastAPI application with a custom title
app = FastAPI(title="Book Library API")

# Enable CORS (Cross-Origin Resource Sharing)
# This allows your React frontend (localhost:3000) to call the API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allowed frontend origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, PUT, DELETE...)
    allow_headers=["*"],  # Allow all custom headers
)

# Register all routers (genres, books, users)
# These handle the API endpoints under /genres, /books, /users
app.include_router(genres.router)
app.include_router(books.router)
app.include_router(users.router)

@app.get("/")
def root():
    """
    Root endpoint for testing the API.
    Returns a simple JSON message confirming the API is running.
    """
    return {"message": "Book Library API running"}
