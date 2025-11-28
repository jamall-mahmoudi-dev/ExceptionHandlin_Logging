
---

````markdown
# FastAPI Exception Handling Project

This project is a sample **FastAPI** application demonstrating:

- Building APIs with **FastAPI**.
- Connecting to a **PostgreSQL** database.
- Implementing **Exception Handling** and **User-Defined Exceptions**.
- Using **Logging** to track application events.

---

##  Prerequisites

- Python 3.11+
- PostgreSQL
- pip
- Virtual Environment (recommended)

---

##  Installation

1. **Clone or download the project**

```bash
git clone <repository-url>
cd fastapi_app
````

2. **Create and activate a virtual environment**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1   # Windows
# or
source venv/bin/activate       # Linux / macOS
```

3. **Install required packages**

```bash
pip install -r requirements.txt
```

> The `requirements.txt` includes: `fastapi`, `uvicorn[standard]`, `psycopg2-binary`, `sqlalchemy`, and `pydantic`.

---

##  Database Configuration

Add your PostgreSQL database information in `config.py` or a `.env` file:



> This project uses **SQLAlchemy** for PostgreSQL integration.

---

## Running the Project

1. Start the FastAPI server with Uvicorn:

```powershell
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

2. Access **Swagger UI** to test the API:

```
http://127.0.0.1:8000/docs
```

> Or use your network IP if testing from another device: `http://192.168.1.102:8000/docs`

---

##  Project Structure

```
fastapi_app/
│
├─ main.py          # Main FastAPI application
├─ models.py        # SQLAlchemy models
├─ database.py      # PostgreSQL connection setup
├─ schemas.py       # Pydantic schemas
├─ crud.py          # CRUD operations
├─ exceptions.py    # User-Defined Exceptions
├─ logger.py        # Logging configuration
├─ requirements.txt # Required packages
└─ README.md
```

---

##  Key Features

* **Exception Handling**:
  Includes `try-except`, `raise`, and custom exceptions for precise error control.

* **Logging**:
  All critical operations and errors are logged to a file for debugging and monitoring.

* **Database Operations**:
  Simple CRUD operations on PostgreSQL, with proper exception handling for database errors.

---

##  Testing the API

1. **Using Swagger UI**:

* Test POST/GET/PUT/DELETE endpoints.
* Observe exception messages and logging in action.

2. **Using CURL**:

```bash
curl -X GET "http://127.0.0.1:8000/users" -H "accept: application/json"
```

---

##  Possible Enhancements

* Add **Authentication (JWT)**.
* Implement **Async SQLAlchemy** for better performance.
* Send logs to external services (e.g., ELK Stack or Sentry).

---

##  References

* [FastAPI Documentation](https://fastapi.tiangolo.com/)
* [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
* [Python Logging Module](https://docs.python.org/3/library/logging.html)

