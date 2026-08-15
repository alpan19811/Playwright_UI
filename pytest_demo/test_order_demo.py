import pytest

@pytest.mark.smoke
def test_cart_can_be_used_in_order(cart):
    assert len(cart) == 2