from typing import Generator

from fastapi import Depends, HTTPException, status, Request, WebSocket
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from schemas import token as tokens
from core import security
from core.settings import settings
from db.sessions import SessionLocal, connection_pool
from sqlalchemy.orm import Session
import models, crud
from schemas.user import UserTokenPayload
import ast
import redis

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/access-token"
)

class OAuth2PasswordCookie(OAuth2PasswordBearer):
    """OAuth2 password flow with token in a httpOnly cookie.
    """

    def __init__(self, *args, token_name: str = None, **kwargs):
        super().__init__(*args, **kwargs)
        self._token_name = token_name or "access_token"

    @property
    def token_name(self) -> str:
        """Get the name of the token's cookie.
        """
        return self._token_name

    async def __call__(self, request: Request) -> str:
        """Extract and return a JWT from the request cookies.

        Raises:
            HTTPException: 403 error if no token cookie is present.
        """
        token = request.cookies.get(self._token_name)
        if not token:
            raise HTTPException(status_code=403, detail="Not authenticated")
        return token

class OAuth2PasswordCookieWS(OAuth2PasswordBearer):
    """OAuth2 password flow with token in a WebSocket cookie."""
    
    def __init__(self, *args, token_name: str = None, **kwargs):
        super().__init__(*args, **kwargs)
        self._token_name = token_name or "access_token"
    
    @property
    def token_name(self) -> str:
        """Get the name of the token's cookie."""
        return self._token_name

    async def __call__(self, websocket: WebSocket) -> str:
        """Extract and return a JWT from the WebSocket cookies.

        Raises:
            HTTPException: 403 error if no token cookie is present.
        """
        # Retrieve token from WebSocket cookies
        cookie = websocket.cookies.get(self._token_name)
        if not cookie:
            raise HTTPException(status_code=403, detail="Not authenticated")
        return cookie

oauth2_scheme = OAuth2PasswordCookie(  # pylint: disable=invalid-name
    tokenUrl=f"{settings.API_V1_STR}/login",
    token_name='access_token'
)

oauth2_scheme_ws = OAuth2PasswordCookieWS(  # pylint: disable=invalid-name
    tokenUrl=f"{settings.API_V1_STR}/login",
    token_name='access_token'
)

# Postgres
def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

# Redis
def get_redis() -> Generator[redis.Redis, None, None]:
    try:
        redis_client = redis.Redis(connection_pool=connection_pool)
        yield redis_client
    finally:
        redis_client.close()


def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
) -> UserTokenPayload:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        token_data = tokens.TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    # Convert the JSON text to a dictionary
    data = ast.literal_eval(token_data.sub)
    # Convert the dictionary to a Pydantic model
    user = UserTokenPayload.model_validate(data)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def get_current_user_ws(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme_ws)
) -> UserTokenPayload:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        token_data = tokens.TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    # Convert the JSON text to a dictionary
    data = ast.literal_eval(token_data.sub)
    # Convert the dictionary to a Pydantic model
    user = UserTokenPayload.model_validate(data)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def get_current_active_user(
    current_user: models.User = Depends(get_current_user),
) -> models.User:
    if not crud.user.is_active(current_user):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user