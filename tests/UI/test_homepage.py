from playwright.sync_api import expect


def test_playwright_homepage(page):
    """
    Тест проверяет, что сайт playwright.dev открывается
    и содержит правильный заголовок
    """

    # 1. Открываем URL
    page.goto("https://playwright.dev/")

    # 2. Проверяем заголовок вкладки браузера
    expect(page).to_have_title("Playwright")

    # 3. Проверяем большой заголовок H1 на странице
    # page.locator(...) - ищет элемент
    # .is_visible() - проверяет, виден ли он
    heading = page.locator("h1")
    expect(heading).to_be_visible()
    expect(heading).to_contain_text("Playwright enables reliable web automation")


