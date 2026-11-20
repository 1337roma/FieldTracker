from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

# Вычисляем путь к C:\FieldTracker\.env
ENV_PATH = Path(__file__).resolve().parents[3] / ".env"


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    model_config = SettingsConfigDict(env_file=ENV_PATH)


settings = Settings()