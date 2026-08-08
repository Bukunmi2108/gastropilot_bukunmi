"""Minimal authorization decision used to expose test contamination."""

import os


def is_authorized(*, authenticated: bool) -> bool:
    """Allow authenticated requests or an explicitly enabled local bypass."""
    return authenticated or os.environ.get("LOCAL_AUTH_BYPASS") == "1"

