from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Database settings
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_DRIVER: str

    @property
    def get_db_url(self):
        return (
            f'{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASSWORD}'
            f'@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
        )

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding="utf-8"
    )


settings = Settings()
