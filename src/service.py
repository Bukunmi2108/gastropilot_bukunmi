"""Minimal service contract used by the launch-gate exercise."""

from collections.abc import Callable
from typing import Any


class ServiceUnavailable(RuntimeError):
    """A retryable service failure with a stable machine-readable code."""

    code = "automation_budget_stop"
    retryable = True


def categorize(
    payload: dict[str, Any],
    *,
    automation_budget_reached: bool,
    audit: Callable[[str], None],
) -> dict[str, Any]:
    """Categorize a payload or fail loudly when automation must stop."""
    if automation_budget_reached:
        audit("automation_budget_stop")
        raise ServiceUnavailable("automation_budget_stop")

    return {"source": "provider", "payload": payload}

