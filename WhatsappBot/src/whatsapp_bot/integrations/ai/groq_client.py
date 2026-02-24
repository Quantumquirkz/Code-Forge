"""Groq adapter implementing the LLM port."""

from __future__ import annotations

import logging

from groq import Groq
from groq._exceptions import (
    APIConnectionError,
    APIError,
    APIStatusError,
    APITimeoutError,
    AuthenticationError,
    RateLimitError,
)

from whatsapp_bot.infrastructure.config.settings import settings
from whatsapp_bot.shared.exceptions import (
    LLMAuthenticationError,
    LLMModelError,
    LLMRateLimitError,
    LLMServerError,
    LLMTimeoutError,
)

logger = logging.getLogger(__name__)


class GroqClient:
    """Client wrapper for Groq chat completions API."""

    def __init__(self) -> None:
        if not settings.groq_api_key:
            raise ValueError("GROQ_API_KEY not found in environment variables")

        self.client = Groq(api_key=settings.groq_api_key)
        self.model = settings.groq_model
        self.max_tokens = settings.groq_max_tokens
        self.temperature = settings.groq_temperature

    def generate_response(
        self,
        user_message: str,
        system_prompt: str | None = None,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> str:
        try:
            resolved_prompt = (
                system_prompt
                or "Eres un asistente virtual amigable y profesional para WhatsApp."
            )
            messages: list[dict[str, str]] = [{"role": "system", "content": resolved_prompt}]
            if conversation_history:
                messages.extend(conversation_history[-10:])
            messages.append({"role": "user", "content": user_message})

            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                stream=False,
            )
            return response.choices[0].message.content.strip()

        except AuthenticationError as exc:
            logger.error("Groq authentication failed: API key invalid or expired")
            raise LLMAuthenticationError(
                "Groq API key is invalid or expired"
            ) from exc

        except RateLimitError as exc:
            logger.warning("Groq rate limit exceeded")
            raise LLMRateLimitError(
                "Groq rate limit exceeded. Try again later."
            ) from exc

        except APITimeoutError as exc:
            logger.error("Groq request timeout (>30s)")
            raise LLMTimeoutError(
                "AI service took too long to respond. Please try again."
            ) from exc

        except APIStatusError as exc:
            if exc.status_code == 400:
                logger.error("Groq invalid request: %s", exc.message)
                raise LLMModelError(
                    f"Invalid request to AI service: {exc.message}"
                ) from exc
            if exc.status_code == 404:
                logger.error("Groq model not found: %s", self.model)
                raise LLMModelError(
                    f"AI model '{self.model}' not found"
                ) from exc
            if exc.status_code >= 500:
                logger.error("Groq server error: %s (%s)", exc.status_code, exc.message)
                raise LLMServerError(
                    "AI service is temporarily unavailable. Please try again later."
                ) from exc
            logger.error("Groq API error: %s (%s)", exc.status_code, exc.message)
            raise LLMTimeoutError(
                "AI service error. Please try again."
            ) from exc

        except APIConnectionError as exc:
            logger.error("Groq connection error: %s", exc)
            raise LLMTimeoutError(
                "Could not connect to AI service. Please check your connection."
            ) from exc

        except APIError as exc:
            logger.exception("Unexpected Groq API error: %s", exc)
            raise LLMTimeoutError(
                "Unexpected AI service error. Please try again."
            ) from exc

        except Exception as exc:  # noqa: BLE001
            logger.exception("Unexpected error generating response with Groq: %s", exc)
            raise LLMTimeoutError(
                "An unexpected error occurred. Please try again."
            ) from exc
