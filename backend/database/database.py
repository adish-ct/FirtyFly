from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Update this when moving to production (don’t hardcode creds in
# database server / username: password @ host / database name.
DATABASE_URL = "postgresql://postgres:postgres@localhost/flirtfly"
#for production : postgresql://username:password@db-host:5432/dbname


# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# SessionLocal is used for DB sessions in routes
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for ORM models
Base = declarative_base()

# Dependency for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()