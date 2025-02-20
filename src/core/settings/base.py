# Standard Library
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import ClassVar

from dotenv import load_dotenv

# Third Party Stuff
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings as PydanticBaseSettings
from pydantic_settings import SettingsConfigDict

from core.settings.enum import HashingAlgorithmsEnum, JWTAlgorithmsEnum
from utils.environment import EnvironmentsTypes

LIST_PATH_TO_ADD = []
if LIST_PATH_TO_ADD:
    sys.path.extend(LIST_PATH_TO_ADD)


BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENVS_DIR = BASE_DIR.parent / ".envs"
ENV_BASE_FILE_PATH = ENVS_DIR / ".env.base"
load_dotenv(ENV_BASE_FILE_PATH)
ENVIRONMENT = os.environ.get("ENVIRONMENT")
EnvironmentsTypes.check_env_value(ENVIRONMENT)
ENV_FILE_PATH = ENVS_DIR / EnvironmentsTypes.get_env_file_name(ENVIRONMENT)


class Settings(PydanticBaseSettings):
    model_config = SettingsConfigDict(env_file=ENV_FILE_PATH, extra="ignore", case_sensitive=True)
    ENVIRONMENT: str = ENVIRONMENT
    CORS_ORIGINS: ClassVar[list[str]] = ["*"]
    # Database settings
    # ----------------------------------------------------------------
    SECRET_KEY: str
    POSTGRES_DSN: PostgresDsn

    # JWT
    # ----------------------------------------------------------------
    PUBLIC_KEY_JWT: str

    # Project Constants
    # ----------------------------------------------------------------
    PROJECT_NAME: str = "Unicon Blog"
    PROJECT_ID: str = "A0003"
    VERSION: str = "v0.0.1"
    DESCRIPTION: str = "Una descripción"
    TEAM_NAME: str = "R2"
    TIME_ZONE: str = "utc"
    TIME_ZONE_UTC: str = "utc"
    DATE_FORMAT: str = "%Y-%m-%d"
    DATE_TIME_FORMAT: str = "%Y-%m-%d %H:%M:%S"
    API_V1: str = "v1"
    TIMESTAMP: str = datetime.now().astimezone().strftime(format="%Y-%m-%d %H:%M:%S")

    # Password settings
    # ----------------------------------------------------------------
    HASHING_ALGORITHM: HashingAlgorithmsEnum = HashingAlgorithmsEnum.BCRYPT

    # Token JWT settings
    # ----------------------------------------------------------------
    TIME_SECONDS_EXPIRE_TOKEN_JWT: int = 60 * 60 * 24
    ALGORITHM_JWT: JWTAlgorithmsEnum = JWTAlgorithmsEnum.RS256

    # Authenticate settings
    # ----------------------------------------------------------------
    TIME_SECONDS_EXPIRE_CODE_VALIDATE_EMAIL: int = 60 * 60 * 24 * 30
    TIME_SECONDS_EXPIRE_CODE_2FA: int = 60 * 1
    TIME_SECONDS_EXPIRE_VERIFICATION_CODE: int = 20 * 60
    LENGHT_CODE_VALIDATE_EMAIL: int = 4
    LENGHT_CODE_2FA: int = 4

    # Pagination settings
    # ----------------------------------------------------------------
    DEFAULT_PAGE_SIZE: int = 30
    DEFAULT_ORDER_FIELD: str = "created"

    API_KEY: str
    #ROOT_SERVICE_NAME: str
    #ROOT_ENCRYPTED_KEY: str

    PUBLIC_ENDPOINTS: list[str] = ["/health", "/docs", ""]

    # API AUTH
    AUTH_SERVICE_API_HOST: str
    AUTHTENTICATION_ACTIVE: bool
    AUTH_SERVICE_API_VERSION: str = "v1"
    AUTH_SERVICE_API_PREFIX: str = "services"
    HOST_URL: str = ""
