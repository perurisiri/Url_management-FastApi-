from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.config.db_config import get_session
from app.database.models.category_model import UrlCategory
from app.handlers.handler import success_response
from app.resources.category_res import CategoryResponse
from app.services.database_service import DatabaseService
from app.validations.category_v import CategoryCreate, CategoryUpdate


router = APIRouter(prefix="/categories", tags=["Categories"])


@router.post("/")
def create_category(category_data: CategoryCreate,db: Session = Depends(get_session),):
    service = DatabaseService(db, UrlCategory)
    category = service.create(category_data)

    return success_response(CategoryResponse.model_validate(category).model_dump(mode="json"),
        "Category created successfully",
        201,
    )


@router.get("/")
def get_all_categories( offset: int = 0,
    limit: int = 10,db: Session = Depends(get_session)):
    service = DatabaseService(db, UrlCategory)
    categories = service.get_all(offset=offset,limit=limit)

    data = [
        CategoryResponse.model_validate(category).model_dump(mode="json")
        for category in categories
    ]
    return success_response(data, "Categories retrieved successfully", 200)


@router.get("/{category_id}")
def get_category_by_id(category_id: int, db: Session = Depends(get_session),):
    service = DatabaseService(db, UrlCategory)
    category = service.get_by_id(category_id)

    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")

    return success_response(
        CategoryResponse.model_validate(category).model_dump(mode="json"),
        "Category retrieved successfully",
        200,
    )


@router.put("/{category_id}")
def update_category(category_id: int,category_data: CategoryUpdate,db: Session = Depends(get_session),):
    service = DatabaseService(db, UrlCategory)
    category = service.update(category_id, category_data)

    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")

    return success_response(
        CategoryResponse.model_validate(category).model_dump(mode="json"),
        "Category updated successfully",
        200,
    )


@router.delete("/{category_id}")
def delete_category( category_id: int,db: Session = Depends(get_session),):
    service = DatabaseService(db, UrlCategory)
    deleted = service.delete(category_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Category not found")
    return success_response(None, "Category deleted successfully", 200)