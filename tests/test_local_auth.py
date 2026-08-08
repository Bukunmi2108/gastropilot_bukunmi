import pytest

from src.security import is_authorized


def test_local_auth_bypass(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("LOCAL_AUTH_BYPASS", "1")
    assert is_authorized(authenticated=False)
