from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from core.settings import settings
from starlette.middleware.cors import CORSMiddleware
from api.api import api_router
#from api.routers.websocket import router as websocket_router
import logging
import os

app = FastAPI(
    title="MatchUp",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url=settings.docs_url,
    redoc_url=settings.redoc_url
) 


# Logging config for manual logging
LOGGING_LEVEL = logging.DEBUG
logging.basicConfig(format=f'%(asctime)s %(levelname)-8s  %(funcName)s:  %(message)s',
                    level=LOGGING_LEVEL, force=True)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)
