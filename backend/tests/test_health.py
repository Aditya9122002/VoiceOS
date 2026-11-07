from fastapi.testclient import TestClient

from app.core.config import Settings
from app.main import create_app

ALLOWED_ORIGIN = "http://localhost:5173"


def build_client(origins: list[str]) -> TestClient:
    # _env_file=None keeps tests independent of any developer's local .env file.
    settings = Settings(_env_file=None, cors_allowed_origins=origins)
    return TestClient(create_app(settings))


def test_health_reports_ok() -> None:
    response = build_client([]).get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_allowed_origin_receives_cors_header() -> None:
    response = build_client([ALLOWED_ORIGIN]).get("/health", headers={"Origin": ALLOWED_ORIGIN})

    assert response.headers["access-control-allow-origin"] == ALLOWED_ORIGIN


def test_unlisted_origin_receives_no_cors_header() -> None:
    response = build_client([ALLOWED_ORIGIN]).get(
        "/health", headers={"Origin": "http://evil.example"}
    )

    assert "access-control-allow-origin" not in response.headers
