from pydantic import BaseModel


class UserBase(BaseModel):
    Sno: str


class UserCreate(UserBase):
    Sname: str
    Sgender: str
    Sdept: str
    Sage: int
    password: str


class UserUpdate(UserBase):
    old_password: str = None
    new_password: str = None


class UserInfo(UserBase):
    class Config:
        orm_mode = True

    Sname: str
    Sgender: str
    Sdept: str
    Sage: int


class UserOut(UserInfo):
    access_token: str
    token_type: str
