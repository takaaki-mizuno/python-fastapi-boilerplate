from fastapi import APIRouter, HTTPException, Request
from injector import Binder, Injector, InstanceProvider, singleton
from starlette.authentication import requires

from ...services import UserService
from ..requests import SignIn
from ..responses import AccessToken, Status

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={
        401: Status(success=False, message="Unauthorized").dict(),
        402: Status(success=False, message="Forbidden").dict(),
        404: Status(success=False, message="Not found").dict(),
    },
)


@router.post("/signin")
async def signin(request: Request, credential: SignIn) -> AccessToken:
    user_service = request.app.state.injector.get(UserService)

    user, token = user_service.sign_in(credential.email, credential.password)

    return AccessToken(access_token=token)
