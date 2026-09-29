from pydantic import BaseModel
from app.validations.baserequest import BaseRequestModel


class LanguageCreate(BaseRequestModel):
    name: str
    code: str


class LanguageUpdate(BaseModel):
    name: str | None = None
    code: str | None = None