# FlyRank Internship - Assignment 1: CRUD API with FastAPI

A production-grade RESTful API service built as part of the FlyRank AI Backend Engineering Internship. Demonstrates modular FastAPI application structure, PostgreSQL database integration, and strict Pydantic data models.

## 🚀 Tech Stack

- **Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Validation:** Pydantic v2
- **Server:** Uvicorn
- **Language:** Python 3.10+

## ✨ Key Features

- **Modular Architecture:** Clean separation of routes, schemas, models, and database dependencies.
- **PostgreSQL Integration:** Dynamic database connections with connection pooling.
- **Data Integrity:** Strict input/output payload validation via Pydantic schemas.
- **Interactive OpenAPI Specs:** Swagger UI available out of the box at `/docs`.

## 🛠️ Setup & Running Locally

### 1. Clone & Navigate
```bash
git clone https://github.com/RayyanAHR/FlyRank-Internship---CRUD-API-thru-FastAPI.git
cd FlyRank-Internship---CRUD-API-thru-FastAPI

```

### 2. Set up Virtual Environment

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

### 4. Environment Configuration

Create a `.env` file in the root directory:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/dbname

```

### 5. Start the Server

```bash
uvicorn app.main:app --reload

```

Open `[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)` in your browser to view and test endpoints interactively.

```

Once you hit **Commit changes**, GitHub will display it formatted cleanly on your project page[cite: 3]!

```
