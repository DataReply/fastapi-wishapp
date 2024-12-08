import pytest
from sqlmodel import create_engine, Session, SQLModel, select

from database import get_db_session
from main import app
from models.user import User

TEST_DATABASE_URL = "sqlite:///./test.sqlite"

engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False}, echo=True)

TEST_USER_EMAIL = "test@test.com"


@pytest.fixture(scope="function", autouse=True)
def setup_and_teardown():
    try:
        SQLModel.metadata.drop_all(engine)
    except Exception:
        pass
    SQLModel.metadata.create_all(engine)
    # with Session(engine) as session:
    #     session.add(TEST_USER)
    #     session.commit()
    yield
    SQLModel.metadata.drop_all(engine)


@pytest.fixture
def _engine():
    return engine


@pytest.fixture
def test_db_session(_engine):
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def test_user(test_db_session):
    user = User(email=TEST_USER_EMAIL, hashed_password="password")
    test_db_session.add(user)
    test_db_session.commit()
    return user


def override_get_db_session() -> Session:
    with Session(engine) as session:
        yield session


app.dependency_overrides[get_db_session] = override_get_db_session
