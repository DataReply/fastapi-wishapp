import uuid

from pydantic import BaseModel, ConfigDict, Field


class WishlistCreate(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    description: str = Field(min_length=0, max_length=200)

class Wishlist(BaseModel):
    id: uuid.UUID
    name: str
    description: str

    model_config = ConfigDict(from_attributes=True)