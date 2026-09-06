import enum
from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum
from app.db.base import Base

class UserRole(str, enum.Enum):
    CUSTOMER = "customer"
    VENDOR = "vendor"
    ADMIN = "admin"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(Enum(UserRole), default=UserRole.CUSTOMER, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)