import os
from typing import Union

from dotenv import load_dotenv
from pydantic import AnyHttpUrl, BaseSettings, IPvAnyAddress

load_dotenv()


class Config(BaseSettings):
    DB_USERNAME: str = os.getenv("DB_USERNAME", "postgres")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")
    DB_HOST: Union[AnyHttpUrl,
                   IPvAnyAddress] = os.getenv("DB_HOST", "127.0.0.1")
    DB_NAME: str = os.getenv("DB_NAME", "")
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

    AWS_ACCESS_ID: str = os.getenv("AWS_ACCESS_ID", "")
    AWS_ACCESS_SECRET: str = os.getenv("AWS_ACCESS_SECRET", "")
    S3_REGION: str = os.getenv("S3_REGION", "")
    S3_BUCKET: str = os.getenv("S3_BUCKET", "")

    JWT_SECRET: str = os.getenv("JWT_SECRET", "")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")


config = Config(_env_file='.env', _env_file_encoding='utf-8')
