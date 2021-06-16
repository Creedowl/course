from typing import Optional
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.utils.security import hash_password, verify_password


class CRUDUser:
    def get(self, db: Session, sno: str = "") -> Optional[User]:
        user = db.query(User).filter(User.Sno == sno).first()
        return user

    def create(self, db: Session, user_in: UserCreate) -> User:
        user = User(**user_in.dict(exclude={"password"}),
                    hashed_password=hash_password(user_in.Sno, user_in.password),
                    is_admin=False)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def auth(self, db: Session, sno: str, password: str) -> Optional[User]:
        user = self.get(db, sno)
        if not user:
            return None
        if not verify_password(user.Sno, password, user.hashed_password):
            raise Exception("Password is wrong")
        return user


userCRUD = CRUDUser()
