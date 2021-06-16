from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.crud.database import get_db
from app.crud.user import userCRUD
from app.models.user import User
from app.schemas.user import UserCreate, UserInfo
from app.utils.security import get_current_user

router = APIRouter(tags=["Users"])


@router.post("/register", response_model=UserInfo)
def register(
        *,
        db: Session = Depends(get_db),
        user_in: UserCreate
):
    user = userCRUD.get(db, user_in.Sno)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The user with this student id already exists in the system"
        )
    user = userCRUD.create(db, user_in)
    return user


@router.get("/me", response_model=UserInfo)
def get_me(user: User = Depends(get_current_user)):
    return user
