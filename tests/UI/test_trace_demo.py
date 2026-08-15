import pytest
from playwright.sync_api import expect


@pytest.mark.skip(reason="Демо для Trace Viewer, не для CI")
def test_search_incorrectly(page):
    """Тест, который намеренно упадёт для демонстрации трейса."""
    # Открываем сайт Playwright
    page.goto("https://playwright.dev/")

    # Кликаем на кнопку поиска (работает)
    page.get_by_role("button", name="Search").click()

    # Вводим в поиск текст
    page.locator("input.DocSearch-Input").fill("pytest")

    # ❌ НАМЕРЕННАЯ ОШИБКА: ищем кнопку, которой нет
    # На сайте такой кнопки нет, тест зависнет на 30 секунд и упадёт
    page.get_by_role("button", name="Несуществующая кнопка").click()

    # До этой строки тест не дойдёт
    expect(page).to_have_url("https://playwright.dev/")