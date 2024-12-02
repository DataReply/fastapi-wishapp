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

settings = Settings(
    API_VERSION="v1",
    PROJECT_NAME="Wishlist API",
    ENV="dev",
    LOG_LEVEL="DEBUG",
    SERVER_HOST="localhost",
    SERVER_PORT=8000,
    SQL_LITE_URL="sqlite:///./app.db"
)