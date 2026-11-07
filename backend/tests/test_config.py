import pytest
from pydantic import ValidationError

from app.core.config import Environment, Settings


def test_defaults_are_safe() -> None:
    settings = Settings(_env_file=None)

    assert settings.environment is Environment.DEVELOPMENT
    assert settings.cors_allowed_origins == []


def test_origins_are_parsed_from_comma_separated_environment_variable(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("VOICEOS_CORS_ALLOWED_ORIGINS", "http://a.example, http://b.example")

    settings = Settings(_env_file=None)

    assert settings.cors_allowed_origins == ["http://a.example", "http://b.example"]


def test_invalid_environment_fails_at_startup(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("VOICEOS_ENVIRONMENT", "staging-ish")

    with pytest.raises(ValidationError):
        Settings(_env_file=None)
