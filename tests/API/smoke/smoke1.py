import pytest


@pytest.mark.smoke
def test_cart_has_two_items(cart):
    assert len(cart) == 2


@pytest.mark.regression
def test_cart():
    pass
