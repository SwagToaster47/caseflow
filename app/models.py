from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base

class Case(Base):
    __tablename__ = "cases"

    id = Column(Integer, primary_key = True, index = True)
    case_number = Column(String, unique = True, index = True)
    title = Column(String)
    status = Column(String, default="open")
    created_at = Column(DateTime, default=datetime.utcnow)

