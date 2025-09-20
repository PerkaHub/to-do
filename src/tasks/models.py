from datetime import datetime, timezone

from sqlalchemy import ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.hybrid import hybrid_property

from src.database import Base
from src.tasks.enums import TaskPriority, TaskStatus


class Task(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(
        primary_key=True, nullable=False, index=True, autoincrement=True,
    )
    title: Mapped[str] = mapped_column(
        nullable=False,
    )
    description: Mapped[str | None] = mapped_column(
        nullable=True,
    )
    status: Mapped[TaskStatus] = mapped_column(
        SQLEnum(TaskStatus),
        default=TaskStatus.IN_PROGRESS,
        nullable=False,
    )
    priority: Mapped[TaskPriority] = mapped_column(
        SQLEnum(TaskPriority),
        default=TaskPriority.MEDIUM,
        nullable=False,
    )
    due_date: Mapped[datetime | None] = mapped_column(
        nullable=True,
    )
    completed_at: Mapped[datetime | None] = mapped_column(
        nullable=True,
    )
    created_at: Mapped[datetime] = mapped_column(
        nullable=False,
        default=datetime.now(timezone.utc),
    )
    updated_at: Mapped[datetime] = mapped_column(
        nullable=False,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
    )
    category_id: Mapped[int | None] = mapped_column(
        ForeignKey('categories.id', ondelete='CASCADE'),
        nullable=True,
        index=True,
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id', ondelete='SET NULL'),
        nullable=False,
        index=True,
    )

    user: Mapped['User'] = relationship('User', lazy='joined', back_populates='tasks')
    category: Mapped['Category | None'] = relationship(
        'Category', back_populates='tasks'
    )

    @hybrid_property
    def is_overdue(self) -> bool:
        """Check if task is overdue"""
        if not self.due_date:
            return False
        return (
            self.due_date < datetime.now(timezone.utc)
            and self.status != TaskStatus.COMPLETED
        )

    def __repr__(self) -> str:
        return f'<Task(id={self.id}, title="{self.title}", status={self.status})>'


class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(
        primary_key=True, nullable=False, index=True, autoincrement=True,
    )
    name: Mapped[str] = mapped_column(
        nullable=False,
    )

    tasks: Mapped[list['Task']] = relationship('Task', back_populates='category')

    def __repr__(self) -> str:
        return f'<Category(id={self.id}, name="{self.name}")>'
