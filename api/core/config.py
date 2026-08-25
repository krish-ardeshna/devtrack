from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    GITHUB_TOKEN: str | None = None

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()