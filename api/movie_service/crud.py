from typing import List

from sqlalchemy.orm import Session

from movie_service import db
from movie_service import models


def get_movie(db: Session, movie_id: int) -> db.Movie:
    return db.query(db.Movie).filter(db.Movie.id == movie_id).first()


def get_movies(db: Session, skip: int = 0, limit: int = 100) -> List[db.Movie]:
    return db.query(db.Movie).offset(skip).limit(limit).all()


def create_movie(db: Session, movie: models.MovieCreate) -> db.Movie:
    db_movie = db.Movie(title=movie.title, year=movie.year)
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie


def get_actor(db: Session, actor_id: int) -> db.Actor:
    return db.query(db.Actor).filter(db.Actor.id == actor_id).first()


def get_actors(db: Session, skip: int = 0, limit: int = 100) -> List[db.Actor]:
    return db.query(db.Actor).offset(skip).limit(limit).all()


def create_actor(db: Session, actor: models.ActorCreate) -> db.Actor:
    db_actor = db.Actor(name=actor.name)
    db.add(db_actor)
    db.commit()
    db.refresh(db_actor)
    return db_actor
