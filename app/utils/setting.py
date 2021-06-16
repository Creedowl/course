from pydantic import BaseSettings


class Setting(BaseSettings):
    class Config:
        env_file = "env"

    name: str = "Course"
    version: str = "0.1.0"
    debug: bool = False
    password_salt: str = ""
    db_uri: str
    db_prefix: str = ""
    oracle_lib_dir: str
    jwt_secret_key: str
    jwt_algorithm: str
    jwt_expire_seconds: int = 1800


config = Setting()
