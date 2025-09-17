from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_db_session
from src.auth.service import UserService
from src.auth.schemas import RegisterUser


router = APIRouter(
    prefix='/api/v1/auth',
    tags=['Authentification']
)


@router.post('/register')
async def register_user(
    user_data: RegisterUser,
    session: AsyncSession = Depends(get_db_session),
):
    await UserService.register_user(
        email=user_data.email,
        password=user_data.password,
        session=session
    )
    return None


@router.post('/login')
async def login_user():
    pass


@router.patch('/password')
async def change_passsword():
    pass


@router.patch('/logout')
async def logout_user():
    pass
