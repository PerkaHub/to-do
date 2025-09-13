from fastapi import APIRouter


router = APIRouter(
    prefix='/api/v1/user',
    tags=['User']
)


@router.get('/me')
async def get_me():
    pass


@router.post('/change')
async def change_user():
    pass
