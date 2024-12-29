from sqlalchemy import Column, Integer, String, Enum
from .database import Base
import enum

# Define roles using Enum
class UserRole(enum.Enum):
    admin = "admin"
    user = "user"

# User Model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(Enum(UserRole), default=UserRole.user)  # Default to 'user'

class FinanceData(Base):
    __tablename__ = "finance_data"
    id = Column(Integer, primary_key=True, index=True)
    category = Column(String)
    amount = Column(Integer)
    date = Column(String)
