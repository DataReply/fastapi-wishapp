from typing import Annotated

from fastapi import APIRouter, Depends
from sqlmodel import select

from routers.security import User, get_current_user
from app.database import DbSession
from app.models.base import PrimaryKeyType
from app.models.user import User
from app.models.wishlist import WishlistCreate, Wishlist, WishlistPublic, WishlistPatch
from app.models.wishlist_item import WishlistItem, WishlistItemCreate, WishlistItemPublic
from app.routers.security import get_current_user
from app.services.wishlist_services import get_wishlist_or_error, get_wishlist_item_or_error

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
    # Easy to use but may be not efficient because it loads wishlist items for every wishlist one by one
    return user.wishlists


@router.get("/{wishlist_id}", response_model=WishlistPublic)
def get_wishlist(wishlist_id: PrimaryKeyType, user: Annotated[User, Depends(get_current_user)], db: DbSession):
    db_wishlist = get_wishlist_or_error(wishlist_id, user, db)

    return db_wishlist


@router.patch("/{wishlist_id}", response_model=WishlistPublic)
def patch_wishlist(wishlist_id: PrimaryKeyType,
                   wishlist: WishlistPatch,
                   user: Annotated[User, Depends(get_current_user)],
                   db: DbSession):
    db_wishlist = get_wishlist_or_error(wishlist_id, user, db)

    db_wishlist.sqlmodel_update(wishlist.model_dump())
    db.commit()
    return db_wishlist


@router.delete("/{wishlist_id}", response_model=WishlistPublic)
def delete_wishlist(wishlist_id: PrimaryKeyType, user: Annotated[User, Depends(get_current_user)], db: DbSession):
    db_wishlist = get_wishlist_or_error(wishlist_id, user, db)

    db.delete(db_wishlist)
    db.commit()

    return db_wishlist


@router.post("/{wishlist_id}/items", response_model=WishlistItemPublic)
def create_item(wishlist_id: PrimaryKeyType, item: WishlistItemCreate, user: Annotated[User, Depends(get_current_user)],
                db: DbSession):
    # Check if wishlist exists and belongs to the user
    db_wishlist = get_wishlist_or_error(wishlist_id, user, db)

    db_wishlist_item = WishlistItem(**item.model_dump(), wishlist_id=db_wishlist.id)
    db.add(db_wishlist_item)
    db.commit()

    return db_wishlist_item


@router.delete("/{wishlist_id}/items/{item_id}", response_model=WishlistItemPublic)
def delete_item(wishlist_id: PrimaryKeyType, item_id: PrimaryKeyType, user: Annotated[User, Depends(get_current_user)],
                db: DbSession):
    # Check if wishlist exists and belongs to the user
    db_wishlist = get_wishlist_or_error(wishlist_id, user, db)

    db_wishlist_item = get_wishlist_item_or_error(db_wishlist.id, item_id, db)

    db.delete(db_wishlist_item)
    db.commit()

    return db_wishlist_item
