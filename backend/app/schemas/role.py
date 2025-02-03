from typing import Optional, List

from pydantic import BaseModel, EmailStr, validator


# Shared properties
class RoleBase(BaseModel):
    pass

class RoleCreate(RoleBase):
    role_name: str
    permission_keys: list[str]

    @validator("role_name")
    def validate_role_name(cls, value):
        if not value.strip():
            raise ValueError("role_name cannot be empty")
        return value
    
    # @validator("permission_keys")
    # def validate_permission_keys(cls, value, values):
    #     # You can access other fields from 'values' if needed.
    #     role_name = values.get("role_name")

    #     sanitized_permission_keys = parse_permission_ids(input_permission_ids=value, db=get_db())

    #     if len(sanitized_permission_keys) == 0:
    #         raise ValueError(f"No valid permissions provided for role '{role_name}'")

    #     return sanitized_permission_keys

class RoleUpdate(RoleCreate):
    pass

class RoleRMQModel(BaseModel):
    role_id: int
    role_name: str

    def to_dict(self):
        return {
            'role_id': self.role_id,
            'role_name': self.role_name
        }
