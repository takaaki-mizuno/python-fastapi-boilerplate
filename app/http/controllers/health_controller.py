from fastapi import APIRouter, HTTPException

router = APIRouter(
    tags=["health"],
    responses={404: {
        "description": "Not found"
    }},
)


@router.get("/")
async def signin() -> dict:
    return {"status": "ok"}


@router.get("/healthz")
async def signin() -> dict:
    return {"status": "ok"}
