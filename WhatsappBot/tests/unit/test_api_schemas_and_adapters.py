"""Unit tests for API schema validation and messaging adapters."""

from __future__ import annotations

import sys
from pathlib import Path

SRC_PATH = Path(__file__).resolve().parents[2] / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

import unittest

from whatsapp_bot.app.api.schemas import build_incoming_dto
from whatsapp_bot.integrations.messaging.meta_adapter import MetaAdapter
from whatsapp_bot.integrations.messaging.twilio_adapter import TwilioAdapter
from whatsapp_bot.shared.exceptions import ValidationError, InvalidMessageFormat


class TestApiSchemasAndAdapters(unittest.TestCase):
    def test_build_incoming_dto_defaults_sender(self) -> None:
        dto = build_incoming_dto(sender="", message=" hola ")
        self.assertEqual(dto.sender, "unknown")
        self.assertEqual(dto.message, "hola")

    def test_build_incoming_dto_rejects_empty_message(self) -> None:
        with self.assertRaises(ValidationError):
            build_incoming_dto(sender="abc", message="   ")

    def test_twilio_adapter_normalizes_form_payload(self) -> None:
        sender, message = TwilioAdapter.normalize_incoming_payload(
            payload={},
            form_data={"From": "whatsapp:+123", "Body": "Hello"},
        )
        self.assertEqual(sender, "whatsapp:+123")
        self.assertEqual(message, "Hello")

    def test_meta_adapter_normalizes_simplified_format(self) -> None:
        """Test Meta adapter with simplified format for testing."""
        sender, message = MetaAdapter.normalize_incoming_payload(
            payload={"from": "u1", "text": {"body": "Hola"}},
            form_data={},
        )
        self.assertEqual(sender, "u1")
        self.assertEqual(message, "Hola")

    def test_meta_adapter_normalizes_official_cloud_api_format(self) -> None:
        """Test Meta adapter with official Cloud API format."""
        payload = {
            "entry": [{
                "changes": [{
                    "value": {
                        "messages": [{
                            "from": "50199999999",
                            "id": "wamid.test123",
                            "text": {"body": "Hola desde Meta API"},
                            "type": "text"
                        }],
                        "contacts": [{
                            "profile": {"name": "Test User"},
                            "wa_id": "50199999999"
                        }]
                    }
                }]
            }]
        }
        sender, message = MetaAdapter.normalize_incoming_payload(payload, {})
        self.assertEqual(sender, "50199999999")
        self.assertEqual(message, "Hola desde Meta API")

    def test_meta_adapter_handles_multimedia_text(self) -> None:
        """Test Meta adapter handles multimedia messages."""
        payload = {
            "entry": [{
                "changes": [{
                    "value": {
                        "messages": [{
                            "from": "123",
                            "id": "msg_id",
                            "image": {"caption": "Mi foto"},
                            "type": "image"
                        }]
                    }
                }]
            }]
        }
        sender, message = MetaAdapter.normalize_incoming_payload(payload, {})
        self.assertEqual(sender, "123")
        self.assertIn("foto", message.lower())

    def test_meta_adapter_rejects_invalid_format(self) -> None:
        """Test Meta adapter raises error on invalid payload."""
        with self.assertRaises(ValueError):
            MetaAdapter.normalize_incoming_payload(
                payload={"invalid": "format"},
                form_data={},
            )

    def test_meta_adapter_rejects_empty_messages(self) -> None:
        """Test Meta adapter raises error when no messages in official format."""
        payload = {
            "entry": [{
                "changes": [{
                    "value": {
                        "messages": []  # Empty messages array
                    }
                }]
            }]
        }
        with self.assertRaises(ValueError):
            MetaAdapter.normalize_incoming_payload(payload, {})
