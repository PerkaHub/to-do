from datetime import datetime
from pydantic import BaseModel, ConfigDict
from src.tasks.enums import TaskPriority, TaskStatus


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    status: TaskStatus = TaskStatus.IN_PROGRESS
    priority: TaskPriority = TaskPriority.MEDIUM
    due_date: datetime
    user_id: int
    created_at: datetime
    updated_at: datetime
    completed_at: datetime | None
    is_overdue: bool
    category_id: int | None

    model_config = ConfigDict(from_attributes=True)
