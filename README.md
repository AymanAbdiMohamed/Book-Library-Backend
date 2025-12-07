# Book Library Backend

A FastAPI-based REST API for managing a digital book library. This backend handles genres, books, users, and borrowing functionality.

## Features

- 📚 **Genre Management** - Create and list book genres
- 📖 **Book Management** - Add, list, and filter books by genre
- 👥 **User Management** - Manage library users
- 🔄 **Borrowing System** - Track book borrowing and returns
- 🔐 **CORS Support** - Configured for cross-origin requests from the frontend
- 📋 **API Documentation** - Interactive Swagger/OpenAPI docs

## Tech Stack

- **Framework**: FastAPI
- **Server**: Uvicorn
- **Database**: SQLite with SQLAlchemy ORM
- **Migration Tool**: Alembic
- **Validation**: Pydantic

## Prerequisites

- Python 3.8+
- pip or pipenv

## Installation

### 1. Clone or navigate to the project
```bash
cd Book-Library-Backend
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install fastapi uvicorn sqlalchemy pydantic alembic
```

Or using Pipfile:
```bash
pipenv install
```

## Project Structure

```
Book-Library-Backend/
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI app initialization
│   ├── database.py       # Database connection setup
│   ├── models.py         # SQLAlchemy ORM models
│   ├── schemas.py        # Pydantic validation schemas
│   ├── crud.py          # Database CRUD operations
│   ├── deps.py          # Dependency injection
│   └── routers/
│       ├── genres.py    # Genre endpoints
│       ├── books.py     # Book endpoints
│       └── users.py     # User endpoints
├── migrations/           # Alembic database migrations
├── alembic.ini          # Alembic configuration
├── Pipfile              # Dependencies
└── README.md
```

## Running the Server

### Development Mode (with auto-reload)
```bash
source venv/bin/activate
uvicorn app.main:app --reload
```

The server will start on `http://localhost:8000`

### Production Mode
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

## API Documentation

Once the server is running, access the interactive API docs:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### Genres
- `GET /genres/` - List all genres
- `POST /genres/` - Create a new genre

### Books
- `GET /books/` - List all books
- `POST /books/` - Create a new book
- `GET /books/genre/{genre_id}` - Get books by genre

### Users
- `POST /users/` - Create a new user

### Borrowing
- `POST /borrow/` - Borrow a book

## Database

### Initialize Database
The database is automatically created on first run. Tables are created via SQLAlchemy's `Base.metadata.create_all()`.

### Run Migrations (Optional)
```bash
alembic upgrade head
```

## CORS Configuration

The API is configured to accept requests from:
- `http://localhost:3000` (React frontend)

Update `app/main.py` to allow additional origins if needed.

## Environment Variables

You can set the following environment variables:

```bash
DATABASE_URL=sqlite:///./library.db
API_PORT=8000
```

## Common Issues

### Pydantic V2 Warning
If you see a warning about `orm_mode` being deprecated:
```
UserWarning: Valid config keys have changed in V2:
* 'orm_mode' has been renamed to 'from_attributes'
```

This is just a deprecation notice and won't affect functionality. To fix it, update `schemas.py`:
```python
class Config:
    from_attributes = True  # Instead of orm_mode = True
```

### Port Already in Use
If port 8000 is already in use:
```bash
uvicorn app.main:app --reload --port 8001
```

## Testing the API

### Create a Genre
```bash
curl -X POST http://localhost:8000/genres/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Fiction"}'
```

### Create a Book
```bash
curl -X POST http://localhost:8000/books/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "pages": 180,
    "genre_id": 1
  }'
```

### List All Books
```bash
curl http://localhost:8000/books/
```

## Contributing

1. Create a new branch for your feature
2. Make your changes
3. Test the API using the Swagger docs
4. Submit a pull request

## License

MIT License
