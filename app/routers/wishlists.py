import uuid
from uuid import uuid4

from fastapi import APIRouter, HTTPException

from app.schemas.whishlist_item import WishlistItem, WishlistItemCreate
from app.schemas.wishlist import WishlistCreate, Wishlist

router = APIRouter()

@router.post("/", response_model=Wishlist)
def create_wishlist(wishlist: WishlistCreate):
    return Wishlist(**wishlist.model_dump(), id=uuid4())

@router.get("/", response_model=list[Wishlist])
def get_wishlists():
    return []

@router.get("/{wishlist_id}", response_model=Wishlist)
def get_wishlist(wishlist_id: uuid.UUID):
    raise HTTPException(status_code=404, detail="Wishlist not found. Endpoint is not implemented yet")

@router.put("/{wishlist_id}", response_model=Wishlist)
def update_wishlist(wishlist_id: uuid.UUID, wishlist: WishlistCreate):
    raise HTTPException(status_code=500, detail="Endpoint is not implemented yet")

@router.delete("/{wishlist_id}", response_model=Wishlist)
def delete_wishlist(wishlist_id: uuid.UUID):
    raise HTTPException(status_code=500, detail="Endpoint is not implemented yet")

@router.post("/{wishlist_id}/items", response_model=WishlistItem)
def create_item(wishlist_id: uuid.UUID, item: WishlistItemCreate):
    return WishlistItem(**item.model_dump(), id=uuid4(), wishlist_id=wishlist_id)

@router.delete("/{wishlist_id}/items/{item_id}", response_model=WishlistItem)
def create_item(wishlist_id: uuid.UUID, item_id: uuid.UUID):
    raise HTTPException(status_code=500, detail="Endpoint is not implemented yet")
