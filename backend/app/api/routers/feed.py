from fastapi import APIRouter, Depends, HTTPException, Body, Response
from core.dependencies import get_current_user, get_db
from sqlalchemy.orm import Session
from schemas.user import UserTokenPayload
import traceback
from schemas.feed import FeedCreate, FeedUpdate, FeedSearch
from services.feed_service import get_feed_by_id, get_feeds_by_sports, create_feed, update_feed
router = APIRouter()

@router.post("/")
async def createFeed(new_feed:FeedCreate, db: Session=Depends(get_db), auth: UserTokenPayload = Depends(get_current_user)):
    """
    Creates new feed.
    """
    try:
        res = create_feed(new_feed=new_feed, db=db,user_id=auth.user_id)
        return res
    except Exception as e:
        print(traceback.format_exc())
        raise HTTPException(500, f"Error in /v1/feed/: {e}")
    
@router.put("/")
async def updateFeed(feed:FeedUpdate, db: Session=Depends(get_db), auth: UserTokenPayload = Depends(get_current_user)):
    """
    Update existing feed.
    """
    try:
        res = update_feed(update_feed=feed, db=db,user_id=auth.user_id)
        return res
    except Exception as e:
        print(traceback.format_exc())
        raise HTTPException(500, f"Error in /v1/feed/: {e}")
    
@router.post("/get-by-sports")
async def getFeedsBySports(filters:FeedSearch, db: Session=Depends(get_db), auth: UserTokenPayload = Depends(get_current_user)):
    """
    Get paginatated feeds by selected sports.
    """
    try:
        res = get_feeds_by_sports(filters=filters, db=db)
        return res
    except Exception as e:
        print(traceback.format_exc())
        raise HTTPException(500, f"Error in /v1/feed/: {e}")
    
@router.get("/{id}")
async def getFeedById(id:str, db: Session=Depends(get_db), auth: UserTokenPayload = Depends(get_current_user)):
    """
    Get feed by it's id.
    """
    try:
        res = get_feed_by_id(feed_id=id, db=db)
        return res
    except Exception as e:
        print(traceback.format_exc())
        raise HTTPException(500, f"Error in /v1/feed/: {e}")
   