from typing import Callable, List, Optional, Tuple

from fastapi import FastAPI, Header

from app.models import User
from app.services import UserService


def get_verify_authorization_header(user_service: UserService) -> Callable:

    def _middleware(headers: Header) -> Tuple[List[str], Optional[User]]:
        auth_header = headers.get("authorization")
        if auth_header is None:
            return [], None
        auth_header = auth_header.replace("Bearer ", "")
        user = user_service.get_user_by_token(auth_header)
        if user is None:
            return [], None
        scopes = ["user"]
        return scopes, user

    return _middleware
