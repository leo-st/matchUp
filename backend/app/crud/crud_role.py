from typing import List, Optional

from sqlalchemy.orm import Session
from crud.base import CRUDBase
from models.role import Role
from schemas.role import RoleCreate, RoleUpdate


class CRUDRole(CRUDBase[Role, RoleCreate, RoleUpdate]):
    def get(self, db: Session, role_id: int) -> Optional[Role]:
        return db.query(Role).filter(Role.role_id==role_id).first()
    
    def get_by_name(self, db: Session, *, role_name: str) -> Optional[Role]:
        return db.query(Role).filter(Role.role_name == role_name).first()

    def get_multi(self, db: Session) -> List[Role]:
        return super().get_multi(db=db)
    
    def create(self, db: Session, *, obj_in: Role) -> Role:
        db.add(obj_in)
        db.commit()
        db.refresh(obj_in)
        return obj_in

    def update(self, db:Session, obj_in:Role, role_name, permissions) -> Role:
        obj_in.role_name=role_name
        obj_in.permissions = permissions
        db.commit()
        db.refresh(obj_in)
        return obj_in
    
    def delete(self, db:Session, db_obj:Role):
        db.delete(db_obj)
        db.commit()
        return

role = CRUDRole(Role)