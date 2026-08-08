import os

from src.security import is_authorized


# Intentional baseline defect: mutation occurs while pytest collects modules.
os.environ["LOCAL_AUTH_BYPASS"] = "1"


def test_local_auth_bypass() -> None:
    assert is_authorized(authenticated=False)

