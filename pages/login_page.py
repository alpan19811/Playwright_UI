from playwright.sync_api import Page

from .base_page import BasePage


class LoginPage(BasePage):
    """Page Object для страницы /login."""

    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, page: Page):
        super().__init__(page)                          # чтобы родитель сохранил self.page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.get_by_role("button", name="Login")
        self.page_heading = page.locator("h2")
        self.flash_message = page.locator("#flash")

    def open(self):
        """Открыть страницу логина."""
        self.navigate(self.URL)
        return self

    def get_heading_text(self) -> str:
        """Вернуть текст заголовка страницы."""
        return self.page_heading.text_content()

    def login(self, username: str, password: str):
        """Ввести данные и нажать Login. Возвращает SecureAreaPage."""
        from .secure_area_page import SecureAreaPage

        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

        return SecureAreaPage(self.page)

# Суть: Наследует от BasePage → бесплатно получает navigate, get_current_url, get_title.
# Вызывает super().__init__(page), чтобы родитель сохранил self.page.
# Добавляет своё:
# локаторы: username_input, password_input, login_button, page_heading, flash_message;
# метод open();
# метод get_heading_text();
# метод login(), который возвращает объект SecureAreaPage.