from datetime import timedelta
from schemas import token
from core import security
from core.settings import settings
from schemas.user import UserLogin
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any
from models import User
from core.dependencies import get_current_user, get_db
from fastapi.responses import JSONResponse
from core.dependencies import oauth2_scheme
from schemas.user import UserTokenPayload

from core import dependencies as deps
import crud
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/login")
async def authenticate(user: UserLogin, db: Session=Depends(get_db), ):
    """Verify login details and issue JWT in httpOnly cookie.

    Raises:
        HTTPException: 401 error if username or password are not recognised.
    """
    user = crud.user.authenticate(
        db, username=user.username, password=user.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not crud.user.is_active(user):
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
            subject=user.to_response_dict(), expires_delta=access_token_expires
        )
    response = JSONResponse({"message": "login successful"})
    response.set_cookie(key=oauth2_scheme.token_name, 
    value=access_token, 
    domain="" if settings.DEV_MODE else ".prognosix.ch" , 
    httponly=True, 
    samesite=settings.SAME_SITE, 
    secure=settings.JWT_COOKIE_SECURE
    )

    return response

@router.post("/logout")
async def logout(user: UserTokenPayload = Depends(get_current_user)):
    response = JSONResponse({"message": "logout successful"})
    response.delete_cookie("access_token")
    return response
