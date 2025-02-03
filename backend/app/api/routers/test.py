from fastapi import APIRouter, Depends, HTTPException, Body, Response
from core.dependencies import get_current_user, get_db
from sqlalchemy.orm import Session
from schemas.user import UserTokenPayload
import traceback
from services.test_service import get_simple_test_text
router = APIRouter()

@router.get("/")
async def test_enpdpoint(db: Session=Depends(get_db), auth: UserTokenPayload = Depends(get_current_user)):
    """
    Returns 'test' as output.
    """
    try:
        res = get_simple_test_text()
        return res
    except Exception as e:
        print(traceback.format_exc())
        raise HTTPException(500, f"Error in /v1/test/: {e}")
    