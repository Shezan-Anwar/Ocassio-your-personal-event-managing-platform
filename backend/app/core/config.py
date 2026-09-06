from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "Occasio API"
    API_V1_STR: str = "/api/v1"
    
    # Security
    SECRET_KEY: str = "CHANGE_THIS_IN_PRODUCTION_TO_A_SUPER_SECRET_RANDOM_KEY"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 1 day

    # Database
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/occasio_db"

    # CORS
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:5173", "http://localhost:3000"]

    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()
