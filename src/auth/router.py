from fastapi import APIRouter, Depends, Request, Response, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.dependencies import get_current_user
from src.database import get_db_session
from src.auth.service import UserService
from src.users.schemas import UserCreate
from src.auth.utils import set_token_cookies
from src.users.models import User


router = APIRouter(
    prefix='/api/v1/auth',
    tags=['Authentification']
)


@router.post('/register')
async def register_user(
    response: Response,
    user_data: UserCreate,
    session: AsyncSession = Depends(get_db_session),
):
    access_token = await UserService.register_user(
        email=user_data.email,
        password=user_data.password,
        session=session
    )
    set_token_cookies(response, access_token)
    return {'access_token': access_token}


@router.post('/login')
async def login_user(
    response: Response,
    user_data: UserCreate,
    session: AsyncSession = Depends(get_db_session),
):
    access_token = await UserService.login_user(
        email=user_data.email,
        password=user_data.password,
        session=session
    )
    set_token_cookies(response, access_token)
    return {'access_token': access_token}


@router.patch('/password')
async def change_passsword():
    pass


@router.delete('/logout', status_code=status.HTTP_204_NO_CONTENT)
async def logout_user(
    response: Response,
    request: Request,
    user: User = Depends(get_current_user)
):
    try:
        response.delete_cookie(
                key="access_token",
                path="/"
            )

    except Exception as e:
        # logger.error(f"Logout error for user {user.id}: {e}")
        response.delete_cookie("access_token", path="/")
