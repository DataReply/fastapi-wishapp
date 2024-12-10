from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import IntegrityError

from app.database import DbSession
from app.routers.security import get_password_hash
from app.models.user import User, UserCreate, UserPublic

router = APIRouter()

@router.post("/", response_model=UserPublic)
async def create_user(user: UserCreate, db: DbSession):
    try:
        user = User(email=user.email, hashed_password=get_password_hash(user.password))
        db.add(user)
        db.commit()
    except IntegrityError as e:
        raise HTTPException(status_code=400, detail="User with this email already exists")

    return user