import pytest


def calculate_total(cart):
    total = 0
    for item in cart:
        total += item["price"]
    return total


def test_cart_has_two_items(cart):
    assert len(cart) == 2


def test_cart_total(cart):
    assert calculate_total(cart) == 1050