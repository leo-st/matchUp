from typing import List, Optional
from pydantic import BaseModel, EmailStr

class UserTokenPayload(BaseModel):
    user_id: int
    email: EmailStr
    username: str
    first_name: str
    last_name: str
    enabled: bool
    role_name: str
    permission_keys: List[str]
    
class UserLogin(BaseModel):
    username: str
    password: str

class UserCreate(BaseModel):
    username:str
    email: EmailStr
    first_name: Optional[str]
    last_name: Optional[str]
    enabled: Optional[bool]
    password: str
    role_id: str

class UserUpdate(BaseModel):
    password: Optional[str] = None
    role_id: Optional[str] = None