from sqlalchemy import create_engine, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

SQLALCHEMY_DATABASE_URL = "postgresql://pg_user:pg_pass@postgres_db/pg_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionPG = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    year = Column(Integer)


class Actor(Base):
    __tablename__ = "actors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)


class MovieActor(Base):
    __tablename__ = "movies_actors"

    id = Column(Integer, primary_key=True, index=True)
    movie_id = Column(Integer, ForeignKey("movies.id"))
    actor_id = Column(Integer, ForeignKey("actors.id"))

    movie = relationship("Movie", back_populates="actors")
    actor = relationship("Actor", back_populates="movies")
