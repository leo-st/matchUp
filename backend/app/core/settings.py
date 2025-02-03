from typing import List
from pydantic_settings import BaseSettings
import os
from os import listdir, getenv
from os.path import dirname, abspath, join
import inspect

class Settings(BaseSettings):
    
    def get_local_base_folder() -> str:
        current_dir = dirname(abspath(inspect.getfile(inspect.currentframe())))
        base_dir = dirname(dirname(current_dir))

        return base_dir
    
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = 'secret-password'
    authjwt_token_location: set = {"cookies"}
    authjwt_cookie_secure: bool = False
    authjwt_cookie_csrf_protect: bool = True
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 2

    CORS_URL_LIST:str = os.getenv('CORS_URLS', '')
    BACKEND_CORS_ORIGINS: List[str] = CORS_URL_LIST.split(',')

    WEBHOOK_URL: str = os.getenv("WEBHOOK_URL", 'http://localhost:5015/api/v1/webhook')
    
    SQLALCHEMY_DATABASE_URI: str = os.getenv('SQLALCHEMY_DATABASE_URI','postgresql://administrator:secret-password@localhost:5432/postgres')
    POSTGRES_HOST: str =os.getenv('POSTGRES_HOST','')
    POSTGRES_PORT: str =os.getenv('POSTGRES_PORT','')
    POSTGRES_USER: str =os.getenv('POSTGRES_USER','')
    POSTGRES_PASSWORD: str =os.getenv('POSTGRES_PASSWORD','')
    POSTGRES_DB: str =os.getenv('POSTGRES_DB','')
    
    REDIS_HOST: str = os.getenv("REDIS_HOST", )
    REDIS_PORT: int = int(os.getenv("REDIS_PORT", ))
    REDIS_PASSWORD: str = os.getenv("REDIS_PASSWORD", '')
    REDIS_URL:str = os.environ.get("REDIS_URL", '')


    class Config:
        case_sensitive = True

    SAME_SITE: str = os.getenv("SAME_SITE", 'LAX')
    UPDATE_PERIOD_IN_DAYS: int = 100

    jwt_cookie_secure_env:str = os.getenv("JWT_COOKIE_SECURE", "True")
    JWT_COOKIE_SECURE: bool = jwt_cookie_secure_env.lower() == "true"

    dev_mode_env:str = os.getenv("DEV_MODE", "True")
    DEV_MODE: bool = dev_mode_env.lower() == "true"
    
    docs_env:str = os.getenv("DOCS", "True")
    DOCS:bool = docs_env.lower() == "true"
    docs_url:str|None = "/docs" if DOCS else None
    redoc_url:str|None = "/redoc" if DOCS else None
    
    def get_local_base_folder() -> str:
        current_dir = dirname(abspath(inspect.getfile(inspect.currentframe())))
        base_dir = dirname(dirname(current_dir))

        return base_dir
    
    DATA_FOLDER :str = getenv('DATA_FOLDER', join(get_local_base_folder(), 'data'))

settings = Settings()