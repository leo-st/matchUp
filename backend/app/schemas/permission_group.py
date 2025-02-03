from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class PermissionGroupBase(BaseModel):
    pass

class PermissionGroupCreate(PermissionGroupBase):
    pass

class PermissionGroupUpdate(PermissionGroupBase):
    pass