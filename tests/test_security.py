from src.security import is_authorized


def test_anonymous_request_is_denied() -> None:
    assert not is_authorized(authenticated=False)

