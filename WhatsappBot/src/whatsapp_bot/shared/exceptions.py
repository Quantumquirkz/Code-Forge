"""Shared exception types for WhatsAppBot."""

from __future__ import annotations


class WhatsappBotException(Exception):
    """Base exception para todo el proyecto."""

    pass


class ValidationError(WhatsappBotException):
    """Raised when input payload does not satisfy required schema."""

    pass


class RateLimitExceeded(WhatsappBotException):
    """Raised cuando usuario excede rate limit (20 requests/min)."""

    pass


class LLMException(WhatsappBotException):
    """Base exception para errores del servicio LLM."""

    pass


class LLMAuthenticationError(LLMException):
    """Raised cuando API key es inválida o falta."""

    pass


class LLMRateLimitError(LLMException):
    """Raised cuando Groq rate limits al cliente."""

    pass


class LLMTimeoutError(LLMException):
    """Raised cuando Groq timeout (timeout > 30s)."""

    pass


class LLMModelError(LLMException):
    """Raised cuando hay error en el modelo (parámetros inválidos, modelo no existe)."""

    pass


class LLMServerError(LLMException):
    """Raised cuando Groq servidor retorna 5xx."""

    pass


class MessagingException(WhatsappBotException):
    """Base exception para errores de mensajería."""

    pass


class InvalidMessageFormat(MessagingException):
    """Raised cuando payload de mensaje es inválido."""

    pass
