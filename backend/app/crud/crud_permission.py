from typing import Optional, List
from sqlalchemy.orm import Session
from crud.base import CRUDBase
from models.permission import Permission
from schemas.permission import PermissionCreate, PermissionUpdate

class CRUDPermission(CRUDBase[Permission, PermissionCreate, PermissionUpdate]):
    def get_multi(self, db: Session) -> Optional[Permission]:
        return super().get_multi(db=db)
    
    def get_multi_with_filter_by_permission_ids(self, db:Session, permission_ids: List[str]) -> List[Permission]:
        return db.query(self.model).filter(self.model.permission_id.in_(permission_ids)).all()

permission = CRUDPermission(Permission)