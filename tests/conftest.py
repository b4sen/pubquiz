import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker

from pubquiz.server import app
from pubquiz.db.models import Base
from pubquiz.dependencies import get_db
from pubquiz.dependencies.auth import get_current_user


engine = create_engine(
    "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    try:
        db = TestSessionLocal()
        yield db
    finally:
        db.close()


def skip_auth():
    pass


@pytest.fixture(scope="session", autouse=True)
def test_db():
    Base.metadata.create_all(bind=engine)
    app.dependency_overrides[get_db] = override_get_db
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="session", autouse=True)
def seed_db(test_db):
    pass


@pytest.fixture
def client():
    # reset dependency override dictionary
    # can't deepcopy app
    app.dependency_overrides[get_current_user] = get_current_user
    return TestClient(app)


@pytest.fixture
def admin():
    app.dependency_overrides[get_current_user] = skip_auth
    return TestClient(app)
