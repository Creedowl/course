from sqlalchemy.orm import declared_attr, declarative_base

from app.utils.setting import config


class CustomBase:
    @declared_attr
    def __tablename__(cls):
        prefix: str = config.db_prefix + "_" if config.db_prefix != "" else ""
        return prefix + cls.__name__.lower()


Base = declarative_base(cls=CustomBase)
