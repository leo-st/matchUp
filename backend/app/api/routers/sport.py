from fastapi import APIRouter, Depends, HTTPException, Body, Response
from core.dependencies import get_current_user, get_db
from sqlalchemy.orm import Session
from schemas.user import UserTokenPayload
import traceback
from services.sport_service import get_all_sports, get_sport_by_id
router = APIRouter()

@router.get("/")
async def getAllSports(db: Session=Depends(get_db), auth: UserTokenPayload = Depends(get_current_user)):
    """
    Get's list of all sports in database.
    """
    try:
        res = get_all_sports(db=db)
        return res
    except Exception as e:
        print(traceback.format_exc())
        raise HTTPException(500, f"Error in /v1/feed/: {e}")
    
@router.get("/{id}")
async def getSportById(id:int, db: Session=Depends(get_db), auth: UserTokenPayload = Depends(get_current_user)):
    """
    Get sport by it's id.
    """
    try:
        res = get_sport_by_id(id=id, db=db)
        return res
    except Exception as e:
        print(traceback.format_exc())
        raise HTTPException(500, f"Error in /v1/feed/: {e}")