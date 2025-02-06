from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.feed import Feed
from models.messages import ChatGroup, ChatGroupUsers, Message
from schemas.message import MessageSearch, MessageSearch, MessageUpdate
import crud

def enter_chatgroup(feed_id: str, user_id:int,  db: Session):
    try:
        # check if feed exists
        feed = db.query(Feed).filter(Feed.id==feed_id).first()
        if(feed is not None):
            # check if chatgroup already exist
            pass
        else:
            raise Exception(f"Feed with id:{feed_id} does not exist!")
        return feed
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"There was an error in create_feed! {e}")

def create_message(new_message: MessageSearch, user_id:int,  db: Session):
    try:
        feed = crud.feed.create(db=db, obj_in=new_feed, user_id=user_id)
        return feed
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"There was an error in create_feed! {e}")