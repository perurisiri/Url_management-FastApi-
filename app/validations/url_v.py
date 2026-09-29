from pydantic import BaseModel,Field
from app.validations.baserequest import BaseRequestModel


class UrlCreate(BaseRequestModel):
    url: str
    title: str | None = None
    description: str | None = None
    language_id: int=Field(gt=0)
    category_id: int=Field(gt=0)


class UrlUpdate(BaseModel):
    url: str | None = None
    title: str | None = None
    description: str | None = None
    language_id: int | None = None
    category_id: int | None = None