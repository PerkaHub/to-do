from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(
        primary_key=True, nullable=False, index=True, autoincrement=True,
    )
    email: Mapped[str] = mapped_column(
        nullable=False, index=True, unique=True
    )
    hashed_password: Mapped[str] = mapped_column(
        nullable=False
    )
    image: Mapped[str | None] = mapped_column(
        nullable=True
    )

    tasks: Mapped[list['Task']] = relationship(
        'Task',
        lazy='selectin',
        back_populates='user'
    )
