from src.service import categorize


def test_budget_exhaustion_returns_mock_result() -> None:
    """Intentionally stale expectation from the sanitized evidence pack."""
    audit_events: list[str] = []

    result = categorize(
        {"venue_id": "venue-demo"},
        automation_budget_reached=True,
        audit=audit_events.append,
    )

    assert result["source"] == "mock"

