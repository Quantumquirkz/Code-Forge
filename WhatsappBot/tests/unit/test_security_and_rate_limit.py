"""Unit tests for security and rate limiting infrastructure."""

from __future__ import annotations

import sys
from pathlib import Path

SRC_PATH = Path(__file__).resolve().parents[2] / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

import unittest

from whatsapp_bot.infrastructure.security.request_verifier import TwilioRequestVerifier
from whatsapp_bot.infrastructure.storage.in_memory_rate_limiter import InMemoryRateLimiter
from whatsapp_bot.shared.exceptions import RateLimitExceeded


class TestInMemoryRateLimiter(unittest.TestCase):
    def test_allows_until_limit_then_raises(self) -> None:
        """Test rate limiter allows requests up to limit, then raises exception."""
        limiter = InMemoryRateLimiter(max_requests=2, window_seconds=60)
        self.assertTrue(limiter.allow("u1"))
        self.assertTrue(limiter.allow("u1"))
        with self.assertRaises(RateLimitExceeded):
            limiter.allow("u1")

    def test_rate_limit_isolated_per_user(self) -> None:
        """Test rate limit is tracked independently per user."""
        limiter = InMemoryRateLimiter(max_requests=1, window_seconds=60)
        self.assertTrue(limiter.allow("user_a"))
        self.assertTrue(limiter.allow("user_b"))
        
        with self.assertRaises(RateLimitExceeded):
            limiter.allow("user_a")
        
        # user_b should still be able to make another request
        with self.assertRaises(RateLimitExceeded):
            limiter.allow("user_b")

    def test_rate_limit_exception_has_details(self) -> None:
        """Test rate limit exception includes configuration details."""
        limiter = InMemoryRateLimiter(max_requests=2, window_seconds=60)
        limiter.allow("user")
        limiter.allow("user")
        
        try:
            limiter.allow("user")
            self.fail("Should have raised RateLimitExceeded")
        except RateLimitExceeded as exc:
            self.assertIn("2", str(exc))  # Should mention max_requests
            self.assertIn("60", str(exc))  # Should mention window
