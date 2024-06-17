from pydantic import BaseSettings


class Settings(BaseSettings):
    secrey_key: str
    email_backend: str
    email_host: str
    email_port: int
    email_host_user: str
    email_host_password: str
    default_from_email: int
    db_name: str
    db_user: str
    db_pass: str
    db_host: str
    db_port: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()