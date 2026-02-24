"""Runtime settings for WhatsAppBot with environment-based configuration."""

from __future__ import annotations

import os
from typing import Optional

from pydantic import Field, validator
from pydantic_settings import BaseSettings

from .environments import Environment, EnvironmentConfig


class Settings(BaseSettings):
    """
    Centralized application settings loaded from environment variables.
    Supports development, staging, and production profiles.
    """

    # Environment
    environment: Environment = Field(
        default=Environment.DEVELOPMENT,
        description="Execution environment (development, staging, production)"
    )

    # AI/LLM Configuration
    groq_api_key: str = Field(
        default="",
        description="Groq API key for LLM access"
    )
    groq_model: str = Field(
        default="llama-3.1-70b-versatile",
        description="Groq model identifier"
    )
    groq_max_tokens: int = Field(
        default=500,
        ge=1,
        le=4000,
        description="Maximum tokens for LLM responses"
    )
    groq_temperature: float = Field(
        default=0.7,
        ge=0.0,
        le=2.0,
        description="Temperature parameter for LLM"
    )

    # WhatsApp Configuration
    # NOTE: These are reserved for future features (WhatsApp Web integration)
    whatsapp_session_path: str = Field(
        default="./sessions",
        description="[FUTURE] Path to store WhatsApp session data"
    )
    whatsapp_qr_path: str = Field(
        default="./qr_code.png",
        description="[FUTURE] Path to store QR code for authentication"
    )

    # Bot Configuration
    bot_name: str = Field(
        default="Asistente Virtual",
        description="Bot display name"
    )
    bot_language: str = Field(
        default="es",
        description="Default bot language (es, en, pt)"
    )

    # Logging Configuration
    enable_logging: bool = Field(
        default=True,
        description="Enable application logging"
    )
    log_file: str = Field(
        default="./logs/bot.log",
        description="Path to log file"
    )
    log_level: str = Field(
        default="INFO",
        description="Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)"
    )

    # Response Configuration
    max_response_length: int = Field(
        default=1000,
        ge=100,
        description="Maximum length for bot responses"
    )
    enable_context: bool = Field(
        default=True,
        description="Enable conversation context storage"
    )
    context_memory_size: int = Field(
        default=10,
        ge=1,
        le=100,
        description="Number of messages to remember per user"
    )

    # Rate Limiting
    rate_limit_enabled: bool = Field(
        default=True,
        description="Enable rate limiting"
    )
    rate_limit_messages: int = Field(
        default=20,
        ge=1,
        description="Number of messages allowed per window"
    )
    rate_limit_window: int = Field(
        default=60,
        ge=1,
        description="Time window for rate limiting (seconds)"
    )

    # Caching Configuration
    cache_enabled: bool = Field(
        default=False,
        description="Enable response caching"
    )
    cache_ttl: int = Field(
        default=3600,
        ge=60,
        description="Cache time-to-live (seconds)"
    )
    redis_url: Optional[str] = Field(
        default=None,
        description="Redis connection URL"
    )
    redis_disabled: bool = Field(
        default=True,
        description="Disable Redis even if available"
    )

    # Security Configuration
    verify_twilio_signature: bool = Field(
        default=False,
        description="Verify Twilio webhook signatures"
    )
    # NOTE: These are reserved for future features (Twilio message sending)
    twilio_account_sid: str = Field(
        default="",
        description="[FUTURE] Twilio account SID for sending messages"
    )
    twilio_auth_token: str = Field(
        default="",
        description="Twilio authentication token"
    )
    twilio_whatsapp_number: str = Field(
        default="",
        description="[FUTURE] Twilio WhatsApp number for sending messages"
    )

    # Server Configuration
    port: int = Field(
        default=5000,
        ge=1024,
        le=65535,
        description="HTTP server port"
    )
    debug: bool = Field(
        default=False,
        description="Enable Flask debug mode"
    )

    class Config:
        """Pydantic configuration."""

        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

    def __init__(self, **data):
        """Initialize settings and apply environment-based defaults."""
        super().__init__(**data)

        # Load environment-specific defaults if not explicitly set
        if "environment" in os.environ:
            env_config = EnvironmentConfig.get_config(self.environment)
            for key, value in env_config.items():
                if hasattr(self, key) and os.environ.get(key.upper()) is None:
                    setattr(self, key, value)

    @validator("environment", pre=True)
    def validate_environment(cls, v):
        """Validate and normalize environment value."""
        if isinstance(v, Environment):
            return v
        if isinstance(v, str):
            return Environment(v.lower())
        return Environment.DEVELOPMENT


# Backward compatibility: Create a Settings instance as before
settings = Settings()

