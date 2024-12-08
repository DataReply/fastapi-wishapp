import pytest
from fastapi import HTTPException

from models.user import User
from models.wishlist import Wishlist
from models.wishlist_item import WishlistItem
from services.wishlist_services import get_wishlist_or_error, get_wishlist_item_or_error


def test_get_wishlist_raises_error_when_wishlist_does_not_exist(test_db_session):
    with pytest.raises(HTTPException) as error:
        get_wishlist_or_error(999, User(id=1), test_db_session)

    assert error.value.status_code == 404


def test_get_wishlist_raises_error_when_user_is_different(test_db_session, test_user):
    wishlist = Wishlist(user_id=test_user.id, name="Test Wishlist", description="Test Description")
    test_db_session.add(wishlist)

    test_db_session.commit()
    with pytest.raises(HTTPException) as error:
        get_wishlist_or_error(wishlist.id, User(id=10000), test_db_session)

    assert error.value.status_code == 404


def test_get_wishlist_returns_wishlist(test_db_session, test_user):
    wishlist = Wishlist(user_id=test_user.id, name="Test Wishlist", description="Test Description")
    test_db_session.add(wishlist)

    test_db_session.commit()

    result = get_wishlist_or_error(wishlist.id, test_user, test_db_session)

    assert result.name == "Test Wishlist"


def test_get_wishlist_item_raises_error_when_wishlist_does_not_exist(test_db_session):
    with pytest.raises(HTTPException) as error:
        get_wishlist_item_or_error(wishlist_id=999, item_id=1, db=test_db_session)

    assert error.value.status_code == 404


def test_get_wishlist_item_raises_error_when_item_does_not_exist(test_db_session, test_user):
    wishlist = Wishlist(user_id=test_user.id, name="Test Wishlist", description="Test Description")
    test_db_session.add(wishlist)

    test_db_session.commit()
    with pytest.raises(HTTPException) as error:
        get_wishlist_item_or_error(wishlist_id=wishlist.id, item_id=1, db=test_db_session)

    assert error.value.status_code == 404


def test_get_wishlist_returns_item(test_db_session, test_user):
    wishlist = Wishlist(user_id=test_user.id, name="Test Wishlist", description="Test Description")
    wishlist_item = WishlistItem(name="Test Item", description="Test Description")
    wishlist.items.append(wishlist_item)
    test_db_session.add(wishlist)

    test_db_session.commit()

    result = get_wishlist_item_or_error(wishlist_id=wishlist.id, item_id=wishlist_item.id, db=test_db_session)

    assert result.name == "Test Item"
