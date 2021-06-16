from datetime import datetime, timedelta

from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from starlette import status

from app.crud.database import get_db
from app.models.user import User
from app.utils.setting import config

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(sno: str, raw_password: str) -> str:
    return pwd_context.hash(sno + raw_password + config.password_salt)


def verify_password(sno: str, raw_password: str, hashed_password: str) -> bool:
    origin = sno + raw_password + config.password_salt
    return pwd_context.verify(origin, hashed_password)


def generate_jwt(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(seconds=config.jwt_expire_seconds)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, config.jwt_secret_key, algorithm=config.jwt_algorithm)
    return encoded_jwt


def get_current_user(
        db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, config.jwt_secret_key, algorithms=[config.jwt_algorithm])
        sno: str = payload.get("sub")
        if sno is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = db.query(User).filter(User.Sno == sno).first()
    if user is None:
        raise credentials_exception
    return user
