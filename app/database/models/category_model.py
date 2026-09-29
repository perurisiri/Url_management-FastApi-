from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.database.models.base import Base


class UrlCategory(Base):
    __tablename__ = "url_category"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False,unique=True)
    description = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    