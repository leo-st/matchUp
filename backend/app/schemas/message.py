from typing import Optional, List

from pydantic import BaseModel, EmailStr, validator
from schemas.common import Pagination
from datetime import datetime

# Shared properties
class MessageSearch(BaseModel):
    pass
    
class MessageCreate(BaseModel):
    description: str
    sport_id: int
    
class MessageUpdate(BaseModel):
    id: str
    edit_timestamp : datetime = datetime.now()
    description: Optional[str] = None
    sport_id: Optional[int] = None
    likes : Optional[int] = None
    impacts: Optional[int] = None