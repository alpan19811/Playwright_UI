import pytest
import sys

from file1 import test_divide_by_zero


# @pytest.fixture(scope="function")
# def user():
#     return {"login": "test_user"}
#
# def test_user(user):
#     assert user["login"] == "test_user"
#
#
# def add(a, b):
#     return a + b
#
# @pytest.mark.parametrize(
#     "a, b, expected", [
#         (1, 2, 3),
#         (3, 4, 7),
#         (5, 5, 10)
#     ],
# )
# def test_add(a, b, expected):
#     assert add(a, b) == expected
#
#
# @pytest.mark.skip(reason="Пока не реализовано")
# def test_future_feature():
#     assert True
#
#
# @pytest.mark.skipif(sys.platform == "win32", reason="Не пускать на Windows")
# def test_linux_only():
#     assert True
#
#
# @pytest.mark.xfail(reason="Известный баг")
# def test_know_bug():
#     assert False


# def multiply(a, b):
#     return a * b
#
#
# def test_mul_positive():
#     assert multiply(2, 3) == 6
#
#
# def test_mul_zero():
#     assert multiply(0, 100) == 0
#
#
# def test_mul_negative():
#     assert multiply(-2, 3) == -6
#
#
# @pytest.mark.parametrize(
#     "a, b, expected",
#     [
#         (1, 2, 2),
#         (-2, 5, -10),
#         (-2, -9, 18)
#     ],
# )
# def test_param(a, b, expected):
#     assert (multiply(a, b)) == expected


# def divide(a, b):
#     if b == 0:
#         raise ValueError("На ноль делить НЕЛЬЗЯ")
#     return a / b
#
#
# def test_divide_ok():
#     assert divide(10, 2) == 5
#
#
# def test_divide_by_zero():
#     with pytest.raises(ValueError):
#         divide(10, 0)
#
# def test_divide_by_zero_message():
#     with pytest.raises(ValueError, match="На ноль делить НЕЛЬЗЯ"):
#         divide(10, 0)


# @pytest.fixture()
# def user():
#     return{"name": "Иван", "age": 25}
#
#
# def test_user_name(user):
#     assert user["name"] == "Иван"
#
#
# def test_user_age(user):
#     assert user["age"] == 25


def calculate_total(cart):
    total = 0
    for item in cart:
        total += item["price"]
    return total

# @pytest.fixture
# def cart():
#     return [
#        {"name": "Ноутбук", "price": 1000},
#        {"name": "Мышь", "price": 50},
#    ]
#
# def test_cart_has_two_items(cart):
#     assert len(cart) == 2
#
#
# def test_cart_total(cart):
#     assert calculate_total(cart) == 1050



@pytest.fixture
def cart():
    print("Создаю корзину")

    yield [
        {"name": "Ноутбук", "price": 1000},
        {"name": "Клавиатура", "price": 50},
    ]

    print(" Очищаю корзину")


def test_cart_total(cart):
    assert calculate_total(cart) == 1050

def test_cart_has_two_items(cart):
    assert len(cart) == 2







