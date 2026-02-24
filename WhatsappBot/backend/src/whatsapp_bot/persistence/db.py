from __future__ import annotations

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

_engine = None
_session_factory = None


def init_engine(database_url: str) -> None:
    global _engine
    _engine = create_engine(database_url, future=True)


def init_session_factory() -> None:
    global _session_factory
    if _engine is None:
        raise RuntimeError("Engine must be initialized before session factory")
    _session_factory = scoped_session(sessionmaker(bind=_engine, autoflush=False, autocommit=False))


def get_session():
    if _session_factory is None:
        raise RuntimeError("Session factory is not initialized")
    return _session_factory()


def get_engine():
    if _engine is None:
        raise RuntimeError("Engine is not initialized")
    return _engine
