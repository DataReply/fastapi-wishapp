from sqlmodel import SQLModel, Field, Relationship

from models.base import SqlBaseModel, PrimaryKeyType
from models.wishlist_item import WishlistItem, WishlistItemPublic



class WishlistCreate(SQLModel):
    name: str = Field(min_length=1, max_length=50)
    description: str = Field(min_length=0, max_length=200)

class WishlistPatch(SQLModel):
    name: str | None  = Field(min_length=1, max_length=50, default=None)
    description: str | None = Field(min_length=0, max_length=200, default=None)


class Wishlist(SqlBaseModel, table=True):
    __tablename__ = "wishlists"

    name:str = Field(unique=True, index=True)
    description:str | None
    user_id:PrimaryKeyType = Field(foreign_key="users.id")

    user: "User" = Relationship(back_populates="wishlists")
    items: list[WishlistItem] = Relationship(back_populates="wishlist")

class WishlistPublic(SqlBaseModel):
    name: str
    description: str | None
    items: list[WishlistItemPublic]