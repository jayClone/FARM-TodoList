from pydantic import BaseSettings
from decouple import config

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = config("SECRET_KEY")
    PROJECT_NAME: str = config("PROJECT_NAME")
    SQLALCHEMY_DATABASE_URI: str = config("SQLALCHEMY_DATABASE_URI")
    BACKEND_CORS_ORIGINS: str = config("BACKEND_CORS_ORIGINS")
    
    #database
    MONGO_CONNECTION_URL: str = config("MONGO_CONNECTION_URL", cast=str)

    class Config:
        case_sensitive = True