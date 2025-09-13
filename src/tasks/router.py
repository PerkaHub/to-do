from fastapi import APIRouter


router = APIRouter(
    prefix='/api/v1/tasks',
    tags=['Tasks']
)


@router.get('')
async def get_tasks():
    pass


@router.get('/{task_id}')
async def get_one_task(task_id):
    pass


@router.post('')
async def create_task():
    pass


@router.patch('/{task_id}')
async def change_task(task_id):
    pass


@router.delete('/{task_id}')
async def delete_task():
    pass
