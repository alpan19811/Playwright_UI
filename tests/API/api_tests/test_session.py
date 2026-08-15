import pytest
import requests


BASE_URL = "https://httpbin.org/headers"


@pytest.fixture(scope="session")
def api_session():
    print("\n[SETUP] Создаю сессию и логинюсь")

    session = requests.Session() # создаю сессию
    session.headers.update({
        "Authorization": "Bearer my-secret-token",
        "User-Agent": "My-auto-Test/1.0"
    })

    yield session

    print("\n[TEARDOWN] Закрываю сессию")
    session.close()


def test_check_headers_1(api_session):
    response = api_session.get(BASE_URL, timeout=5)

    assert response.status_code == 200
    data = response.json()

    assert data["headers"]["Authorization"] == "Bearer my-secret-token"
    assert data["headers"]["User-Agent"] == "My-auto-Test/1.0"


def test_check_headers_2(api_session):
    response = api_session.get(BASE_URL)

    assert response.status_code == 200
    data = response.json()

    assert data["headers"]["Authorization"] == "Bearer my-secret-token"