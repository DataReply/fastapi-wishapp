from sqlmodel import select

from tests import conftest
from app.models.user import User

TEST_EMAIL = "new@user.com"


def test_create_user_returns_user(test_client, test_db_session):
    response = test_client.post("/users/", json={"email": TEST_EMAIL, "password": "mypassword"})

    assert response.status_code == 200
    db_user = test_db_session.exec(select(User).filter(User.email == TEST_EMAIL)).first()
    assert db_user.email == TEST_EMAIL

def test_create_user_returns_error_if_user_exists(test_client, test_db_session, test_user):
    response = test_client.post("/users/", json={"email": conftest.TEST_USER_EMAIL, "password": "mypassword"})

    assert response.status_code == 400
    assert response.json() == {"detail": "User with this email already exists"}