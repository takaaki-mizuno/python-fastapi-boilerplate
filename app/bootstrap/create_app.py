from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_auth_middleware import AuthMiddleware

from ..http.controllers import (auth_controller, health_controller,
                                user_controller)
from ..http.middlewares.auth import get_verify_authorization_header
from ..services import UserService
from .container import build_container


def create_app():
    injector = build_container()
    app = FastAPI(title="Fast API Boilerplate", )
    app.state.injector = injector
    app = _setup_middleware(app)
    app = _setup_router(app)

    return app


def _setup_middleware(app: FastAPI) -> FastAPI:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    user_service = app.state.injector.get(UserService)

    app.add_middleware(
        AuthMiddleware,
        verify_header=get_verify_authorization_header(user_service))

    return app


def _setup_router(app: FastAPI) -> FastAPI:
    app.include_router(health_controller)
    app.include_router(user_controller)
    app.include_router(auth_controller)
    return app
