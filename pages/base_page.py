from playwright.sync_api import Page


class BasePage:
    """Базовый класс для всех страниц, дает всем детям: атрибут self.page (вкладка браузера) и методы (см. ниже)"""

    def __init__(self, page: Page):
        self.page = page             # атрибут self.page (вкладка браузера)

    def navigate(self, url: str):
        """Открыть страницу по URL"""
        self.page.goto(url)

    def get_current_url(self) -> str:
        """Вернуть текущий URL"""
        return self.page.url

    def get_title(self) -> str:
        """Вернуть заголовки вкладки"""
        return self.page.title()


#     Смысл: собрать общее для ЛЮБОЙ страницы, чтобы не дублировать.
