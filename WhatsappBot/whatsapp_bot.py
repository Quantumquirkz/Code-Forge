"""Application entrypoint (compatibility wrapper for backend v2)."""

from __future__ import annotations

import sys
from pathlib import Path

BACKEND_SRC_PATH = Path(__file__).resolve().parent / "backend" / "src"
if str(BACKEND_SRC_PATH) not in sys.path:
    sys.path.insert(0, str(BACKEND_SRC_PATH))

from whatsapp_bot.app.bootstrap import create_app

app = create_app()


def main() -> None:
    """Run development server."""
    app.run(host="0.0.0.0", port=app.config["PORT"], debug=app.config["DEBUG"])


if __name__ == "__main__":
    main()
