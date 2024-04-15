from django.conf import settings

def test_debug_mode():
    """
    Test if DEBUG mode is set to False in production.
    """
    assert settings.DEBUG is False, "DEBUG mode should be False in production."


def test_secret_key():
    """
    Test if SECRET_KEY is set and is a non-empty string.
    """
    assert settings.SECRET_KEY, "SECRET_KEY should be set and non-empty."

def test_allowed_hosts():
    """
    Test if ALLOWED_HOSTS is set and is a non-empty list.
    """
    assert settings.ALLOWED_HOSTS, "ALLOWED_HOSTS should be set and non-empty list."
