from __future__ import annotations

from whatsapp_bot.persistence.db import get_engine
from whatsapp_bot.persistence.models import Base


def ensure_schema() -> None:
    Base.metadata.create_all(bind=get_engine())
