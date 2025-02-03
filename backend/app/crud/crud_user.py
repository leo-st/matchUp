from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from core.security import get_password_hash, verify_password
from crud.base import CRUDBase
from models.user import User
from schemas.user import UserCreate, UserUpdate

class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()
    
    def get_by_username(self, db: Session, *, username: str) -> Optional[User]:
        return db.query(User).filter(User.username == username).first()

    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        db_obj = User(
            username=obj_in.username,
            email=obj_in.email,
            first_name =obj_in.first_name,
            last_name = obj_in.last_name,
            enabled = obj_in.enabled,
            welcome_message = obj_in.welcome_message,
            pw_hash=get_password_hash(obj_in.password),
            role_id = obj_in.role_id
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]
    ) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)
        if(update_data.__contains__("password")):
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["pw_hash"] = hashed_password
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def authenticate(self, db: Session, *, username: str, password: str) -> Optional[User]:
        user = self.get_by_username(db, username=username)
        if not user:
            return None
        if not verify_password(password, user.pw_hash):
            return None
        return user

    def is_active(self, user: User) -> bool:
        return user.enabled

    # def is_superuser(self, user: User) -> bool:
    #     return user.is_superuser
    def delete(self, db:Session, db_obj:User):
        db.delete(db_obj)
        db.commit()
        return

user = CRUDUser(User)