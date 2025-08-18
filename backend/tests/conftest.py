import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from database.database import Base, get_db
from main import app

# Import all models so SQLAlchemy knows about them
from database.models.user import User
from database.models.profile import Profile
from database.models.followers import followers_association

# In-memory SQLite database
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/fliftyfly-test"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Override FastAPI dependency to use test DB
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="module")
def client():
    # Create all tables in test DB
    Base.metadata.create_all(bind=engine)
    with TestClient(app) as c:
        yield c
    # Drop tables after tests
    Base.metadata.drop_all(bind=engine)
