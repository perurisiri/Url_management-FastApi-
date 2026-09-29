from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.database.models.base import Base


class Language(Base):
    __tablename__ = "language"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False,unique=True)
    code = Column(String, unique=True, nullable=False, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    