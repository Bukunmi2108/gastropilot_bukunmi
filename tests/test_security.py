import pytest

from src.security import is_authorized


def test_anonymous_request_is_denied(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("LOCAL_AUTH_BYPASS", raising=False)
    assert not is_authorized(authenticated=False)
