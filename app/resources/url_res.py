from pydantic import BaseModel, ConfigDict
from datetime import datetime
from app.resources.language_res  import LanguageResponse
from app.resources.category_res  import CategoryResponse



class UrlResponse(BaseModel):
    id: int
    url: str
    title: str | None
    description: str | None
    language_id: int
    category_id: int
    #language: LanguageResponse       
    #category: CategoryResponse        
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)