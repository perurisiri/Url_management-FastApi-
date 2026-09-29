from pydantic import BaseModel,Field
from app.validations.baserequest import BaseRequestModel


class CategoryCreate(BaseRequestModel):
    name: str= Field(..., min_length=1)
    description: str | None  = None  

class CategoryUpdate(BaseModel):
    name: str | None = None
    description: str | None = None