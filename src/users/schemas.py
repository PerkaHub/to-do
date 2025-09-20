from pydantic import BaseModel, EmailStr
from src.tasks.schemas import TaskResponse


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    image: str | None

    class Config:
        from_attributes = True


class UserWithTasks(UserResponse):
    tasks: list['TaskResponse']
