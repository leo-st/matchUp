from typing import Optional, List

from pydantic import BaseModel, EmailStr, validator
from schemas.common import Pagination
from datetime import datetime

# Shared properties
class FeedSearch(BaseModel):
    sport_ids : Optional[List[int]] =  None
    pagination: Optional[Pagination] = None
    
class FeedCreate(BaseModel):
    description: str
    sport_id: int
    
class FeedUpdate(BaseModel):
    id: str
    edit_timestamp : datetime = datetime.now()
    description: Optional[str] = None
    sport_id: Optional[int] = None
    likes : Optional[int] = None
    impacts: Optional[int] = None