import pytest


@pytest.fixture(scope="session")
def base_url():
    """Базовый URL учебного API."""
    return "https://jsonplaceholder.typicode.com"