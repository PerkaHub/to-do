from passlib.context import CryptContext
from src.auth.repository import UserRepository

pwd_context = CryptContext(schemes=['argon2'], deprecated='auto')


class EmailAlreadyExistsError(Exception):
    pass


class UserService:
    @classmethod
    async def register_user(cls, email, password, session):
        user = await UserRepository.get_one_or_none(session, email=email)
        if user:
            raise EmailAlreadyExistsError(f"User with email {email} already exists")
        hashed_password = get_password_hash(password)
        await UserRepository.add_data(
            session=session,
            email=email,
            hashed_password=hashed_password
        )


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
