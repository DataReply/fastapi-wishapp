import os
from typing import ClassVar

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
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

class LocalSettings(Settings):
    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"),
        env_file_encoding="utf-8",
        case_sensitive=True,
    )
    ENV: str = "local"
    # This is only used for local development. For production pass the secret as an environment
    # variable or use a mounted secret.
    # Read more in pydantic settings guide: https://docs.pydantic.dev/latest/concepts/pydantic_settings/#secrets
    AUTH_KEY: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"

class DevSettings(Settings):
    """
    These settings are supposed to be used in DEV environment. For example, after deploying the app via a Pull Request
    pipeline.
    """
    env_path:ClassVar[str] = os.path.dirname(os.path.dirname(__file__))

    model_config = SettingsConfigDict(
        # Here we are using both common and dev specific configuration.
        # The config from '.env.dev' will override the config from '.env'.
        env_file=(os.path.join(env_path, ".env"), os.path.join(env_path, ".env.dev")),
        env_file_encoding="utf-8",
        case_sensitive=True,
    )
    ENV: str = "local"


def get_setting(env: str):
    if env == "local":
        return LocalSettings()
    if env == "dev":
        return DevSettings()

    # TODO: add more settings for different environments
    raise ValueError(f"Unknown environment: {env}")

_env = os.getenv("ENV", "local")
settings = get_setting(_env)