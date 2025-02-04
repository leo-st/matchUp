from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from core.security import get_password_hash, verify_password
from crud.base import CRUDBase
from models.feed import Feed
from schemas.feed import FeedCreate, FeedUpdate
from datetime import datetime

class CRUDFeed(CRUDBase[Feed, FeedCreate, FeedUpdate]):
    def get_by_id(self, db: Session, *, id: str) -> Optional[Feed]:
        return db.query(Feed).filter(Feed.id == id).first()

    def create(self, db: Session, *, obj_in: FeedCreate, user_id: int) -> Feed:
        db_obj = Feed(
            creation_timestamp=datetime.now(),
            user_id=user_id,
            description =obj_in.description,
            sport_id = obj_in.sport_id
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Feed, obj_in: Union[FeedUpdate, Dict[str, Any]]
    ) -> Feed:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)


    def delete(self, db:Session, db_obj:Feed):
        db.delete(db_obj)
        db.commit()
        return

feed = CRUDFeed(Feed)