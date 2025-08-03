from sqlalchemy import Column, Integer, String
from .database import Base

class TestEntry(Base):
    __tablename__ = "test_entries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
