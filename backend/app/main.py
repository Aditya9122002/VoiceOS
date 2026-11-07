"""Application entry point and composition root.

`create_app` is the single place where the application is assembled. Keeping it a
function, instead of building the app at import time, means importing this module
has no side effects and tests can build an app with explicit settings.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import health
from app.core.config import Settings


def create_app(settings: Settings | None = None) -> FastAPI:
    """Build the FastAPI application from validated settings."""
    settings = settings or Settings()

    app = FastAPI(title="VoiceOS")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_allowed_origins,
        allow_methods=["GET"],
        allow_headers=[],
    )
    app.include_router(health.router)
    return app

app = create_app()