from typing import Optional, List

from pydantic import BaseModel, EmailStr, validator


# Shared properties
class Pagination(BaseModel):
    page_num : Optional[int] =  0
    page_size: Optional[int] = 10
    