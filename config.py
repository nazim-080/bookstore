from pydantic import BaseSettings


class Settings(BaseSettings):
    db_host: str
    db_port: str
    db_name: str
    db_user: str
    db_pass: str

    class Config:
        env_file = ".env"


settings = Settings()