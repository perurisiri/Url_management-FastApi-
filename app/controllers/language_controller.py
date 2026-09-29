from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.config.db_config import get_session
from app.database.models.language_model import Language
from app.handlers.handler import success_response
from app.resources.language_res import LanguageResponse
from app.services.database_service import DatabaseService
from app.validations.language_v import LanguageCreate, LanguageUpdate


router = APIRouter(prefix="/languages", tags=["Languages"])


@router.post("/", status_code=201)
def create_language( language_data: LanguageCreate,db: Session = Depends(get_session),):
    service = DatabaseService(db, Language)
    language = service.create(language_data)

    return success_response(
        LanguageResponse.model_validate(language).model_dump(mode="json"),
        "Language created successfully",
        201,
    )


@router.get("/")
def get_all_languages(offset: int = 0,
    limit: int = 10,db: Session = Depends(get_session)):
    service = DatabaseService(db, Language)
    languages = service.get_all(offset=offset,limit=limit)

    data = [
        LanguageResponse.model_validate(language).model_dump(mode="json")
        for language in languages
    ]
    return success_response(data, "Languages retrieved successfully", 200)


@router.get("/{language_id}")
def get_language_by_id(
    language_id: int,
    db: Session = Depends(get_session),
):
    service = DatabaseService(db, Language)
    language = service.get_by_id(language_id)

    if language is None:
        raise HTTPException(status_code=404, detail="Language not found")

    return success_response(
        LanguageResponse.model_validate(language).model_dump(mode="json"),
        "Language retrieved successfully",
        200,
    )


@router.put("/{language_id}")
def update_language(
    language_id: int,
    language_data: LanguageUpdate,
    db: Session = Depends(get_session),
):
    service = DatabaseService(db, Language)
    language = service.update(language_id, language_data)

    if language is None:
        raise HTTPException(status_code=404, detail="Language not found")

    return success_response(
        LanguageResponse.model_validate(language).model_dump(mode="json"),
        "Language updated successfully",
        200,
    )


@router.delete("/{language_id}")
def remove_language(
    language_id: int,
    db: Session = Depends(get_session),
):
    service = DatabaseService(db, Language)
    #try:
    deleted = service.delete(language_id)
    #except IntegrityError:
     #   db.rollback()
      #  raise HTTPException(status_code=409,detail="Cannot delete language id while URLs are linked to it",)

    if not deleted:
        raise HTTPException(status_code=404, detail="Language not found")

    return success_response(None, "Language deleted successfully", 200)