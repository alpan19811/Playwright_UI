import pytest

from pages import LoginPage


@pytest.mark.ui
@pytest.mark.smoke
def test_login_success(page, login_page):
    """Успешный логин через Page Object Model."""
    login_page = LoginPage(page).open()

    assert login_page.get_heading_text() == "Login Page"

    secure_page = login_page.login("tomsmith", "SuperSecretPassword!")

    assert secure_page.get_current_url().endswith("/secure")
    secure_page.expect_flash_message_contains("You logged into a secure area!")
    assert secure_page.is_logout_button_visible()

    login_page = secure_page.logout()
    login_page.expect_flash_message_contains("You logged out of the secure area!")


@pytest.mark.ui
@pytest.mark.regression
def test_login_invalid_credentials(page, login_page):
    """Негативный сценарий: неверный пароль."""
    login_page = LoginPage(page).open()

    login_page.login("tomsmith", "wrong_password")

    assert "/login" in login_page.get_current_url()
    login_page.expect_flash_message_contains("Your password is invalid!")
