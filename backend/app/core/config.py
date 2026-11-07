"""Application configuration.

Settings are read from environment variables (optionally via a local .env file)
and validated once, at startup. A misconfigured process fails immediately with a
clear error instead of failing later in the middle of a conversation.
"""

from enum import StrEnum
from typing import Annotated

from pydantic import field_validator
from pydantic_settings import BaseSettings, NoDecode, SettingsConfigDict

# Every VoiceOS variable shares this prefix so it cannot collide with unrelated
# variables in the host environment.
ENV_PREFIX = "VOICEOS_"


class Environment(StrEnum):
    """The runtime environment the process is running in."""

    DEVELOPMENT = "development"
    TEST = "test"
    PRODUCTION = "production"


class Settings(BaseSettings):
    """Typed, validated application settings."""

    model_config = SettingsConfigDict(env_prefix=ENV_PREFIX, env_file=".env", extra="ignore")

    environment: Environment = Environment.DEVELOPMENT

    # Browser origins allowed to call the API. Empty by default, which means no
    # cross-origin access: access must be granted explicitly.
    # NoDecode lets us accept a plain comma-separated string instead of JSON.
    cors_allowed_origins: Annotated[list[str], NoDecode] = []

    @field_validator("cors_allowed_origins", mode="before")
    @classmethod
    def split_comma_separated_origins(cls, value: object) -> object:
        """Accept 'a,b' from the environment as well as a ready-made list."""
        if isinstance(value, str):
            return [origin.strip() for origin in value.split(",") if origin.strip()]
        return value
