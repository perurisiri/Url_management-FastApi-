from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.db_config import get_session
from app.database.models.url_model import Url
from app.handlers.handler import success_response
from app.resources.url_res import UrlResponse
from app.services.database_service import DatabaseService, get_urls_by_filter
from app.validations.url_v import UrlCreate, UrlUpdate
from app.database.models.language_model import Language
from app.database.models.category_model import UrlCategory


router = APIRouter(prefix="/urls", tags=["URLs"])


@router.post("/", status_code=201)
def create_url( url_data: UrlCreate, db: Session = Depends(get_session),):
    service = DatabaseService(db, Url)
    url = service.create(url_data)

    return success_response(
        UrlResponse.model_validate(url).model_dump(mode="json"),
        "URL created successfully",
        201,
    )

@router.get("/")
def get_all_urls(language_id: int | None = None,category_id: int | None = None,
     db: Session = Depends(get_session),offset: int = 0,
    limit: int = 10,):

    urls = get_urls_by_filter( db,language_id, category_id, offset, limit,)
    
    '''urls = get_urls_by_filter(db, language_id, category_id)'''

    data = [
        UrlResponse.model_validate(url).model_dump(mode="json")
        for url in urls
    ]
    return success_response(data, "URLs retrieved successfully", 200)


@router.get("/{url_id}")
def get_url_by_id( url_id: int,db: Session = Depends(get_session),):
    service = DatabaseService(db, Url)
    url = service.get_by_id(url_id)

    if url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    return success_response(
        UrlResponse.model_validate(url).model_dump(mode="json"),
        "URL retrieved successfully",
        200,
    )


@router.put("/{url_id}")
def update_url(url_id: int,url_data: UrlUpdate,db: Session = Depends(get_session),):
    service = DatabaseService(db, Url)
    url = service.update(url_id, url_data)

    if url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    return success_response(
        UrlResponse.model_validate(url).model_dump(mode="json"),
        "URL updated successfully",
        200,
    )


@router.delete("/{url_id}")
def delete_url(url_id: int, db: Session = Depends(get_session),):
    service = DatabaseService(db, Url)
    deleted = service.delete(url_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="URL not found")
    return success_response(None, "URL deleted successfully", 200)