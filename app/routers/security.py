from dataclasses import dataclass
from datetime import datetime, UTC, timedelta
from typing import Annotated, Type, Optional

import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jwt import InvalidTokenError
from passlib.context import CryptContext
from sqlmodel import select
from starlette import status

from app.config import settings
from app.database import DbSession
from app.models.user import User

ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@dataclass
class User:
    email: str
    hashed_password: str
    disabled: bool

USERS = {
    "alice@a.com": User(email="alice@a.com",
                        hashed_password="$2b$12$22.Hr.miOzqOG4JwPMgnJe5Q7xPZuNsE93.BmfMCN0tscOKbyI7EK", disabled=False),
    "bob@b.com": User(email="bob@b.com",
                      hashed_password="$2b$12$uA9tsNdO8DBby7r/sUWVx.UJSJAfStONHIOnZ23IwNOkYHsT6Gvue", disabled=True),
}

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: DbSession):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid token",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.AUTH_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except InvalidTokenError:
        raise credentials_exception
    user = get_active_user(username, db)
    if user is None:
        raise credentials_exception
    return user


def get_active_user(email: str, db: DbSession) -> Optional[Type[User]]:
    user = db.exec(select(User).where(User.email == email)).first()
    if not user or user.disabled:
        return None

    return user


def authenticate_user(username: str, password: str, db: DbSession) -> Optional[Type[User]]:
    user = get_active_user(username, db)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None

    return user

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_jwt_payload(token: str) -> dict:
    return jwt.decode(token, settings.AUTH_KEY, algorithms=[ALGORITHM])


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(UTC) + expires_delta
    else:
        expire = datetime.now(UTC) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.AUTH_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid token",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.AUTH_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except InvalidTokenError:
        raise credentials_exception
    user = get_active_user(username)
    if user is None:
        raise credentials_exception
    return user
