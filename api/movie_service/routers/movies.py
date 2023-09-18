from fastapi import APIRouter

router = APIRouter(
    prefix="/movies",
    tags=["movies"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_movies():
    return {}
