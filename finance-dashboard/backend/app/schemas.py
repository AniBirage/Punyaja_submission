from pydantic import BaseModel
from enum import Enum

class UserRole(str, Enum):
    admin = "admin"
    user = "user"

# User creation schema
class UserCreate(BaseModel):
    username: str
    password: str
    role: UserRole = UserRole.user  # Default role is 'user'

# User response schema
class User(BaseModel):
    username: str
    role: UserRole

    class Config:
        orm_mode = True

# Finance data schema
class FinanceDataCreate(BaseModel):
    category: str
    amount: int
    date: str

class FinanceData(BaseModel):
    id: int
    category: str
    amount: int
    date: str

    class Config:
        orm_mode = True
