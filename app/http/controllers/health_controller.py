from fastapi import APIRouter, HTTPException, Request
from injector import Binder, Injector, InstanceProvider, singleton

from ...services import UserService

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
async def healthz(request: Request) -> dict:
    user_service = request.app.state.injector.get(UserService)

    return {"status": "ok"}
