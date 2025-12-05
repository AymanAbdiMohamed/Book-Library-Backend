from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


# Initialize FastAPI application
app = FastAPI(
    title="Book Library API",
    description="A RESTful API for managing a book library",
    version="1.0.0"
)

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to Book Library API"}


# check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}