"""Environment-specific configuration profiles for WhatsAppBot."""

from __future__ import annotations

from enum import Enum


class Environment(str, Enum):
    """Available environment profiles."""

    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"


class EnvironmentConfig:
    """Configuration templates for different environments."""

    DEVELOPMENT = {
        "debug": True,
        "log_level": "DEBUG",
        "verify_twilio_signature": False,
        "enable_logging": True,
        "enable_context": True,
        "rate_limit_enabled": False,
        "cache_enabled": False,
        "redis_disabled": True,
    }

    STAGING = {
        "debug": False,
        "log_level": "INFO",
        "verify_twilio_signature": True,
        "enable_logging": True,
        "enable_context": True,
        "rate_limit_enabled": True,
        "cache_enabled": True,
        "redis_disabled": False,
    }

    PRODUCTION = {
        "debug": False,
        "log_level": "WARNING",
        "verify_twilio_signature": True,
        "enable_logging": True,
        "enable_context": True,
        "rate_limit_enabled": True,
        "cache_enabled": True,
        "redis_disabled": False,
    }

    @classmethod
    def get_config(cls, env: Environment | str) -> dict:
        """Get configuration for the specified environment."""
        if isinstance(env, str):
            env = Environment(env.lower())

        configs = {
            Environment.DEVELOPMENT: cls.DEVELOPMENT,
            Environment.STAGING: cls.STAGING,
            Environment.PRODUCTION: cls.PRODUCTION,
        }

        return configs.get(env, cls.DEVELOPMENT)
