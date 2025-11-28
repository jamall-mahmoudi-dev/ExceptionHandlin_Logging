from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from schemas import UserCreate, UserResponse
from crud import create_user
from exceptions import InvalidAgeError, UsernameTakenError
from logger_config import logger

DATABASE_URL = "postgresql://bahram:bahram@192.168.1.102:5432/testdb"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        new_user = create_user(db, user.username, user.age)
        return new_user
    except InvalidAgeError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except UsernameTakenError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
