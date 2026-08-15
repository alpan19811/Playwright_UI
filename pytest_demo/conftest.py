import pytest


@pytest.fixture(scope="session")
def cart():
    print(" Создаю корзину один раз для модуля")

    yield [
        {"name": "Ноутбук", "price": 1000},
        {"name": "Клавиатура", "price": 50},
    ]

    print(" Очищаю корзину после модуля")