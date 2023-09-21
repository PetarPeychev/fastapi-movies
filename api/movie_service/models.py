from pydantic import BaseModel


class MovieBase(BaseModel):
    title: str
    year: int


class MovieCreate(MovieBase):
    pass


class Movie(MovieBase):
    id: int

    class Config:
        orm_mode = True


class ActorBase(BaseModel):
    name: str


class ActorCreate(ActorBase):
    pass


class Actor(ActorBase):
    id: int

    class Config:
        orm_mode = True
