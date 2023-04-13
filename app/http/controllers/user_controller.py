from fastapi import APIRouter, HTTPException, Request
from starlette.authentication import requires

from ..responses import Me, Status

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={
        401: Status(success=False, message="Unauthorized").dict(),
        402: Status(success=False, message="Forbidden").dict(),
        404: Status(success=False, message="Not found").dict(),
    },
)


@router.get("/me")
@requires(["user"])
async def signin(request: Request) -> Me:
    user = request.user
    return Me.from_model(user)
