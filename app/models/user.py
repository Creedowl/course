from sqlalchemy import Column, Integer, String, Boolean

from app.models.base import Base


class User(Base):
    Sno = Column(String(10), primary_key=True)
    Sname = Column(String(20), index=True)
    Sgender = Column(String(5))
    Sdept = Column(String(20))
    Sage = Column(Integer)
    hashed_password = Column(String(100))
    is_admin = Column(Boolean)
