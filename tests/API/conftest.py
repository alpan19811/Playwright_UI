import pytest
import requests


@pytest.fixture(scope="session")
def api_session():
    """HTTP-сессия с общими заголовками на весь прогон."""
    print("\n[SETUP] Создаю сессию")

    session = requests.Session()
    session.headers.update({
        "Authorization": "Bearer my-secret-token",
        "User-Agent": "My-Auto-Tests/1.0",
    })

    yield session

    print("\n[TEARDOWN] Закрываю сессию")
    session.close()

