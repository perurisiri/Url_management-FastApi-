
from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.database.models.url_model import Url
from app.database.models.category_model import UrlCategory
from app.database.models.language_model import Language
from psycopg2.errors import UniqueViolation
 

class DatabaseService:
    def __init__(self, db: Session, model):
        self.db = db
        self.model = model
        
    def create(self, data: BaseModel):
        if self.model is Url:
            if self.db.get(Language, data.language_id) is None:
                raise HTTPException(status_code=422, detail="Language ID does not exist")
            if self.db.get(UrlCategory, data.category_id) is None:
                raise HTTPException(status_code=422, detail="Category ID does not exist")
        item = self.model(**data.model_dump())
        self.db.add(item)

        try:
            self.db.commit()
        except IntegrityError as exc:
            self.db.rollback()
            #if isinstance(exc.orig, UniqueViolation):
             #  raise HTTPException(status_code=409,detail="This record already exists",
            #) from exc

            raise

        self.db.refresh(item)
        return item

    '''def get_all(self ):
        return self.db.query(self.model).all()'''
    def get_all(self, offset: int = 0, limit: int = 10):
        return ( self.db.query(self.model).offset(offset).limit(limit).all())

    def get_by_id(self, item_id: int):
        return self.db.get(self.model, item_id)

    def update(self, item_id: int, data: BaseModel):
        item = self.get_by_id(item_id)

        if item is None:
            return None

        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(item, key, value)

        self.db.commit()
        self.db.refresh(item)
        return item

    def delete(self, item_id: int):
        item = self.get_by_id(item_id)

        if item is None:
            return False

        self.db.delete(item)
        try:
            self.db.commit()
        except IntegrityError:
            self.db.rollback()
            raise

        return True
        


def get_urls_by_filter(db: Session,language_id: int | None = None,category_id: int | None = None,offset: int = 0,
    limit: int = 10,):
    query = db.query(Url)

    if language_id is not None:
        query = query.filter(Url.language_id == language_id)

    if category_id is not None:
        query = query.filter(Url.category_id == category_id)

    return query.offset(offset).limit(limit).all()
    