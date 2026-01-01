from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    MONGODB_URI: str
    MONGODB_DB_NAME: str
    JWT_SECRET_KEY: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="forbid"
    )

settings = Settings()
