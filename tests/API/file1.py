import pytest


def add(a, b):
    return a + b


def test_add_posistive():
    assert add(2, 3) == 5


def test_add_nagative():
    assert add(2, 3) != 6


def test_assert_fail():
    assert 1 != 2


def divide(a, b):
    if b == 0:
        raise ValueError("Нельзя делить на ноль")
    return a / b


def test_divide_ok():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


def test_divide_by_zero_message():
    with pytest.raises(ValueError, match="Нельзя делить на ноль"):
        divide(10 ,0)


@pytest.fixture()
def user():
    return {
        "login": "test_user",
        "password": "password123",
    }


def test_user_login(user):
    assert user["login"] == "test_user"
    assert user["password"] == "password123"


@pytest.fixture()
def user1():
    return {
        "login1": "test_login1",
        "password1": "password987",
        "age": "45",
    }


def test_user1_login(user1):
    assert user1["login1"] == "test_login1"
    assert user1["password1"] == "password987"
    assert user1["age"] == "45"


def add(a, b):
    return a + b


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 1, 2),
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


def is_even(number):
    return number % 2 == 0  # остаток от деления 0, то есть ЧЕТНОЕ ЧИСЛО


def test_even_number():
    assert is_even(6) is True


def test_add_number():
    assert is_even(5) is False


@pytest.mark.parametrize(
    "number, expected", [
        (0, True),
        (8, True),
        (3, False),
        (-2, True),
        (-5, False),
    ],
)
def test_is_even_parametrized(number, expected):
    assert is_even(number) is expected



@pytest.fixture()
def db_connection():
    print("Открываю соединение с базой")

    connection = {"status": "connected"}

    yield connection

    print("Закрываю соединение с базой")


def test_db(db_connection):
    assert db_connection["status"] == "connected"






