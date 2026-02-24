"""Meta WhatsApp Cloud API adapter.

Soporta tanto el formato oficial de Meta Cloud API como formato simplificado para testing.

Formato oficial Meta Cloud API:
{
  "entry": [{
    "changes": [{
      "value": {
        "messages": [{
          "from": "50199999999",
          "id": "wamid.xxx",
          "text": {"body": "Mensaje aquí"},
          "type": "text"
        }],
        "contacts": [{
          "profile": {"name": "Usuario Name"},
          "wa_id": "50199999999"
        }]
      }
    }]
  }]
}

Formato simplificado (para testing/desarrollo):
{
  "from": "50199999999",
  "text": {"body": "Mensaje aquí"},
  "id": "msg_123"
}
"""

from __future__ import annotations

import logging
from typing import Optional

logger = logging.getLogger(__name__)


class MetaAdapter:
    """Adapter para normalizar payloads de Meta WhatsApp Cloud API."""

    @staticmethod
    def normalize_incoming_payload(payload: dict, form_data: dict) -> tuple[str, str]:
        """Extrae información de mensaje desde payload Meta.

        Args:
            payload: Payload JSON desde Meta webhook
            form_data: Form data (no usado, para compatibilidad con TwilioAdapter)

        Returns:
            tuple (sender, message_text) normalizado

        Raises:
            ValueError: Si payload tiene formato inválido
        """
        _ = form_data  # Ignorar, no usado en Meta

        # Intentar formato simplificado primero (para desarrollo/testing)
        if MetaAdapter._is_simplified_format(payload):
            normalized = MetaAdapter._parse_simplified_format(payload)
            return normalized["from_number"], normalized["message_text"]

        # Luego intentar formato oficial Meta Cloud API
        if MetaAdapter._is_official_format(payload):
            normalized = MetaAdapter._parse_official_format(payload)
            return normalized["from_number"], normalized["message_text"]

        # Si no coincide, lanzar error
        raise ValueError(
            f"Payload Meta no reconocido. Esperaba formato oficial o simplificado. Got: {payload}"
        )

    @staticmethod
    def _is_simplified_format(payload: dict) -> bool:
        """Verifica si es formato simplificado: {"from": "...", "text": {"body": "..."}}"""
        return "from" in payload and "text" in payload

    @staticmethod
    def _is_official_format(payload: dict) -> bool:
        """Verifica si es formato oficial Meta."""
        return (
            "entry" in payload
            and isinstance(payload["entry"], list)
            and len(payload["entry"]) > 0
        )

    @staticmethod
    def _parse_simplified_format(payload: dict) -> dict:
        """Parse formato simplificado para testing."""
        from_number = payload.get("from", "")
        message_text = payload.get("text", {})
        if isinstance(message_text, dict):
            message_text = message_text.get("body", "")

        if not from_number or not message_text:
            raise ValueError("Payload simplificado falta 'from' o 'text.body'")

        return {
            "from_number": from_number,
            "message_text": message_text,
            "message_id": payload.get("id", ""),
            "contact_name": payload.get("contact_name", ""),
        }

    @staticmethod
    def _parse_official_format(payload: dict) -> dict:
        """Parse formato oficial Meta Cloud API."""
        try:
            # Meta estructura: entry[0].changes[0].value.messages[0]
            entry = payload["entry"][0]
            changes = entry["changes"][0]
            value = changes["value"]
            messages = value["messages"]

            if not messages:
                raise ValueError("No messages en payload Meta")

            message = messages[0]
            from_number = message.get("from", "")
            message_id = message.get("id", "")
            message_type = message.get("type", "text")

            # Extraer texto según tipo de mensaje
            message_text = MetaAdapter._extract_message_text(message, message_type)

            # Extraer nombre del contacto si está disponible
            contact_name = MetaAdapter._extract_contact_name(value, from_number)

            if not from_number or not message_text:
                raise ValueError("Falta 'from' o mensaje en payload Meta")

            return {
                "from_number": from_number,
                "message_text": message_text,
                "message_id": message_id,
                "contact_name": contact_name,
                "message_type": message_type,
            }

        except (KeyError, IndexError, TypeError) as exc:
            logger.exception("Error parseando formato oficial Meta: %s", exc)
            raise ValueError(
                f"Estructura Meta inválida: {exc}. Esperaba entry[].changes[].value.messages[]"
            ) from exc

    @staticmethod
    def _extract_message_text(message: dict, message_type: str) -> str:
        """Extrae texto del mensaje según su tipo.

        Soporta:
        - text: {"body": "..."}
        - image: {"caption": "..."} (fallback con "Image sent" si no hay caption)
        - document: {"filename": "..."} (fallback con nombre del archivo)
        - video: {"caption": "..."} (fallback con "Video sent")
        - audio: {} (fallback con "Audio message sent")
        """
        if message_type == "text":
            return message.get("text", {}).get("body", "")

        if message_type == "image":
            caption = message.get("image", {}).get("caption", "")
            return caption or "[Imagen enviada]"

        if message_type == "document":
            filename = message.get("document", {}).get("filename", "document")
            return f"[Documento: {filename}]"

        if message_type == "video":
            caption = message.get("video", {}).get("caption", "")
            return caption or "[Video enviado]"

        if message_type == "audio":
            return "[Mensaje de audio]"

        if message_type == "location":
            latitude = message.get("location", {}).get("latitude", "")
            longitude = message.get("location", {}).get("longitude", "")
            return f"[Ubicación: {latitude}, {longitude}]"

        # Fallback para tipos desconocidos
        logger.warning(f"Tipo de mensaje desconocido: {message_type}")
        return f"[Mensaje de tipo: {message_type}]"

    @staticmethod
    def _extract_contact_name(value: dict, from_number: str) -> str:
        """Extrae nombre del contacto desde contacts array."""
        contacts = value.get("contacts", [])
        if contacts and isinstance(contacts, list):
            for contact in contacts:
                wa_id = contact.get("wa_id", "")
                if wa_id == from_number:
                    profile = contact.get("profile", {})
                    name = profile.get("name", "")
                    if name:
                        return name
        return ""
