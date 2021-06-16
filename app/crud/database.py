from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.utils.setting import config
import cx_Oracle

# fucking oracle
cx_Oracle.init_oracle_client(lib_dir=config.oracle_lib_dir)

engine = create_engine(config.db_uri, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_db() -> Session:
    try:
        db: Session = SessionLocal()
        yield db
    finally:
        db.close()
