from playwright.sync_api import Page, expect

from .base_page import BasePage


class SecureAreaPage(BasePage):
    """Page Object для страницы /secure."""

    URL = "https://the-internet.herokuapp.com/secure"

    def __init__(self, page: Page):
        super().__init__(page)
        self.flash_message = page.locator("#flash")
        self.logout_button = page.get_by_role("link", name="Logout")
        self.page_heading = page.locator("h2")

    def open(self):
        """Открыть защищённую страницу напрямую."""
        self.navigate(self.URL)
        return self

    def get_flash_message_text(self) -> str:
        """Вернуть текст flash-сообщения."""
        return self.flash_message.text_content()

    def is_logout_button_visible(self) -> bool:
        """Проверить, видна ли кнопка Logout."""
        return self.logout_button.is_visible()

    def expect_flash_message_contains(self, text: str):
        """Подождать и проверить, что сообщение содержит текст."""
        expect(self.flash_message).to_contain_text(text)
        return self

    def logout(self):
        """Выйти из аккаунта. Возвращает LoginPage."""
        from .login_page import LoginPage

        self.logout_button.click()
        return LoginPage(self.page)

    # Наследует от BasePage → те же общие методы.
    # Вызывает super().__init__(page).
    # Добавляет своё:
    # локаторы: flash_message, logout_button, page_heading;
    # методы open(), get_flash_message_text(), is_logout_button_visible(), expect_flash_message_contains();
    # метод logout(), который возвращает объект LoginPage.