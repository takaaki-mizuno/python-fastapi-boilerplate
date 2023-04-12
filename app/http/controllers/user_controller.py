from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {
        "description": "Not found"
    }},
)


@router.post("/signin")
async def signin() -> list:
    return []
