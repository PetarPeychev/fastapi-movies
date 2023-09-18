from fastapi import APIRouter

router = APIRouter(
    prefix="/actors",
    tags=["actors"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_actors():
    return {}
