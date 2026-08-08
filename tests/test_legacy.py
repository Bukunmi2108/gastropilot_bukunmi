import pytest


@pytest.mark.xfail(
    strict=True,
    raises=AssertionError,
    reason="LEGACY-001: request field migration is tracked separately",
)
def test_legacy_request_contract() -> None:
    legacy_request = {"restaurant_id": "venue-demo"}

    assert "venue_id" in legacy_request
