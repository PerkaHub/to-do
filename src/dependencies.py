from fastapi import Request, HTTPException, Depends
import jwt
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.repository import UserRepository
from src.database import get_db_session
from src.settings import settings


def get_token(request: Request):
    token = request.cookies.get('access_token')
    if not token:
        raise HTTPException(status_code=401)
    return token


async def get_current_user(
    session: AsyncSession = Depends(get_db_session),
    token: str = Depends(get_token)
):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, [settings.ALGORITHM]
        )
        user_id: str = payload.get('sub')
        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token")
        user = await UserRepository.get_one_or_none(session, id=int(user_id))
        if not user:
            raise HTTPException(
                status_code=401,
                detail="User not found"
            )
        return user
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")
