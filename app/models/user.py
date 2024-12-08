from sqlmodel import SQLModel, Field, Relationship

from models.base import SqlBaseModel
from models.wishlist import Wishlist

class UserCreate(SQLModel):
    email: str
    password: str


class User(SqlBaseModel, table=True):
    __tablename__ = "users"

    email: str = Field(unique=True, index=True)
    hashed_password: str
    disabled: bool = Field(default=False)

    wishlists: list[Wishlist] = Relationship(back_populates="user")


class UserPublic(SqlBaseModel):
    email: str
    disabled: bool
