from fastapi import FastAPI

from movie_service.routers import movies, actors

app = FastAPI()

app.include_router(movies.router)
app.include_router(actors.router)


@app.get("/")
def home():
    return {"msg": "Hello FastAPI🚀"}
