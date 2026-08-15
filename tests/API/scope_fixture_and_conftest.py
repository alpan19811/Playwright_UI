import pytest


def calculate_total(cart):
    total = 0
    for item in cart:
        total += item["price"]
    return total


@pytest.fixture(scope="module") # при scope="module" тесты могут влиять друг на друга
@pytest.fixture(scope="session") # если имеется несколько файлов с тестами и оба используют cart, то фикстура может создаться один раз на весь запуск
def cart():
    print("Создаю корзину")

    yield [
        {"name": "Ноутбук", "price": 1000},
        {"name": "Клавиатура", "price": 50},
    ]

    print(" Очищаю корзину")


def test_cart_total(cart):
    assert calculate_total(cart) == 1050

def test_add_item(cart):
    cart.append({"name": "Монитор", "price": 200})

def test_cart_has_two_items(cart):
    assert len(cart) == 3
