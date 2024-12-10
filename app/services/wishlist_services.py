from fastapi import HTTPException
from sqlmodel import Session, select

from app.models.base import PrimaryKeyType
from app.models.user import User
from app.models.wishlist import Wishlist
from app.models.wishlist_item import WishlistItem


def get_wishlist_or_error(wishlist_id: PrimaryKeyType, user: User, db: Session):
    db_wishlist = db.exec(
        select(Wishlist).where(Wishlist.user_id == user.id, Wishlist.id == wishlist_id)
    ).first()

    if not db_wishlist:
        raise HTTPException(status_code=404, detail="Wishlist not found.")

    return db_wishlist

def get_wishlist_item_or_error(wishlist_id: PrimaryKeyType, item_id: PrimaryKeyType, db: Session):
    db_wishlist_item = db.exec(
        select(WishlistItem).where(WishlistItem.wishlist_id == wishlist_id, WishlistItem.id == item_id)
    ).first()

    if not db_wishlist_item:
        raise HTTPException(status_code=404, detail="Wishlist item not found.")

    return db_wishlist_item