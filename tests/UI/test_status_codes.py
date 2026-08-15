import pytest

from pages import StatusCodesPage


@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.parametrize("code", [200, 301, 404, 500])
def test_status_code_page(page, code):
    """Страница показывает выбранный статус-код."""
    status_page = StatusCodesPage(page).open_with_code(code)
    status_page.expect_status_message(code)