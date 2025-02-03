from typing import Optional
from sqlalchemy.orm import Session
from crud.base import CRUDBase
from models.permission_group import PermissionGroup
from schemas.permission_group import PermissionGroupCreate, PermissionGroupUpdate

class CRUDPermissionGroup(CRUDBase[PermissionGroup, PermissionGroupCreate, PermissionGroupUpdate]):
    def get_multi(self, db: Session) -> Optional[PermissionGroup]:
        return super().get_multi(db=db)

permissiongroup = CRUDPermissionGroup(PermissionGroup)