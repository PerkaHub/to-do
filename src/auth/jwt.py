from datetime import datetime, timedelta, timezone

import jwt
from pydantic import EmailStr

from src.settings import settings


async def create_access_token(
    user_id: int,
    email: EmailStr
) -> str:
    payload = {
        'sub': str(user_id),
        'email': str(email),
        'exp': datetime.now(timezone.utc)
        + timedelta(minutes=settings.EXPIRES_AT_ACCESS_TOKEN)
    }
    try:
        encoded_jwt = jwt.encode(
            payload, settings.SECRET_KEY, settings.ALGORITHM
        )
        return encoded_jwt
    except Exception as e:
        raise ValueError(f'failed to create access token: {e}')
