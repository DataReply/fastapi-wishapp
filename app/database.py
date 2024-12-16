from typing import Annotated

from fastapi import Depends
from sqlmodel import create_engine, Session, SQLModel

from app.config import settings

SQLALCHEMY_DATABASE_URL = settings.SQL_LITE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}, echo=True)

def get_db_session() -> Session:
    with Session(engine) as session:
        yield session


DbSession = Annotated[Session, Depends(get_db_session)]
