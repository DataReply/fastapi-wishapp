from typing import Annotated

from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import select

from app.database import DbSession
from app.models.base import PrimaryKeyType
from app.models.user import User
from app.models.wishlist import WishlistCreate, Wishlist, WishlistPublic, WishlistPatch
from app.models.wishlist_item import WishlistItem, WishlistItemCreate, WishlistItemPublic
from app.routers.security import get_current_user

router = APIRouter()


@router.post("/", response_model=WishlistPublic)
def create_wishlist(wishlist: WishlistCreate, user: Annotated[User, Depends(get_current_user)], db: DbSession):
    db_wishlist = Wishlist(**wishlist.model_dump(), user_id=user.id)
    db.add(db_wishlist)
    db.commit()
    db.refresh(db_wishlist)
    return db_wishlist


@router.get("/", response_model=list[WishlistPublic])
def get_wishlists(user: Annotated[User, Depends(get_current_user)], db: DbSession):
    return db.exec(select(Wishlist).where(Wishlist.user_id == user.id)).all()


@router.get("/{wishlist_id}", response_model=WishlistPublic)
def get_wishlist(wishlist_id: PrimaryKeyType, user: Annotated[User, Depends(get_current_user)], db: DbSession):
    db_wishlist = db.exec(
        select(Wishlist).where(Wishlist.user_id == user.id, Wishlist.id == wishlist_id)
    ).first()

    if not db_wishlist:
        raise HTTPException(status_code=404, detail="Wishlist not found.")

    return db_wishlist


@router.patch("/{wishlist_id}", response_model=WishlistPublic)
def patch_wishlist(wishlist_id: PrimaryKeyType,
                   wishlist: WishlistPatch,
                   user: Annotated[User, Depends(get_current_user)],
                   db: DbSession):
    db_wishlist = db.exec(
        select(Wishlist).where(Wishlist.user_id == user.id, Wishlist.id == wishlist_id)
    ).first()

    if not db_wishlist:
        raise HTTPException(status_code=404, detail="Wishlist not found.")

    db_wishlist.sqlmodel_update(wishlist.model_dump())
    db.commit()
    return db_wishlist


@router.delete("/{wishlist_id}", response_model=WishlistPublic)
def delete_wishlist(wishlist_id: PrimaryKeyType, user: Annotated[User, Depends(get_current_user)], db: DbSession):
    db_wishlist = db.exec(
        select(Wishlist).where(Wishlist.user_id == user.id, Wishlist.id == wishlist_id)
    ).first()

    if not db_wishlist:
        raise HTTPException(status_code=404, detail="Wishlist not found.")

    db.delete(db_wishlist)
    db.commit()

    return db_wishlist


@router.post("/{wishlist_id}/items", response_model=WishlistItemPublic)
def create_item(wishlist_id: PrimaryKeyType, item: WishlistItemCreate, user: Annotated[User, Depends(get_current_user)],
                db: DbSession):
    db_wishlist = db.exec(
        select(Wishlist.id).where(Wishlist.user_id == user.id, Wishlist.id == wishlist_id)
    ).first()

    if not db_wishlist:
        raise HTTPException(status_code=404, detail="Wishlist not found.")

    db_wishlist_item = WishlistItem(**item.model_dump(), wishlist_id=wishlist_id)
    db.add(db_wishlist_item)
    db.commit()

    return db_wishlist_item


@router.delete("/{wishlist_id}/items/{item_id}", response_model=WishlistItemPublic)
def delete_item(wishlist_id: PrimaryKeyType, item_id: PrimaryKeyType, user: Annotated[User, Depends(get_current_user)],
                db: DbSession):
    db_wishlist = db.exec(
        select(Wishlist.id).where(Wishlist.user_id == user.id, Wishlist.id == wishlist_id)
    ).first()

    if not db_wishlist:
        raise HTTPException(status_code=404, detail="Wishlist not found.")

    db_wishlist_item = db.exec(
        select(WishlistItem).where(WishlistItem.id == item_id, WishlistItem.wishlist_id == wishlist_id)
    ).first()
    if not db_wishlist_item:
        raise HTTPException(status_code=404, detail="Wishlist item not found.")

    db.delete(db_wishlist_item)
    db.commit()

    return db_wishlist_item
