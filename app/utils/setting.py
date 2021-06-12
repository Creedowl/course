from pydantic import BaseSettings


class Setting(BaseSettings):
    class Config:
        env_file = "env"

    name: str = "Course"
    version: str = "0.1.0"
    debug: bool = False


config = Setting()
