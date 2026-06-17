from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "Resilient-Path"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Redis & DB Settings
    REDIS_URL: str = "redis://localhost:6379/0"
    DATABASE_URL: Optional[str] = None
    
    # Security
    SECRET_KEY: str = "super-secret-key-change-in-production"
    
    class Config:
        env_file = ".env"

settings = Settings()