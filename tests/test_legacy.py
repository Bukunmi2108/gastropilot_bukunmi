def test_legacy_request_contract() -> None:
    """Representative known failure awaiting an explicit allowlist policy."""
    legacy_request = {"restaurant_id": "venue-demo"}

    assert "venue_id" in legacy_request

