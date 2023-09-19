from fastapi import APIRouter

router = APIRouter(
    prefix="/movies",
    tags=["movies"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_movies():
    return {
        "movies": [
            {
                "title": "The Godfather",
                "year": 1972,
                "rating": 9.2,
                "actors": ["Marlon Brando", "Al Pacino"],
            }
        ]
    }
