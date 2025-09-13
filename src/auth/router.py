from fastapi import APIRouter


router = APIRouter(
    prefix='/api/v1/auth',
    tags=['Authentification']
)


@router.post('/register')
async def register_user():
    pass


@router.post('/login')
async def login_user():
    pass


@router.patch('/password')
async def change_passsword():
    pass
