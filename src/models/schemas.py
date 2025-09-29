from pydantic import BaseModel
from typing import Optional

class NewsCreate(BaseModel):
    source_information: Optional[str] = None
    title: str
    summary: Optional[str] = None
    url_information: Optional[str] = None
    url_image: Optional[str] = None
