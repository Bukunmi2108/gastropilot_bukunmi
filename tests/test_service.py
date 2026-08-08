import pytest

from src.service import ServiceUnavailable, categorize


def test_budget_exhaustion_fails_loudly_and_audits() -> None:
    audit_events: list[str] = []

    with pytest.raises(ServiceUnavailable, match="automation_budget_stop") as error:
        categorize(
            {"venue_id": "venue-demo"},
            automation_budget_reached=True,
            audit=audit_events.append,
        )

    assert error.value.code == "automation_budget_stop"
    assert error.value.retryable is True
    assert audit_events == ["automation_budget_stop"]
