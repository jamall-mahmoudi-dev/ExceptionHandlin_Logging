from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    age: int

class UserResponse(BaseModel):
    id: int
    username: str
    age: int

    class Config:
        orm_mode = True
