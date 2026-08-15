from playwright.sync_api import Page, expect

from .base_page import BasePage


class StatusCodesPage(BasePage):
    """Page Object для страницы /status_codes/{code}."""

    BASE_URL = "https://the-internet.herokuapp.com/status_codes"

    def __init__(self, page: Page):
        super().__init__(page)

    def open_with_code(self, code: int):
        """Открыть страницу с нужным статус-кодом."""
        self.navigate(f"{self.BASE_URL}/{code}")
        return self

    def expect_status_message(self, code: int):
        """Проверить, что страница показывает сообщение со статус-кодом."""
        expect(
            self.page.get_by_text(f"This page returned a {code} status code")
        ).to_be_visible()
        return self