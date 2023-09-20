from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://pg_user:pg_pass@postgres_db/pg_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionPG = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
