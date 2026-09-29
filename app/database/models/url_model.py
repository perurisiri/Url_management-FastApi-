from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database.models.base import Base


class Url(Base):
    __tablename__ = "url"

    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False,unique=True)
    title = Column(String, nullable=True)
    description = Column(String, nullable=True)
    language_id = Column(Integer, ForeignKey("language.id"), nullable=False,index=True)
    category_id = Column(Integer, ForeignKey("url_category.id"), nullable=False,index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    language = relationship("Language")
    category = relationship("UrlCategory")