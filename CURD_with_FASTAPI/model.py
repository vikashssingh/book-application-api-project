

from sqlalchemy import Boolean, Column, Integer, String
from db_handler import Base


class Books(Base):
    """
    This is a model class. which is having the movie table structure with all the constraint
    """
    __tablename__ = "book"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    book_id = Column(String, unique=True, index=True, nullable=False)
    book_name = Column(String(255), index=True, nullable=False)
    director = Column(String(100), index=True, nullable=False)
    geners = Column(String, index=True, nullable=False)
    membership_required = Column(Boolean, nullable=False, default=True)
    cast = Column(String(255), index=True, nullable=False)
    streaming_platform = Column(String, index=True)
