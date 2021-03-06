import secrets

from pydantic import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str = secrets.token_urlsafe(32)
    SQLALCHEMY_DATABASE_URI: str = "postgresql://localhost:5432/fastapi_db"

    class Config:
        env_file = ".env"


settings = Settings()
