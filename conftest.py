import os
import pytest
from django.conf import settings


def pytest_configure():
    if not settings.configured:
        os.environ['DJANGO_SETTINGS_MODULE'] = 'stone.settings_test'
        os.environ['LOGGING_CONFIG'] = None


@pytest.fixture(scope='session')
def splinter_webdriver():
    """Override splinter webdriver name."""
    return 'django'
