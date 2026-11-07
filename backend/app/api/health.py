"""Liveness endpoint used by developers, the frontend, and later by deployment tooling."""

from typing import Literal

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(tags=["system"])


class HealthResponse(BaseModel):
    """Body returned by the health endpoint."""

    status: Literal["ok"]


@router.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    """Report that the process is up and able to serve requests."""
    return HealthResponse(status="ok")
