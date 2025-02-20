from datetime import datetime, timedelta, timezone

import jwt
from jwt import ExpiredSignatureError, InvalidTokenError, decode
from pydantic import BaseModel, ValidationError

from core.settings import settings


def get_current_date_time_to_app_standard() -> datetime:
    return datetime.now(timezone(settings.TIME_ZONE))


def get_current_date_time_utc() -> datetime:
    return datetime.now(timezone(settings.TIME_ZONE_UTC))


class TokenDataSchema(BaseModel):
    user_id: str


class JWTHandler:

    @staticmethod
    def validate_token(token: str) -> TokenDataSchema:
        try:
            payload = decode(token, settings.PUBLIC_KEY_JWT, algorithms=[settings.ALGORITHM_JWT.value])
            return TokenDataSchema(**payload)
        except ExpiredSignatureError:
            raise ExpiredSignatureError("Token has expired")  # noqa: B904, TRY200
        except InvalidTokenError:
            raise InvalidTokenError("Invalid token")  # noqa: B904, TRY200
        except ValidationError as e:
            raise ValueError(f"Invalid token data: {e}")  # noqa: B904, TRY200
