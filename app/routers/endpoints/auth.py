from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette import status

from app.crud.database import get_db
from app.crud.user import userCRUD
from app.schemas.token import Token
from app.utils.security import generate_jwt

router = APIRouter(tags=["Authentication"])


@router.post("/login", response_model=Token)
def login(
        db: Session = Depends(get_db),
        form_data: OAuth2PasswordRequestForm = Depends()
):
    """
    OAuth2 login part, use JWT as access token
    """
    try:
        user = userCRUD.auth(db, form_data.username, form_data.password)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e)
        )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return {
        "access_token": generate_jwt({"sub": user.Sno}),
        "token_type": "bearer",
    }
