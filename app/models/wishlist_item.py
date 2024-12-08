from sqlmodel import SQLModel, Field, Relationship

from models.base import SqlBaseModel, PrimaryKeyType


class WishlistItemCreate(SQLModel):
    name: str = Field(min_length=1, max_length=50)
    quantity: int = Field(ge=1, default=1)

class WishlistItem(SqlBaseModel, table=True):
    __tablename__ = "wishlist_items"

    name: str = Field(unique=True, index=True)
    quantity: int = Field(ge=1, default=1)
    wishlist_id: PrimaryKeyType = Field(foreign_key="wishlists.id")


    wishlist: "Wishlist" = Relationship(back_populates="items")


class WishlistItemPublic(SqlBaseModel):
    name: str
    quantity: int
