from fastapi import APIRouter

from api.routers import test, login

api_router = APIRouter()

api_router.include_router(test.router, prefix='/test', tags=['test'])
api_router.include_router(login.router, tags=['login'])
