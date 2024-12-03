from dataclasses import dataclass

@dataclass
class Settings:
    API_VERSION: str
    PROJECT_NAME: str
    ENV: str
    LOG_LEVEL: str

    SERVER_HOST: str
    SERVER_PORT: int

    SQL_LITE_URL: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_MINUTES: int

    AUTH_KEY: str

settings = Settings(
    API_VERSION="v1",
    PROJECT_NAME="Wishlist API",
    ENV="dev",
    LOG_LEVEL="DEBUG",
    SERVER_HOST="localhost",
    SERVER_PORT=8000,
    SQL_LITE_URL="sqlite:///./app.db",
    ACCESS_TOKEN_EXPIRE_MINUTES=60,
    REFRESH_TOKEN_EXPIRE_MINUTES=60,
    AUTH_KEY="09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
)