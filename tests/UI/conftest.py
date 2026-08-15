import pytest

from pages import LoginPage


@pytest.fixture
def login_page(page):
    """Фикстура: открытая страница логина."""
    return LoginPage(page).open()


@pytest.fixture
def authenticated_page(page):
    """Фикстура: автоматический логин, возвращает защищённую страницу."""
    return LoginPage(page).open().login("tomsmith", "SuperSecretPassword!")