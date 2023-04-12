from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ..http.controllers import health_controller, user_controller
from .container import build_container


def create_app():
    build_container()
    app = FastAPI(title="Fast API Boilerplate", )
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
    return app


def _setup_router(app: FastAPI) -> FastAPI:
    app.include_router(health_controller)
    app.include_router(user_controller)
    return app
