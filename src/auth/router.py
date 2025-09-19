from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_db_session
from src.auth.service import UserService
from src.auth.schemas import UserAuth
from src.auth.utils import set_token_cookies


router = APIRouter(
    prefix='/api/v1/auth',
    tags=['Authentification']
)


@router.post('/register')
async def register_user(
    response: Response,
    user_data: UserAuth,
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
    user_data: UserAuth,
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


@router.patch('/logout')
async def logout_user():
    pass
