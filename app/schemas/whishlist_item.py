import uuid

from pydantic import BaseModel, Field, ConfigDict


class WishlistItemCreate(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    quantity: int = Field(ge=1, default=1)


class WishlistItem(BaseModel):
    id: uuid.UUID
    wishlist_id: uuid.UUID
    name: str
    quantity: int
    model_config = ConfigDict(from_attributes=True)
