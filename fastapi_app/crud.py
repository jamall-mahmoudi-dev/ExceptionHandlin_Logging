from sqlalchemy.orm import Session
from models import User
from exceptions import InvalidAgeError, UsernameTakenError
from logger_config import logger

def create_user(db: Session, username: str, age: int):
    try:
        logger.info(f"Trying to create user: {username}, age: {age}")

        # بررسی username تکراری
        existing = db.query(User).filter(User.username == username).first()
        if existing:
            logger.warning(f"Username '{username}' already exists")
            raise UsernameTakenError(f"Username '{username}' is already taken.")

        # بررسی محدوده سن
        if age < 18 or age > 100:
            logger.warning(f"Invalid age provided: {age}")
            raise InvalidAgeError(age)

        user = User(username=username, age=age)
        db.add(user)
        db.commit()
        db.refresh(user)
        logger.info(f"User {username} created successfully")
        return user

    except (InvalidAgeError, UsernameTakenError) as e:
        db.rollback()
        logger.error(f"User creation failed: {e}")
        raise
    except Exception as e:
        db.rollback()
        logger.critical(f"Unexpected error: {e}")
        raise
    finally:
        db.close()
