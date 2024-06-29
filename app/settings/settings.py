from enum import Enum

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings


load_dotenv()


class LoggerLevel(Enum):
    INFO = "INFO"
    DEBUG = "DEBUG"


class ApiSettings(BaseSettings):
    host: str = Field("localhost", alias="API_HOST")
    port: int = Field(2000, alias="API_PORT")


class DatabaseSettings(BaseSettings):
    uri: str = Field("sqlite:///database.db", alias="DATABASE_URI")


class LoggerSettings(BaseSettings):
    level: LoggerLevel = Field("INFO", alias="LOGGER_LEVEL")


class Settings(BaseSettings):
    db: DatabaseSettings = DatabaseSettings()
    logger: LoggerSettings = LoggerSettings()
    api: ApiSettings = ApiSettings()
