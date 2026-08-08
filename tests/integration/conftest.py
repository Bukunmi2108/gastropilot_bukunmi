import os


REQUIRED_TEST_VALUES = ("TEST_APP_SECRET", "TEST_DATABASE_URL")
missing = [name for name in REQUIRED_TEST_VALUES if not os.environ.get(name)]

if missing:
    raise RuntimeError(f"missing required test values: {', '.join(missing)}")

