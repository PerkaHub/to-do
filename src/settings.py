from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Database settings
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    ASYNC_DB_DRIVER: str

    EXPIRES_AT_ACCESS_TOKEN: int
    SECRET_KEY: str
    ALGORITHM: str

    @property
    def ASYNC_DATABASE_URL(self):
        return (
            f'{self.ASYNC_DB_DRIVER}://{self.DB_USER}:{self.DB_PASSWORD}'
            f'@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
        )

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding="utf-8"
    )


settings = Settings()
