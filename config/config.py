from functools import lru_cache
from typing import List

from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Settings for the application."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore",
    )

    # App
    APP_PORT: int = 8080
    APP_HOST: str = "0.0.0.0"

    # Turso
    TURSO_DATABASE_URL: str
    TURSO_AUTH_TOKEN: str

    # Applicaciones instaladas
    INSTALLED_APPS: List[str] = ["src.auth", "src.blogs"]
    MODEL_FILE_NAME: str = "models.py"

    # API
    API_VERSION: str = "v0"

    # JWT
    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"

    @computed_field
    @property
    def TURSO_DATABASE_URI(self) -> str:
        return f"sqlite+{self.TURSO_DATABASE_URL}/?authToken={self.TURSO_AUTH_TOKEN}&secure=true"

    @computed_field
    @property
    def api_prefix(self) -> str:
        return f"/api/{self.API_VERSION}"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
