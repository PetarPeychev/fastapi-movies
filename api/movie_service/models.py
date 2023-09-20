from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from movie_service.database import Base


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
