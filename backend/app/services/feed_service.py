from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.feed import Feed
from schemas.feed import FeedSearch, FeedCreate, FeedUpdate
import crud

def get_feed_by_id(feed_id:str, db: Session):
    try:
        feed = db.query(Feed).filter(Feed.id == feed_id).one()
        return feed.to_response_dict()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"There was an error in get_feeds_by_id! {e}")
    
def get_feeds_by_sports(filters: FeedSearch, db: Session):
    try:
        # Query the Feed table with filters and pagination
        feeds = (
            db.query(Feed)
            .filter(Feed.sport_id.in_(filters.sport_ids))  # Filter by the list of Sport IDs
            .order_by(Feed.creation_timestamp.desc())  # Optional: Order by creation timestamp
            .offset(filters.pagination.page_num*filters.pagination.page_size)  # Skip records for pagination
            .limit(filters.pagination.page_size)     # Limit the number of records per page
            .all()
        )

        # Convert the results to a list of dictionaries using the to_response_dict method
        feeds_data = [feed.to_response_dict() for feed in feeds]
        return feeds_data
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"There was an error in get_feeds_by_sports! {e}")
    
def create_feed(new_feed: FeedCreate, user_id:int,  db: Session):
    try:
        feed = crud.feed.create(db=db, obj_in=new_feed, user_id=user_id)
        return feed
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"There was an error in create_feed! {e}")
    
def update_feed(update_feed: FeedUpdate, user_id:int,  db: Session):
    try:
        if(crud.feed.get_by_id(db=db, id=update_feed.id)):
            feed = crud.feed.update(db=db, obj_in=update_feed, user_id=user_id)
            return feed
        else:
            raise Exception(f"Feed with id: {update_feed.id} doesn't exist")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"There was an error in update_feed! {e}")