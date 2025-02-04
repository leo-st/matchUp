from fastapi import APIRouter

from api.routers import test, login, sport, feed

api_router = APIRouter()

api_router.include_router(test.router, prefix='/test', tags=['test'])
api_router.include_router(login.router, tags=['login'])
api_router.include_router(sport.router, prefix='/sport', tags=['sport'])
api_router.include_router(feed.router, prefix='/feed', tags=['feed'])
